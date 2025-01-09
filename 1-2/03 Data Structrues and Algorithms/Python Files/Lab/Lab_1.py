len = int(input("Enter the length of the list: "))
olist = []
for i in range(len):
    x = int(input("Enter the element: "))
    olist.append(x)
print(olist)

fnum = int(input("Enter a number: "))
num = fnum
total = 1
while fnum > 0:
    total *= fnum
    fnum -= 1
print("Factorial of", num, "is", total)

fiblen = int(input("Enter the no.of terms: "))
num1, num2 = 1, 1
print(1, 1, end = " ")
while fiblen > 2:
    temp = num2
    num2 = num1
    num1 += temp
    print(num1, end = " ")
    fiblen -= 1
print("")

def dotprod(len, l1, l2):
    sum = 0
    for i in range(len):
        sum += l1[i] * l2[i]
    return sum

len = int(input("Enter the length of the list: "))
list1 = [] 
list2 = [] 
sum = 0
for i in range(len):
    list1.append(int(input("Enter elements of list 1: ")))
for i in range(len):
    list2.append(int(input("Enter elements of list 2: ")))
sum = dotprod(len, list1, list2)
print("The dot product is", sum)

def matrixPrint(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

n = int(input("Enter the no.of rows in Matrix 1: "))
m = int(input("Enter the no.of columns in Matrix 1/rows in Matrix 2: "))
k = int(input("Enter the no of columns in Matrix 2: "))
matrix1 = []
matrix2 = []
matrix2T = []
outmat = []
for i in range(n):
    nums = input("Enter the elements of each row of Matrix 1, separated by ' ' : ")
    matrix1.append(list(map(int, nums.split())))
for i in range(m):
    nums = input("Enter the elements of each row of Matrix 2, separated by ' ' : ")
    matrix2.append(list(map(int, nums.split())))
for i in range(k):
    trrow = []
    for j in range(m):
        trrow.append(matrix2[j][i])
    matrix2T.append(trrow)
for i in range(n):
    row = []
    for j in range(k):
        row.append(dotprod(m, matrix1[i], matrix2T[j]))
    outmat.append(row)
print("The product matrix is: ")
matrixPrint(outmat)