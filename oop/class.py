class BigObject:
    pass


onj1 = BigObject()


class PlayerCharacter:
    '''
     _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    '''
    memberShip = True

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self._last_name = ''

    def run(self):
        '''
        run _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        '''
        print('run')
        return 'done'

    @classmethod  # -> instantiate the whole class in a new variable
    def add_something(cls, num1: int, num2: int):
        '''
        add_something _summary_

        _extended_summary_

        Args:
            num1 (int): _description_
            num2 (int): _description_

        Returns:
            _type_: _description_
        '''
        return num1 + num2

    @classmethod  # -> instantiate the whole class in a new variable
    def add_age(cls, num1: int, num2: int):
        '''
        add_age _summary_

        _extended_summary_

        Args:
            num1 (int): _description_
            num2 (int): _description_

        Returns:
            _type_: _description_
        '''
        return cls('Instance', num1 + num2)

    @staticmethod
    def number_squared(times: int) -> int:
        '''
        number_squared _summary_

        _extended_summary_

        Args:
            times (int): _description_

        Returns:
            int: _description_
        '''
        return times * 2


player1 = PlayerCharacter('Edgar', 30)
print(player1.name, player1.age)

player1.run()
print(PlayerCharacter.add_something(2, 3))

player2 = PlayerCharacter.add_age(10, 20)
print(player2.name, player2.age)

PLAYER3 = PlayerCharacter.number_squared(10)
print(PLAYER3)
