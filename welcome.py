from validate_age import *
from get_name import *

print('='*35)
print('Welcome to voting eligibility check')
print('='*35)
print('\n')

user_name = get_name()
print(f'Hello {user_name}!\n')

age = int(input("Enter your age: "))
validate_age(age)

