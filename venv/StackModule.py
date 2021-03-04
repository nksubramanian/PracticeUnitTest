class Stack:
  c=[]


  def push(self,temp):
    self.c.append(temp)

  def pop(self):
    temp=self.c[len(self.c)-1]
    del self.c[len(self.c)-1]
    return temp
