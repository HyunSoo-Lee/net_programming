#20201514 이현수
class MyComplex:
    def __init__(self, complex_1, complex_2):
        if complex_1[0] == '-':
            self.real_1 = complex_1[:2]
            self.imaginary_1 = int(complex_1[-3:-1])
        else:
            self.real_1 = int(complex_1[:1])
            self.imaginary_1 = int(complex_1[-3:-1])
        
        if complex_2[0] == '-':
            self.real_2 = int(complex_2[:2])
            self.imaginary_2 = int(complex_2[-3:-1])
        else:
            self.real_2 = int(complex_2[:1])
            self.imaginary_2 = int(complex_2[-3:-1])

    def PlusCalculator(self):
        a = self.real_1
        b = self.real_2
        c = self.imaginary_1
        d = self.imaginary_2
        if c+d < 0:
            result = f'{a+b}{c+d}i'
        else :
            result = f'{a+b}+{c+d}i'
        return  result

    def MinusCalculator(self):
        a = self.real_1
        b = self.real_2
        c = self.imaginary_1
        d = self.imaginary_2
        if c-d < 0:
            result = f'{a-b}{c-d}i'
        else :
            result = f'{a-b}+{c-d}i'
        return  result


complex = MyComplex('2-3i', '-5+4i')
#print(complex.real_1, complex.real_2,complex.imaginary_1, complex.imaginary_2)
print(complex.PlusCalculator())
print(complex.MinusCalculator())