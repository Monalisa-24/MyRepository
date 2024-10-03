class TeamMember():
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def name1(self):
        print("teammember class.")
class Worker(TeamMember):
    def __init__(self,pay,jobtitle,name,uid):
        super().__init__(name,uid)
        self.pay=pay
        self.jobtitle=jobtitle
    def name2(self):
        print("worker class.")
class TeamLeader(Worker):
    def __init__(self,ex,pay,jobtitle,name,uid):
        super().__init__(pay,jobtitle,name,uid)
        self.ex=ex
    def name3(self):
        print("teamleader class.")

tl=TeamLeader(5, 25000, "Project Engineer", "Monalisa",1001)
print(tl.ex)
print(tl.pay)
print(tl.jobtitle)
print(tl.name)
print(tl.uid)
tl.name2()