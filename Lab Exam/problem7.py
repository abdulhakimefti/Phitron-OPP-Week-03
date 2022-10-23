class Subset:
    def __init__(self,setNums):
        self.setNums = setNums
    def findSubset(self):
        for i in pow(2,len(self.setNums)):
            

setNums = [4,5,6]
get_subset = Subset(setNums)

