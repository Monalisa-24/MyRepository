class Operator:
    def __init__(self,n):
        self.n=n
    def __add__(self,o):
        return self.n+o.n
    def __sub__(self,o):
        return self.n-o.n
    def __mul__(self,o):
        return self.n*o.n

#n=Operator(0)
n1=Operator(10)
n2=Operator(30)
print("add = ",n1+n2)
print("subtract = ",n1-n2)
print("multiply = ",n1*n2)
