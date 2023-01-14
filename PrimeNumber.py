class PrimeN:

    def __init__(self,value1):
        self.value1=value1
    def primenumber(variable):

        for i in range(2,variable+1):

            if variable % i == 0:
                print("Number is not Prime")
                i=i+1
                break
            else:
                print("number is prime")
                i=i+1
                break


PrimeN.primenumber(17)
