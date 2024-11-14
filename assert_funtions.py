import re
import sys
import pytest


#Basic Assertions:
#assert expr: Checks if expr is true.
def test_basic():
    assert 2 * 1 == 2


#Equality Assertions:
#assert a == b: Checks if a is equal to b.
def test_equality():
    assert 'hello' == 'hello' 


def test_custom_message():
    assert 2 == 2, "Expected 1 to equal 2" 

def test_email():
    email="harikrishna@gmail.com"
    format="^[A-Za-z^@]+@[^@]+\.[^@]+$"
    assert re.match(format,email),"Invalid Email"    

#sys.path.insert(1,'/Users/girish/Vs_Python/assert2.py')
#import assert2
#import assert2
from assert2 import dependent  

def test_independent():
    print( "the answer is" ,dependent(23))
            