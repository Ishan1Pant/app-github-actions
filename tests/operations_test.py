from src.math_operations import add,sub 

def test_add():
    assert add(2,3)==5 
    assert add(-1,1)==0 
    assert add(5,6)==11

def test_sun():
    assert sub(5,2)==3
    assert sub(8,3)==5 
    assert sub(-5,3)==-8 
