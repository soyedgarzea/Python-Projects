'''
    _summary_

_extended_summary_
'''


class User:
    '''
    _summary_

    _extended_summary_
    '''

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('1', 'edgar')
user_2 = User('2', 'arturo')

user_1.follow(user_2)
