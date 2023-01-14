# sum = 0
# var = [1,2,4,5]
# for i in var:
#     sum=sum+i
# print(sum)

var = [34,43,66,33,55,66,88,22,33,44,22,2,212212,21214,214,1412414,1421,4214]

for i in range(0,len(var)-1):
    for j in range(i+1,len(var)):
        if (var[i]<var[j]):
            var[i],var[j] = var[j],var[i]


print(var)

# max = var[0]
#
# for i in range(len(var)):
#     if (var[i]>max):
#         max=var[i]
#
# print(max)
#
