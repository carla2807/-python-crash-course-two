class User():
    ##metodo constructor para inicializar atributos
    def __init__(self,first_name,last_name,age,location) :
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        print('User:{} {} {} {}'.format(self.first,self.last,self.age,self.location))
    
    def greet_user(self):
        print("Hello" + " "  + greet_user.first.title())

#instancias llamo a la clase User y le paso atributos
greet_user = User('Carla','Massat',32,'Rosario')
greet_user.greet_user()


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)

        self.privileges = []  

    
    def show_priviges(self):
        for privilege in self.privileges:

            print(f"{privilege.title()}")