#import the necessary Modules
#be sure to save this file in the save folder as the database file
import sqlite3

def connection():
    '''
    - create connection object
    - create a cursor
    '''
    conn = sqlite3.connect("studentsdb.db")#will create the db file in the folder if it does not exist and if it does it just connects.
    cur = conn.cursor()#create a cursor to execute sql statements
    return conn,cur

def InsertData1():
    '''
    - This method inserts data directly into query statement
    - make a connection
    - execute the query passing the values into the sql statement
    - commit the changes
    - close the connection
    '''
    
    
def InsertData2():
    '''
    - The method inserts data using userinput into query statement
    - Get userinput and store it in variables
    - Modify the query to have placeholders e.g. VALUES(?,?,?,?,?) where the ?
      represent the number of values that must be injected
    - execute the query e.g. ("INSERT INTO employees VALUES(?,?,?)",(fname,lname,epay))
    - comit changes and close the connection
    '''
    

def selectQueryMethod1():
    '''
    - This will query all available data with no criteria applied
    - connect to the database
    - execute the a select query for all available data in a table
      e.g. Select * FROM tablename
    - Use one of the following fetch technique
        cur.fetchone() - returns one
        cur.fetchmany(5) - returns number specified
        cur.fetchall() - returns all records matching the criteria
    - might be worth storing the fetched data into a variable
    - notice that data is returned as a 2d Arrary
    - close the connection'''
    
    
    
def selectQueryMethod2():
    '''
    - This will query data using placeholders for the search string:
    - Connect to the database
    - execute the query statement using the wildcard place holder in the criteria field
      e.g.("SELECT * FROM employees WHERE first=?",("David",))
      notice 2 values in the tuple even if one is being used i.e. ("David", )
    - You could then modify this by getting the data from a  user input
    - Use the fetch method and store results in a variable
    - close the connection'''
    
    
    
    
def delete_record():
    '''
    - This will delete a record from a database
    - Connect to the database
    - Execute a delete query statement
      e.g. DELETE FROM employees WHERE name = 'Charlie'
    - Commit the changes and close the database
    - Output confirmation of the deletion.
    '''
    