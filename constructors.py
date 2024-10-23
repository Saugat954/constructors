
class person:
    def __init__(self,name,occupation,city):
        print("Hey I am a person")
        self.name = name
        self.occupation = occupation

    def my_func(self):
        print(f"My name is {self.name} and I work as a {self.occupation}")

a=person("Saugat","Student","Brisbane")
b = person ("Bijaya", "Chef", "Sydney")
a.my_func()
b.my_func()