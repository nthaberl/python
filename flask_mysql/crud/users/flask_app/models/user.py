from flask_app.config.mysqlconnection import connectToMySQL

class User:
        def __init__(self,data):
                self.id = data['id']
                self.first_name = data['first_name']
                self.last_name = data['last_name']
                self.email = data['email']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']

        #READ ALL
        @classmethod
        def get_all(cls):
                query = "SELECT * FROM users;"
                results = connectToMySQL("users_schema").query_db(query) #queries db and saves results into var results
                #results is a list of dictionaries
                print("this is the data in our users dict: ", results)
                users = []
                for info in results:
                        users.append(User(info))
                        #users.append(cls(info))
                return users

        #CREATE
        @classmethod
        def create(cls, data): #data is a dictionary! holds post info
                query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
                results = connectToMySQL("users_schema").query_db(query, data) #results from an insert query gives us the id of the newly created user
                print("This is the data in the results var after inserting into DB: ", results)
                return results

        #READ ONE
        @classmethod
        def read_one(cls,data):
        #data still is dictionary, but only holds {"id": x}
                query = "SELECT * FROM users WHERE id = %(id)s;"
                #results is a list of dictionaries
                #list is either empty or has length of 1, a single dictionary
                results = connectToMySQL("users_schema").query_db(query, data)
                if len(results) == 0:
                        return False
                #cls()
                return User(results[0])

        #UPDATE
        @classmethod
        def update(cls, data):
                #data is a dictionary, holds post information
                query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;" #make sure to include all keys
                results = connectToMySQL("users_schema").query_db(query, data) #returns id of updated dog
                return results

        #DELETE
        @classmethod
        def delete(cls, data):
                query = "DELETE FROM users WHERE id = %(id)s;" 
                connectToMySQL("users_schema").query_db(query, data)