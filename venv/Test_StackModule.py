import StackModule
def test_Stack():
    s1 =StackModule.Stack()
    s1.push(1)
    temp=s1.pop()
    assert temp==1
    s1.push(1)
    s1.push(2)
    s1.push(3)
    assert s1.pop()==3
    assert s1.pop() == 2
    assert s1.pop() == 1
