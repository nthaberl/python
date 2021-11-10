from flask import flash #enables flash messages

from flask_app.models import user

from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    schema = "recipes_schema"
    def __init__(self, data):
        self.id = data['id']
        self.user = user.User.get_by_id({"id": data['user_id']})
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #CREATE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instruction, under_30, date_made, created_at, updated_at) VALUES (%(user_id)s, %(name)s, %(description)s, %(instruction)s, %(under_30)s, %(date_made)s, NOW(), NOW());"
        #this returns the ID of newly created recipe
        return connectToMySQL(cls.schema).query_db(query, data)

    #READ MANY
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.schema).query_db(query)

        recipes = []
        for info in results:
            recipes.append(Recipe(info))

        return recipes


    #READ ONE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)

        if len(results) < 1: #not necessary but will prevent script from crashing if there are no results
            return False
        #references Recipe to create a recipe OBJECT
        return cls(results[0])


    #UPDATE
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, under_30 = %(under_30)s, date_made = %(date_made)s, updated_at = NOW() WHERE id = %(id)s;"
        #returns ID of newly UPDATED recipe
        return connectToMySQL(cls.schema).query_db(query, data)

    #DELETE
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL(cls.schema).query_db(query, data) #no need to return anything because we are just deleting values from table


    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data['name']) < 3:
            flash("Name of recipe must be at least 3 characters long!")
            is_valid = False

        if len(post_data["description"]) < 3:
            flash("Description must be at least 3 characters long!")
            is_valid = False
        
        if len(post_data["instruction"]) < 3:
            flash("Instructions must be at least 3 characters long!")
            is_valid = False

        if not post_data["date_made"]:
            flash("Please provide a date, best guess is fine")
            is_valid = False
        
        # if not post_data["under_30"]:
        #     flash("does it take less then 30 minutes to prepare??")
        #     is_valid = False

        return is_valid