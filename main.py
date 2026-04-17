# ISSUBSET
class MySet:
    def __init__(self):
        self.data = []

    def issubset(self, other):
        for item in self.data:
            if item not in other.data:
                return False
        return True

    def show(self):
        print(self.data)

s1 = MySet()
s1.data = [1, 2]

s2 = MySet()
s2.data = [1, 2, 3, 4]

print(s1.issubset(s2)) 
