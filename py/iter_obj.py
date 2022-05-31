class Testing:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __iter__ (self):
        return self
    def __next__(self):
        return self.next()
    def next(self):
        if self.a <= self.b:
            self.a += 1
            return self.a-1
        else:
            raise StopIteration

myObj = Testing(1,5)           
for i in myObj:
    print(i)