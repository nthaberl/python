from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
        def __init__(self, data):
                self.id = data['id']
                self.name = data['name']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']
                self.ninjas = []

        #READ ALL
        @classmethod
        def get_all(cls):
                query = "SELECT * FROM dojos;"
                results = connectToMySQL("dojos_and_ninjas_schema").query_db(query) #queries db and saves results into var results
                dojos = []
                for info in results:
                        dojos.append(Dojo(info))
                        #users.append(cls(info))
                return dojos

        #CREATE
        @classmethod
        def create(cls, data):
                query = "INSERT INTO dojos(name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
                results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data) #results from an insert query gives us the id of the newly created user
                print("This is the data in the results var after inserting into DB: ", results)
                return results

        #READ ONE
        @classmethod
        def read_one(cls,data):
        #data still is dictionary, but only holds {"id": x}
                query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
                results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
                if len(results) == 0:
                        return False

                dojo = Dojo(results[0])

                if (results[0])["ninjas.id"] != None:
                        for info in results:
                                ninjaData = {
                                        **info,
                                        "id": info["ninjas.id"],
                                        "dojo_id": info['dojo_id'],
                                        "first_name": info['first_name'],
                                        "last_name": info['last_name'],
                                        "age": info['age'],
                                        "created_at": info["ninjas.created_at"],
                                        "updated_at": info["ninjas.updated_at"]
                                }
                                dojo.ninjas.append(Ninja(ninjaData))
                #cls()
                return dojo

        #UPDATE
        @classmethod
        def update(cls, data):
                #data is a dictionary, holds post information
                query = "UPDATE dojos SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;" #make sure to include all keys
                results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data) #returns id of updated dog
                return results

        #DELETE
        @classmethod
        def delete(cls, data):
                query = "DELETE FROM dojos WHERE id = %(id)s;" 
                connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)