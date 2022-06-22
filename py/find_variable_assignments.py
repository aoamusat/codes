import re
import builtins

def find_variable_assignments(source, target_var_names):
    list_bundlers = []
    for var in target_var_names:
    	if re.search('class '+var, source) or re.search('def '+var, source) or re.search('def.*\(.*'+var+'.*\)', source) or re.search('^[^"\']*'+var+'.*=.*[^"\']*$', source) or re.search(var+'.*=.*$', source):
    		list_bundlers.append(var)
    return list_bundlers
    
    
src1 = """
def fn():
    "str = 42"
    '''next=42'''
    'bin = dir = next = list'
    next == 42
    a, b = str, list
    print(str, a, b)
"""

src2 = """
class str: 
    def __init__(self, list): 
        def next(foo, iter=42, baz=1): bin = 2
"""

src3 = """
def fn():
    next = 42
    str = next
    a, b = tuple, list
"""

src4 = """
def fn(): 
    next,dir,list,dir = 1,2,3,"bin = 4"
str = 45
"""
targets = dir(builtins)
print(find_variable_assignments(src1, targets))
print(find_variable_assignments(src2, targets))
print(find_variable_assignments(src3, targets))
print(find_variable_assignments(src4, targets))
