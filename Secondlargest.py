class Second:
    def second(var):
        size = len(var)
        for i in range(0,size-1):
            for j in range(i+1,size):
                if var[i]>var[j]:
                    var[j],var[i]= var[i],var[j]
                else:
                    pass
            print(var)
        print(var[size-2])

lis=[2,3,4,2,1,2,4,2,1,4,5,6,7,8,6,6,5,9]
Second.second(lis)
