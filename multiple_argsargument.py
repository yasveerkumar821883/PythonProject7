class School:
    school_name = "ABC School"

    @classmethod
    def change_name(cls, new_name):
        cls.school_name = new_name
        print(cls.school_name)
c1=School
c1.change_name("hello ji")