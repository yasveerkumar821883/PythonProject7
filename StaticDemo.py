class StaticDemo:

    @staticmethod
    def fun():
        x=20
        y=30
        return x+y
    def fun1(self,x,y):
        return x+y

print(StaticDemo.fun())
print(StaticDemo.fun1(12,10,10))
