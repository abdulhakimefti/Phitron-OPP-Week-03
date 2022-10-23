class simpleMath:
    def __init__(self,X,n):
        self.X = X
        self.n = n
    def sum(self):
        return self.X+self.n
    def pow(self):
        return pow(self.X,self.n)

print(simpleMath(2,3).pow(),
simpleMath(4,5).sum())