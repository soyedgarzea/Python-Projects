class User():
    def __init__(self, name: str):
        self.name = name

class Wizard(User):
    def __init__(self, name: str, power: int):
        super().__init__(name)
        self.power = power

user1 = Wizard('Edgar', 100)
print(user1.name, user1.power)
