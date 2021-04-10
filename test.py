class Cube():
    def __init__(self, max):
        self.max =max
        self.power =0
    def __iter__(self):
        return self
    def __next__(self):

        if(self.power<=self.max):
            result = 3**self.power
            self.power +=1
            return result

        else:
            raise StopIteration
cube = Cube(5)
for i in cube:
    print(i)