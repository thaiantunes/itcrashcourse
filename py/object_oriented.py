'''Intro to Object-oriented Programming

In object-oriented programming, concepts are modeled as classes and objects. An idea is defined using a class, 
and an instance of this class is called an object. Almost everything in Python is an object, including strings,
lists, dictionaries, and numbers. When we create a list in Python, we are creating an object which is an instance 
of the list class, which represents the concept of a list. Classes also have attributes and methods associated with
them. Attributes are the characteristics of the class, while methods are functions that are part of the class.

We can use the type() function to figure out what class a variable or value belongs to.

You can use the dir() function to print all the attributes and methods of an object. Each string is an instance
of the string class, having the same methods of the parent class. Since the content of the string is different, 
the methods will return different values. You can also use the help() function on an object, which will return 
the documentation for the corresponding class. This will show all the methods for the class, along with parameters 
the methods receive, types of return values, and a description of the methods.'''

#criando a classe
class Apple:
    pass #mantém a classe vazia

#criando classe com atributos
class Apple:
    color = "" #define o atributo cor
    flavor = "" #define o atributo sabor

#criando instancia da classe 
jonagold = Apple()
jonagold.color = "red"
print(jonagold.color)
print(jonagold.color.upper()) #posso usar um metodo em cima de um atributo

#criando um método para a classe
class Dog():
    years = 0 #criando um atributo standard que posso mudar depois
    def dog_years(self):
        return self.years * 7

tiri = Dog()
print(tiri.dog_years())

tiri.years = 2
print(tiri.dog_years())

#criando um metodo especial
class Person():
    def __init__(self, name, years):
        self.name = name
        self.years = years
    def __str__(self):
        return "My name is {} and I'm {} years old".format(self.name,self.years)

toie = Person("Toioio", 27)
print(toie)

class todolist():
    def __init__(self, weekday,tasks=[]):
        self.weekday = weekday
        self.tasks = tasks
    def add_task(self, newtask):
        '''Adds a new task to the task list''' #add a docstring to explain the code when help(function) is called
        return self.tasks.append(newtask)

monday = todolist("monday")
monday.add_task("clean dishes")
print(monday.tasks)

monday.add_task("empty trash can")
print(monday.tasks)

help(todolist)

#INHERITANCE
class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing): #cria uma "classe filha" que herda os atributos e os métodos da classe Clothing
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()