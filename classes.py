
##
class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):

        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print('The restaurant is {} {}'.format(self.restaurant,self.cuisine) )
    
    def open_restaurant(self):
        print('Restaurant is open')
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self,additional_served):
        self.number_served += additional_served

        
#Creo instancia de la clase Restaurant, asigno valores a los atributos
restaurant = Restaurant('Food Times', 'Takeaway')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nNumber served:{restaurant.number_served}" )
restaurant.number_served = 400
print(f"\nNumber served:{restaurant.number_served}" )

restaurant.set_number_served(1257)
print(f"\nNumber served:{restaurant.number_served}" )

restaurant.increment_number_served(239)
print(f"\nNumber served:{restaurant.number_served}" )

##Herencia de clase restaurant
class IceCreamStand(Restaurant):

    #cuisine_type recibe por default el atributo ice cream para no tener que 
    #escribirlo en la instancia
    def __init__(self, restaurant_name, cuisine_type = 'icre-cream'):
       super().__init__(restaurant_name, cuisine_type)
       self.flavors = []
    
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor.title()}")


#Instancia
big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']


big_one.describe_restaurant()
big_one.show_flavors()





















