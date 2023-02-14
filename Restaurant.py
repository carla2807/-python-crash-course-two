
class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):

        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        print('The restaurant is {} {}'.format(self.restaurant,self.cuisine) )
    
    def open_restaurant(self):
        print('Restaurant is open')