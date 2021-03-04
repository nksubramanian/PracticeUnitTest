# Beginning Unit Testing

### Step 1

First step is to ensure pytest framework is available. If it is not available, you use pip install pytest

### Step 2

Below is a sample class Stack created. Stack is a data structure that implements Last in First out(LIFO) under the module "StackModule"

```python
class Stack:
  c=[]

  def push(self,temp):
    self.c.append(temp)

  def pop(self):
    temp=self.c[len(self.c)-1]
    del self.c[len(self.c)-1]
    return temp
 ```
 Below is the unit testing for LIFO property of Stack
 ```python
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
 ```
 
 In the above program, assert is used to make an assertion about the result. You get passed or failed for each of asserts if they're true or false respectively.
  
 Step 3: You could then run the above file using pytest test_StackModule.py either in the command prompt or in the console provided in the pyCharm editor. 
