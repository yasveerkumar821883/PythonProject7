class Team:
    def __init__(self):
        self.__size = 11
    def fun(self):
        print(self.__size)

class TechTeam(Team):
    def update_size(self, new_size):
        self._Team__size = new_size
        print(f"this overwrite value {self._Team__size}")

team = TechTeam()
team.fun()
team.update_size(15)
team.fun()
