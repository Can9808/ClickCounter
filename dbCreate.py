# loading in modules
import sqlite3

# creating file path
dbfile = "D:\Workspace\Python\ClickCounter\\database\\ClickCounter.db"
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()
'''
#Creating table as per requirement
#sql ="CREATE TABLE Mouse(FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT)"
#cur.execute(sql)
#print("Table Mouse created successfully........")

# Commit your changes in the database
#con.commit()
Maus
- ID(PK)
- Name
- Beschreibung
- Hersteller
- Teilenr
- kaufdatum
- Links klick summe
- mittelklick Summe
- rechts klick summe
- Sessions insgesamt = letzte Session_ID
- 
Session
- session_ID(PK)
- maus_ID(FK)
- Datum
- sesion start(timestamp) 
- session end(timestamp)
- links klicks
- rechts klicks
- 


test = ("Can", "B", 20, "S", 2.200)
sqlinsert ="INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (?,?,?,?,?)"
cur.execute(sqlinsert, test)
con.commit()
print("klappt")
'''
# reading all table names
table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# here is you table list
print(table_list)

# Be sure to close the connection
con.close()