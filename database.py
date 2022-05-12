import sqlite3
from sqlite3 import *

# database initlization
class Database:

    # connection
    def DB_Connection(self):

        # connection
        self.conn = sqlite3.connect('UserCredentials.db')
        self.cur = self.conn.cursor()
    
    # table
    def TablesGeneration(self):             # Only run this function if it s the firsttime running the file in your system to Avoid overwriting your database 
        
        # creating the database
        self.cur.execute(""" CREATE TABLE UserDetails(
            fullName TEXT,
            emailAddress TEXT,
            password TEXT,
            verificationKey TEXT,
            paymentKey TEXT,
            paymentAddress TEXT
        )
        """)
    
    # inserting values to the dta abse
    def usersCredentials(self, full_name, email_address, Password, verification_key, payment_key, payment_address):

        # inserting to the database
        self.cur.execute("INSERT INTO UserDetails ( fullName, emailAddress, password, verificationKey, paymentKey, paymentAddress ) VALUES ({}, {}, {}, {}, {}, {})".format(full_name, email_address, Password, verification_key, payment_key, payment_address)) 

# connect to db
if __name__ == '__main__':
    DB = Database()
    DB.DB_Connection()
    DB.usersCredentials("ShadrackMeoli", "shadcodesgmail.com", "Shadcodes1711", "verificationkey", "paymentkey", "paymentaddress")