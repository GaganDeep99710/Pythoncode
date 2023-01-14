class Patterns:
    def patternpr(n):
        for i in range(n):#rows
            for j in range(i,n):#columns
                print("@",end=" ")

            for j in range(i+1):#columns
                print(" ",end="")
            print()
Patterns.patternpr(5)