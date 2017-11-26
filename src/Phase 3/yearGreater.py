from bsddb3 import db

DB_File = "ye.idx"
database = db.DB()
database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
curs = database.cursor()

def yearSearch(Starting_Year):
    
    middleSet = set()
    result = curs.set_range(str(Starting_Year).encode("utf-8")) 
    if(result != None):
        while(result != None): 
            middleSet.add(str(result[1].decode("utf-8")))
            result = curs.next() 
    else:
        print("No result was found")
        return ()            
    return middleSet

print(yearSearch(2018))
curs.close()
database.close()
