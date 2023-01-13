class Factorial:
    def factorialn(number):
        if number==0:
            return 0
        elif number==1:
            return 1
        else:
             return number * Factorial.factorialn(number-1)

for i in range(10):
    print(Factorial.factorialn(i))
