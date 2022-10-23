class getPair:
    def __init__(self,nums):
        self.nums = nums
    def getPair(self,target):
        ln = len(self.nums)
        print(ln)
        for ln in range(ln-1):
            if self.nums[ln]+self.nums[ln+1]==target:
                print('Output: ', ln+1,ln+2)
numbers= [10,20,10,40,50,60,70]
target = 50
s = getPair(numbers)
s.getPair(target)