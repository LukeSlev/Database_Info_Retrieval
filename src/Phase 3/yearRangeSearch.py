from bsddb3 import db

DB_File = input('What is the name of the file that includes your indexed year file? ')
#DB_File = "ye.idx"
database = db.DB()
database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
curs = database.cursor()

while(True):
    
    Starting_Year = input("Enter the Starting_Year: ")
    Ending_Year = input("Enter the Ending_Year: ")
    
    #get the record that has the smallest key greater than or equal to the Starting Name:
    result = curs.set_range(Starting_Year.encode("utf-8")) 
   
    if(result != None):
        print("Found List")
    
        while(result != None):
            #Checking the end condition: If the student's name comes after(or equal to) Ending_Name
            if(str(result[0].decode("utf-8")[0:len(Ending_Year)])>=Ending_Year): 
                break
            
            print("Year: " + str(result[0].decode("utf-8")) + ", Rest: " + str(result[1].decode("utf-8")))
            result = curs.next() y
    else:
        print("No result was found")
            
    NewSearch = input("Do you want to start a new search?(press y for yes) ")
    if(NewSearch != "y"): #Termination Condition
        break

curs.close()
database.close()
