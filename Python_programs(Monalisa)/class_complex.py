class Cmplx:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return self.a + other.a, self.b + other.b


c1=Cmplx(1,3)
c2=Cmplx(2,4)
print("complex number addition = ",c1 + c2)