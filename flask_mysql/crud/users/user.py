from mysqlconnection import connectToMySQL

class User:
        def __init__(self,data):
                self.id = data['id']
                self.first_name = data['first_name']
                self.last_name = data['last_name']
                self.email = data['email']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']


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

        @classmethod
        def create(cls, data): #data is a dictionary! holds post info
                query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
                results = connectToMySQL("users_schema").query_db(query, data)
                print("This is the data in the results var after inserting into DB: ", results)
                return results