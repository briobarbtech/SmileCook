recipe_list = []                        ### Creamos una lista para almacenar las recetas ###
def get_last_id():                      ### Definimos una función que nos devuelva el id del ultimo elemento guardado en la lista recipes
    if recipe_list: 
        last_recipe = recipe_list[-1]
    else:
        return 1                        ### o sino nos devuelve el id 1 para indicar que en realidad es el primer elemento
    return last_recipe.id + 1           ### toma el ultima id y le suma 1

class Recipe():                                                                     ### Creamos una clase llamada Receta
    def __init__(self, name, description, num_of_servings, cook_time, directions):  ### con los atributos nombre, descripción, cantidad de porciones, tiempo de cocción y instrucciónes
        self.id = get_last_id()
        self.name = name
        self.description = description
        self.num_of_servings = num_of_servings
        self.cook_time = cook_time
        self.directions = directions
        self.is_publish = False                                                     ### Seteamos por defecto el valor de publicado como Falso
    @property
    def data(self):                                                                 ### Modificamos el método por defecto de la clase para que devuelva un diccionario con los valores propios de la clase
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'num_of_servings': self.num_of_servings,
            'cook_time': self.cook_time,
            'directions': self.directions
        }