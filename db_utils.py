import sqlite3

class DBUtils:
    def create_tables(self,connection):
        create_loc = 'create table IF NOT EXISTS location (loc_id INTEGER PRIMARY KEY, location TEXT, alias TEXT, address TEXT)'
        ret = connection.execute(create_loc)
        print ("Return: ".format(ret))
        if ret==None:
            insert_one = 'insert into location (loc_id,location,alias,address) values (1,"bangalore","bengaluru","Bangalore")'
            insert_two = 'insert into location (loc_id,location,alias,address) values (2,"hyderabad","hyderabad","Hyderabad")'
            connection.execute(insert_one)
            connection.execute(insert_two)
            connection.commit()
        return ret

    def list_data(self,connection,where):
        select_data='select * from location'
        if where:
            select_data = 'select * from location where location=\''+where+'\' or alias like \'%where%\''
        cursor = connection.execute(select_data)
        for row in cursor:
            print("id: ",row[0])
            print("location: ",row[1])
            print("alias: ",row[2])
            print("Address: ",row[3])