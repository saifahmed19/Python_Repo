if __name__ == '__main__':
    x = int(input("Enter 1st Number: "))
    y = int(input("Enter 2st Number: "))
    z = int(input("Enter 3st Number: "))
    n = int(input("Enter 4st Number: "))
    
list_ijk = []
for i in range(x + 1):
    for j in range (y + 1):
        for k in range (z + 1):
            if i + j + k != n: 
                list_ijk.append([i,j,k])
print(list_ijk)
