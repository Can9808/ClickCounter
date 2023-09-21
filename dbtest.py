# loading in modules
import sqlite3

# creating file path
dbfile = "D:\Workspace\Python\ClickCounter\\test.db"
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

#Creating table as per requirement
sql ="CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT)"
cur.execute(sql)
print("Table created successfully........")

# Commit your changes in the database
con.commit()

# reading all table names
table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# here is you table list
print(table_list)

# Be sure to close the connection
con.close()