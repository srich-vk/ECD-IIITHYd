def dotprod(len, l1, l2):
    sum = 0
    for i in range(len):
        sum += l1[i] * l2[i]
    return sum

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