'''
end goal:
    * make sure the pc randomly pics a cat.
    * make sure sure program accepts your input
    * compare a take the wining value.

---Algorithm---
*Takes the input of the user about number of rounds - done
*define values of interest - done
*take user input - done
*pc randomly pics a value -done
*compare two values pick the wining value.
'''

import random


def items():
    # items = ('rock','papper','scissors')
    items = {1: 'rock', 2: 'papper', 3: 'scissors'}
    return items


def users_choice():
    user_input = int(input('\n Input Your Choice : '))
    s_choice = items()[user_input]
    return str(s_choice)


def pc_choice():
    vals = items().values()
    choice = random.choice(list(vals))
    return str(choice)


def decision(user, pc):
    if user == pc:
        print('Draw')

    else:
        print(
            f"User chose : {user} \n PC chose : {pc} \n Winner! : {'User' if user_beats(user,pc) else 'PC'}")


def user_beats(user, pc):
    rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    return rules[user] == pc


if __name__ == '__main__':
    num_rounds = int(input('Enter number of rounds : '))
    print(''' Welcome to Rock Papper Scissors
         1. Rock
         2. Papper
         3. Scissors
          ''')

    pc = 0
    user = 0
    for _ in range(num_rounds):
        user = users_choice()
        pc = pc_choice()
        print(user)
        print(pc)
        # decision(user,pc)


# class Cake:
#     def __init__(self, employee_name):
#         self.name = employee_name
#         self.owner_name  = 'George'
#     def __repr__(self):
#         return f"Cake('{self.name}')"

#     def __str__(self):
#         return f'{self.name} opened the fridge'

#     def note(self):
#         if self.name == self.owner_name:
#             return f'Enjoy your cake {self.name}'
#         else:
#             return f'{self.name}, I see you , dont eat my cake'

# a = Cake('Jay')
# print(repr(a))
# print(str(a))
# print(a.note())
