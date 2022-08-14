class power:
    def pow():
        x = int(input("Enter any number:"))
        n = int(input("Enter power:"))
        if (n == 0): return 1
        elif (int(n % 2) == 0):
            return (pow(x, int(n / 2)) * pow(x, int(n / 2)))
        else:
         return (x * pow(x, int(n / 2)) * pow(x, int(n / 2)))
 
print(power.pow())


