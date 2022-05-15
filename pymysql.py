import pymysql


class Suman:
    db_name = 'guvi'
    user_name = 'root'
    password = 'suman'
    port = 3306
    host = 'localhost'

    def db_connection(self):
        conn = pymysql.connect(
            host=self.host, user=self.user_name, password=self.password, db=self.db_name)
        
        cur = conn.cursor()
        sql = 'SELECT @@version'
        data = cur.execute(sql)
        if(data):
            print(cur.fetchall())
        else:
            print("error")
        

s = Suman()

s.db_connection()
