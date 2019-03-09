class queue:
    def __init__(self):
        self.list = []
 
    def enqueue(self, data):
            self.list.append(data)
            print(self.list)
    def dequeue(self):
            return self.list.pop(0)
        
 
a = queue()
while 1:
    print('1] enqueue')
    print('2] dequeue')
    print('3] quit')
    do =int( input('enter number '))
 

    if do == 1:
        k=int(input("number of values to be inserted"))
        for i in range(0,k):
            val=int(input("enter the value to be inserted"))
            a.enqueue(val)
        
    elif do== 2:
        popped = a.dequeue()
        if popped is None:
            print('queue is empty.')
        else:
            print('Popped value: ', int(popped))
    elif do ==3:
        break
