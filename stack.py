class Stack:
    def __init__(self):
        self.head = [1,2]
 
    def push(self, data):
            self.head.append(data)
            print(self.head)
    def pop(self):
            return self.head.pop()
        
 
a = Stack()
while 1:
    print('1] push')
    print('2] pop')
    print('3] quit')
    do =int( input('enter number '))
 

    if do == 1:
        k=int(input("number of values to be pushed"))
        for i in range(0,k):
            val=int(input("enter the value to be pushed"))
            a.push(val)
        
    elif do== 2:
        popped = a.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif do ==3:
        break
