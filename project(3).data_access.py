import sqlite3
from customers import Customers
con = sqlite3.connect('C:\sqlite\customers.db')
cursor = con.cursor()

class CustomersDataAcces:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_all_customers(self):
        customers = self.cursor.execute("SELECT * FROM CUSTOMERS");
        for row in customers:
            print(row)

    def delete_customer(self, id):
        self.cursor.execute(f'DELETE FROM CUSTOMERS WHERE id = {id}')

    def insert_customer(self, customers):
        string = f'INSERT INTO CUSTOMERS VALUES ({customers.id}, "{customers.fname}", "{customers.lname}", "{customers.adress}", "{customers.mobile}")'
        #self.cursor.execute(string)
        con.commit()

    def get_customer_by_id(self,id):
        a = self.cursor.execute("select * from customers where "+
                         f" {id} = id ")
        for row in a :
            return (row[0], row[1], row[2], row[3], row[4])


    def update_customer(self,id,customers):
        self.cursor.execute(f'UPDATE CUSTOMERS SET FNAME = "{customers.fname}" where id = {id} ')
        con.commit()
        print('update done')

    def __str__(self):
        return self.__dict__
    def __repr__(self):
        return self.__dict__

customers = Customers
c1 = customers (11,'dani','levi','herzeliya','054321')
c3 = customers (12,'yaron','feraro','natanya','05439086')
c2 = customers (13,'liav','michaeli','tikva','0545678')
c4 = customers (15,'yoav','mich','ramat-gan','05453295')

data_access = CustomersDataAcces(cursor)

#data_access.insert_customer(c4)
#con.commit()

#data_access.update_customer(1,c1)


#print(data_access.get_all_customers())

#print(data_access.get_specific_culumn())
#print(data_access.get_customer_by_id(13))

