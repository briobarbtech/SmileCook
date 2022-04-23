GET    | get all recipes         | RecipeListResource.get       | http://localhost:5000/recipes
POST   | create a recipe         | RecipeListResource.post      | http://localhost:5000/recipes
GET    | get a recipe            | RecipeResource.get           | http://localhost:5000/recipes/1
PUT    | update a recipe         | RecipeResource.put           | http://localhost:5000/recipes/1
DELETE | delete a recipe         | RecipeResource.delete        | http://localhost:5000/recipes/1
PUT    | set recipe as published | RecipePublishResource.put    | http://localhost:5000/recipes/1/publish
DELETE | sets recipe as draft    | RecipePublishResource.delete | http://localhost:5000/recipes/1/publish


-i se usa para indicar que queremos ver el encabezado de respuesta
-X (GET;PUT;POST;DELETE) significa que estamos enviando la petición usando el método GET de HTTP
-H lo usamos para especificar el header en la petición del cliente
-d lo usamos para el dato del POST HTTP, significa que la receta está en formato JSON


### POST ###
curl -i -X POST localhost:5000/recipes -H "Content-Type: application/json" -d '{"name":"Cheese Pizza","description":"This is a lovely cheese pizza", "num_of_servings":2,"cook_time":30,"directions":"This is how you make it"}'

curl -i -X POST localhost:5000/recipes -H "Content-Type: application/json" -d '{"name":"Tomato Pasta", "description":"This is a lovely tomato pasta recipe", "num_of_servings":3, "cook_time":20, "directions":"This is how you make it"}'

### GET ###

curl -i -X GET localhost:5000/recipes/1

### GET ALL ###

curl -i -X GET localhost:5000/recipes

### PUT ###

curl -i -X PUT localhost:5000/recipes/1/publish

curl -i -X PUT localhost:5000/recipes/1 -H "Content-Type: application/json" -d '{"name":"Lovely Cheese Pizza", "description":"This is a lovely cheese pizza recipe", "num_of_servings":3, "cook_time":60, "directions":"This is how you make it"}'

### DELETE ###

curl -i -X DELETE localhost:5000/recipes/1/publish