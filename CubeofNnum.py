class Cube:
    def _cube(var):
        if var == 1:
            return 1
        else:
            i = 0
            while i <= var:
                a = a + (i * i * i)
                i = i + 1
        return a


value1 = int(input("Enter"))
Cube._cube(value1)
