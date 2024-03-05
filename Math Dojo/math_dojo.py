class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self
md = MathDojo()
print("testing add")
print("result after adding 2:", md.add(2).result)
print("result after adding 2, 5, 1:", md.add(2, 5, 1).result)
print()
print("testing the subtract")
print("result after subtracting 3, 2:", md.subtract(3, 2).result)
print()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	

