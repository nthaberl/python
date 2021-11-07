from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #CREATE
        @classmethod
        def create(cls, data):
            query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
            #id of newly created ninja
            return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        # #DELETE
        # @classmethod
        # def delete(cls, data):
        #         query = "DELETE FROM ninjas WHERE id = %(id)s;" 
        #         connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

# ##########################################
# #READ ALL
#         @classmethod
#         def get_all_ninjas(cls):
#                 query = "SELECT * FROM ninjas;"
#                 results = connectToMySQL("dojos_and_ninjas_schema").query_db(query) #queries db and saves results into var results
#                 ninjas = []
#                 for info in results:
#                         ninjas.append(Ninja(info))
#                         #users.append(cls(info))
#                 return ninjas

#         #READ ONE
#         @classmethod
#         def read_one_ninja(cls,data):
#         #data still is dictionary, but only holds {"id": x}
#                 query = "SELECT * FROM ninjas WHERE ninja.id = %(id)s;"
#                 results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
#                 if len(results) == 0:
#                         return False
#                 #cls()
#                 return Ninja(results[0])

#         #UPDATE
#         @classmethod
#         def update_ninja(cls, data):
#                 #data is a dictionary, holds post information
#                 query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s;" #make sure to include all keys
#                 results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data) #returns id of updated dog
#                 return results