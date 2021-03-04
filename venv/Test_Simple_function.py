import Simple_function

def test_addition():
    assert Simple_function.addition(3,4)==7
    assert Simple_function.addition(2,3)==5
    assert Simple_function.addition(3,1)==4


def test_reversing_string():
    assert Simple_function.reversing_string("Tom")=="moT"

