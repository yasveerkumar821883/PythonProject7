class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.total_marks=(mark1+mark2+mark3)/3
        print(f"Total Marks Of {name} is {self.total_marks}%")
s1=Student("YashVeer Singh",80,67,87)



