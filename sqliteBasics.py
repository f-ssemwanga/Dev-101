
import sqlite3 # necessary module for this purpose
class User():
    '''User data for objects created from this class will be written to the database'''
    def __init__(self,f_name,l_name,pay):
        self.fname =f_name
        self.lname = l_name
        self.pay =pay
        


'''
Basic concepts of Sqlite3 module
- scenario is to create a sample application for adding and removing employee details
'''
def connection():
    '''
    - create connection object
    - create a cursor
    '''
    conn = sqlite3.connect("employeedb.db")#will create the db file in the folder if it does not exist and if it does it just connects.
    cur = conn.cursor()#create a cursor to execute sql statements
    return conn,cur
    

def create_database():
    '''
    - run commands using the execute methods
    - create a table containing employees name, lastname and pay
    - when creating table specify data types, sqlite allows: NULL, INTEGER,REAL, TEXT and BLOB
    - commit and close connection
    '''
    
    conn,cur =connection()
    try:
        cur.execute("""CREATE TABLE employees(
                    first text,
                    last text,
                    pay real                   
                
                    )""")
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
         print('Table already exists') 
def add_data_method1():
    '''The method below works but it is vulnerable to sql inject attacks'''
    conn,cur = connection()
    #cur.execute("INSERT INTO employees VALUES('Charlie','Young',21000)")
    fname =input('Enter first name: ')
    lname =input('Enter last name: ')
    epay = float(input('Enter the pay: ' ))
    cur.execute("INSERT INTO employees VALUES('{}','{}',{})".format(fname,lname,epay))
    conn.commit()
    conn.close()
    print(f'{fname} {lname}\'srecord was saved!')
def add_data_method2():
    '''The method is better and uses ? place holders and a tuple for data'''
    conn,cur = connection()
    user1 =User('Elise','Ssemwanga',15.50)
    user2 =User('Dominic','Ssemwanga',19.50)
    #this method uses tuples
    cur.execute("INSERT INTO employees VALUES(?,?,?)",(user1.fname, user1.lname,user1.pay))
    conn.commit()
    print(f'{user1.fname} {user1.lname}\'srecord was saved!')
    #This method uses dictionary place holders and it is a preferred method
    cur.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{'first':user2.fname,'last':user2.lname,'pay':user2.pay})
    print(f'{user2.fname} {user2.lname}\'srecord was saved!')
    conn.commit()
    conn.close()
def add_data_method3():
    '''The method saves data from a class object into a database'''
    conn,cur = connection()
    #cur.execute("INSERT INTO employees VALUES('Charlie','Young',21000)")
    fname =input('Enter first name: ')
    lname =input('Enter last name: ')
    epay = float(input('Enter the pay: ' ))
    cur.execute("INSERT INTO employees VALUES(?,?,?)",(fname,lname,epay))
    conn.commit()
    conn.close()
    print(f'{fname} {lname}\'srecord was saved!')


def query_database_method1():
    '''Available methods:
    cur.fetchone() - returns one
    cur.fetchmany(5) - returns number specified
    cur.fetchall() - returns all records matching the criteria'''
    conn,cur = connection()
    cur.execute("SELECT * FROM employees")
    print(cur.fetchall())
    conn.close()
    
def query_database_method2():
    '''Using placeholders for the search string:'''
    conn,cur = connection()
    #using ? place holder in the query criteria
    cur.execute("SELECT * FROM employees WHERE first=?",("David",)) # notice 2 values in the tuple even if one is being used
    print(cur.fetchall())
    #using the dictionary place holder in the query criteria
    cur.execute("SELECT * FROM employees WHERE last=:last",{'last':'Ssemwanga'}) # notice 2 values in the tuple even if one is being used
    print(cur.fetchall())
    
    conn.close()
def delete_record():
    '''delete a record from a database'''
    conn, cur = connection()
    cur.execute("DELETE FROM employees WHERE first='Charlie'")
    conn.commit()
    conn.close()


