class Distance :
    def __init__(self,x1,y1,x2,y2):
        self.x1= x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def distanceMessure(self):
        totalSq = pow((self.x2-self.x1),2)+pow((self.y2-self.y1),2)
        return pow(totalSq,.5)
    
earthToMoon = Distance(2,3,-5,-3)
print(earthToMoon.distanceMessure())


