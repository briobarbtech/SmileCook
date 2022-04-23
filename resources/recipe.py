import json
from flask import jsonify, request
from flask_restful import Resource
from http import HTTPStatus as http
from models.recipe import Recipe, recipe_list       ### Importamos desde la carpeta models la clase recipe, y la lista de recetas 

class RecipeListResource(Resource):
    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {'data': data}, http.OK

    def post(self):
        data = request.get_json()
        recipe = Recipe(
            name=data['name'],
            description=data['description'],
            num_of_servings=data['num_of_servings'],
            cook_time=data['cook_time'],
            directions=data['directions']
        )
        recipe_list.append(recipe)

        return recipe.data, http.CREATED

class RecipeResource(Resource):

    def get(self, recipe_id):
        
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id and recipe.is_publish == True), None)

        if recipe is None:
            return {'message': 'recipe not found'}, http.NOT_FOUND

        return recipe.data, http.OK

    def put(self, recipe_id):
        data = request.get_json()

        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, http.NOT_FOUND

        recipe.name = data['name']
        recipe.description = data['description']
        recipe.num_of_servings = data['num_of_servings']
        recipe.cook_time = data['cook_time']
        recipe.directions = data['directions']

        return recipe.data, http.OK

    def delete(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        if recipe is None:
            return {'message':'recipe NOT FOUND'}, http.NOT_FOUND
        recipe_list.remove(recipe)
        return '', http.NO_CONTENT

class RecipePublishResource(Resource):
    def put(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, http.NOT_FOUND
        recipe.is_publish = True

        return {}, http.NO_CONTENT
    def delete(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        if recipe is None:
            return {'message': 'recipe not found'}, http.NOT_FOUND
        recipe.is_publish = False
        return {}, http.NO_CONTENT