#інтроспекція
import random
help(random)
#pip install requests
def first_function():
    pass
class Human:
    pass
rq = random
first_f = first_function
nick = Human
print(random.__name__)
print(rq.__name__)
print(nick.__name__)
print(__name__)

info_lst = []#як дізнатися як працювати зі списками?
for method in dir(info_lst):
    print(method)
print(info_lst.__len__)

import inspect

print(inspect.ismethod(list))
print(inspect.isclass(Human))
print(inspect.isfunction(requests))