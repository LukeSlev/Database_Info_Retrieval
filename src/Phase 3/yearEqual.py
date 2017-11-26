from bsddb3 import db

<<<<<<< HEAD
def yearSearch(Starting_Year):
    Starting_Year=int(Starting_Year)-1
=======
def yearSearch(year):
>>>>>>> 0a844b256cad07faf31b6254283416e3444a280f
    DB_File = "ye.idx"
    database = db.DB()
    database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    Starting_Year = int(year)-1
    Ending_Year = int(year) + 1
      
    middleSet = set()
<<<<<<< HEAD

    #print(str(int(Starting_Year)))

    if int(Starting_Year) < int(curs.last()[0].decode("utf-8")):  # Proper Range
        result = curs.set_range(str(int(Starting_Year)+1).encode("utf-8"))
        if int(curs.next()[0].decode("utf-8"))>= int(Starting_Year+1):
             return middleSet
    else:
        result = None

=======
    #get the record that has the smallest key greater than or equal to the Starting Name:
    result = curs.set_range(str(Starting_Year).encode("utf-8")) 
   
>>>>>>> 0a844b256cad07faf31b6254283416e3444a280f
    if(result != None):
  
        while(result != None):
            #Checking the end condition: If the student's name comes after(or equal to) Ending_Name
            if(str(result[0].decode("utf-8")[0:len(str(Ending_Year))])>=str(Ending_Year)): 
                break
            
         #   print("Year: " + str(result[0].decode("utf-8")) + ", Rest: " + str(result[1].decode("utf-8")))
            middleSet.add(str(result[1].decode("utf-8")))
            result = curs.next() 
    else:
        print("No result was found")
        return ()
            
    return middleSet




def main():
    print(yearSearch(1977))


if __name__ == "__main__":
    main()
