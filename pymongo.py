from pymongo import MongoClient 
import datetime as dt

class Suman:
    connection = MongoClient("mongodb://localhost:27017")

    # CHECK FOR MONGODB CONNECTIONS
    def mongo_connection(self):
        if self.mongo_connection:
            return True
        else:
            return False 
    
    # LIST OF ALL MongoDB Databases
    def ListAllDatabase(self):
        if self.mongo_connection()==True:
            return self.connection.list_database_names()
        else:
            print("ERROR : Connection does not exists")
    
    # CHECK WHETHER DATABASE EXISTS OR NOT
    def DatabaseExists(self, dbname):
        if dbname in self.ListAllDatabase():
            return True
        else:
            return False
    # CREATE A NEW COLLECTION
    def CreateCollection(self, dbname, collectionname):
        if self.connection:
            dbname = self.connection[dbname]
            new_collection = dbname[collectionname]
            return(new_collection)
        else:
            print("ERROR : Connection does not exists")
    
    # Create TimeStamp for your Data 
    def timestamp(self):
        return (dt.datetime.now())

    
    # INSERT DATA
    def Insert_Data(self, db_name, collection_name, name, location):
        if self.connection:
            data = {"name":name, "country_of_origin":location, "time_stamp":self.timestamp()} 
            self.connection[db_name][collection_name].insert_one(data)
            return data
        else:
            print("ERROR : Connection does not exists")

    # FETCH ALL DATA 
    def DisplayAll(self,db_name, collection_name):
        result = []
        if self.connection:
            for data in self.connection[db_name][collection_name].find():
                result.append(data)
                for dic in result:
                    for key, value in dic.items():
                        print(value)
        else:
            print("ERROR : Connection does not exists")



s=Suman()

print(s.DisplayAll('suman', 'food_food'))
