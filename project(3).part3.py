from DataAcces import CustomersDataAcces,cursor,c1,c2,c3,c4,con
from customers import Customers
data_access = CustomersDataAcces(cursor)

def functions_input():
    a = int(input('enter number to select function:'))
    if a == 1 :
        data_access.get_all_customers()

    elif a == 2 :
         print(data_access.get_customer_by_id(11))

    elif a == 3 :
         data_access.insert_customer(Customers(20,'yosi','levi','givatayim','0543252'))
         con.commit()
         print(data_access.get_customer_by_id(20))


    elif a == 4:
        data_access.delete_customer(15)
        con.commit()

    elif a ==5 :
        data_access.update_customer(13,c1)
        con.commit()
        print(data_access.get_customer_by_id(13))


functions_input()
con.close()

