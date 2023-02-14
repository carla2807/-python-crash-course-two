
from user import User
from user import Admin

#instancias llamo a la clase User y le paso atributos
user = User('Carla','Massat',32,'Rosario')
user.describe_user()

greet_user = User('Carla','Massat',32,'Rosario')
greet_user.greet_user()


#Instancia
car_adm = Admin('Carla', 'Massat', 32,'Rosario')
car_adm.describe_user()

car_adm.privileges = ['can add post', 'can delete post ', 'can ban user']
car_adm.show_priviges()
