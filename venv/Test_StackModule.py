import StackModule
def test_Stack():
    s1 =StackModule.Stack()
    s1.push(1)
    temp=s1.pop()
    assert temp==1
