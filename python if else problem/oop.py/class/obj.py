

class Person:
    name = "arman"
    occupation = "ML"
    netWorth = 100

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
print(a.name)     # prints: arman
a.info()          # prints: arman is a ML
a.name="new arman"
a.occupation="new ML"
a.info()

