class MyIterator:
    def __iter__(self):
        self.no = 0
        return self
    def __next__(self):
            self.no+=1
            return self.no

for x in MyIterator():
    print(x)