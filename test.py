import os
from functools import reduce

lista = [1,2,3,'hey']
print(reduce(lambda x,y: x*y if type(y) == int else x, lista))