class Demo:
    school_name="ABC School"
    def __init__(self):
        self.name=None
    @staticmethod
    def num():
        print("hello Ji")
class Demo1(Demo):
    def num1(self,name):
        self.name=name
        print(name)
    @classmethod
    def clas1(cls,change_name1):
        cls.school_name=change_name1
        print(cls.school_name)
Demo.num()
d1=Demo1()
d1.num1("yash")
d1.clas1("AJM Public School ")
