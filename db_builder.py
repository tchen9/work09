import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#adds values from courses
c.execute("drop table courses")
c.execute("drop table peeps")

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);") #course table
with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('INSERT INTO courses VALUES("' + str(row['code']) + '", ' + str(row['mark']) + ", " + str(row['id']) + ');')

#added values from peeps
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")
with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('INSERT INTO peeps VALUES("' + str(row['name']) + '", ' + str(row['age']) + ", " + str(row['id']) + ');')

                  
#print (c.execute("SELECT * FROM courses"))  #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database
