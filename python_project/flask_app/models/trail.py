from flask_app.config.mysqlconnection import connectToMySQL

class Trail:
        schema = "trails_schema"
        def __init__():
                self.id = data['id']
                self.name = data['name']
                self.description = data['description']
                self.lat = data['lat']
                self.lng = data['lng']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']


        #CREATE
        @classmethod
        def create(cls, data):
                query = "INSERT INTO trails (name, description, lat, lng, created_at, updated_at) VALUES (%(name)s, %(description)s, %(lat)s, %(lng)s, NOW(), NOW());"
                results = connectToMySQL(cls.schema).query_db(query, data)
                return results


        #READ ALL
        @classmethod
        def get_all(cls):
                query = "SELECT * FROM trails;"
                results = connectToMySQL(cls.schema).query_db(query)
                trails = []
                for info in results:
                        trails.append(info)
                return trails


        #READ ONE
        @classmethod
        def read_one(cls,data):
                query = "SELECT * FROM trails WHERE id = %(id)s;"
                results = connectToMySQL(cls.schema).query_db(query, data)
                if len(results) == 0:
                        return False
                #cls()
                return Trail(results[0])

# #UPDATE
# @classmethod
# def update(cls, data):
#         #data is a dictionary, holds post information
#         query = "UPDATE trails SET name = %(name)s, description = %(description)s, lat = %(lat)s, lng = %(lng)s, updated_at = NOW() WHERE id = %(id)s;" #make sure to include all keys
#         results = connectToMySQL(cls.schema).query_db(query, data) #returns id of updated dog
#         return results

# #DELETE
# @classmethod
# def delete(cls, data):
#         query = "DELETE FROM trails WHERE id = %(id)s;" 
#         connectToMySQL(cls.schema).query_db(query, data)