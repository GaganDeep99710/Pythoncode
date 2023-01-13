class findingnumber:
    list1=["a","b""c","d"]
    def findingnum(value):
        list1 = ["a", "b""c", "d"]
        for i in range(len(list1)):
            if value in list1:
                print("the value present is",value)
                break
            else:
                print("no such value found")
                break

searchthis= input("input a character to search:")
findingnumber.findingnum(searchthis)

