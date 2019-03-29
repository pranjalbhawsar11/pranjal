class rect:
    def __init__(self):
        self.length=9
        self.breath=120
    def cal(self,x):
        return  x.length*x.breath

a=rect()
b=rect()
print(b.cal(a))
