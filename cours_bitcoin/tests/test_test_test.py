'''from python_script import name_function

def test_name_function():
	sample_input
	expected_res
	assert name_function(sample_input) == expected_res'''
from cours_bitcoin.src.simple_add import add

def test_initialize():
	assert(True)
	
def test_add():
	a, b = 2, 5
	res = add(a,b)
	expected_res = 7
	assert (res == expected_res)