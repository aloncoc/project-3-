import sqlite3
con = sqlite3.connect('C:\sqlite\customers.db')
cur = con.cursor()
class Customers:
    def __init__(self,id,fname,lname,adress,mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.adress = adress
        self.mobile = mobile
    def __str__(self):
        return f'id = {self.id} | name = {self.fname} | lname = {self.lname}' +\
    f' | adress = {self.adress} | mobile = {self.mobile}'
    def __repr__(self):
        return f'Customer ({self.id},{self.fname},{self.lname},{self.adress},{self.mobile})'

