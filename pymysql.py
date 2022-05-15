import pymysql


class Suman:
    db_name = 'guvi'
    user_name = 'root'
    password = 'suman'
    port = 3306
    host = 'localhost'
    conn = pymysql.connect(
            host=host, user=user_name, password=password, db=db_name)

    def db_version(self):
        conn = pymysql.connect(
            host=self.host, user=self.user_name, password=self.password, db=self.db_name)
        
        cur = conn.cursor()
        sql = 'SELECT @@version'
        data = cur.execute(sql)
        if(data):
            print(cur.fetchall())
        else:
            print("error")
    
    def db_connection(self):
        try:
            c = self.conn.cursor()
            print('SUCCESS : DB connection')
            self.conn.close()
        except pymysql.DatabaseError:
            print('ERROR : Error with DB connection')

    # CREATE TABLE INSIDE GUVI DB

    def create_table(self):
        try:
            c = self.conn.cursor()
            sql = """CREATE TABLE food_name(ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), country VARCHAR(20))"""
            c.execute(sql)
            print("SUCCESS : TABLE Created")
            self.conn.close()
        except pymysql.DatabaseError:
            print('ERROR : ERROR in Table creation')
    
    def insert_data(self):
        try:
            c = self.conn.cursor()
            sql = """INSERT INTO food_name(name, country) VALUES('Dal Bati Churma', 'Rajasthan') """
            c.execute(sql)
            self.conn.commit()
            print("SUCCESS :  Data Inserted Successfully")
            self.conn.close()
        except pymysql.DatabaseError:
            print('ERROR : Failed to INSERT data into Table')

    def display_all(self):
        try:
            c = self.conn.cursor()
            sql = """SELECT *  FROM food_name"""
            c.execute(sql)
            data = c.fetchall()
            for data in data:
                id = data[0]
                food_name = data[1]
                country = data[2]
                print(id, food_name, country)
        except pymysql.DatabaseError:
            print("ERROR :  Unable to Fetch data from the database")
        
s = Suman()
