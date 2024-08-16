class User():
    '''
    User
    '''
    def __init__(self, name: str) -> None:
        self.name = name

class Wizard(User):
    '''
    Wizard

    Args:
        User (User)
    '''

    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self.power = power

user1 = Wizard('Edgar', 100)
print(user1.name, user1.power)
