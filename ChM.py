import math

k_var=3.3
n_var=-6
a=0.1*k_var
b=0.2*n_var
h=0.1
i=0
tow=0.028#
AA=a/(b*b+1) #
s=tow*AA/(h*h) #
matrix = [[0 for i in range(10)] for i in range(10)]
for i in range(0, 10):
    t = i * tow
    matrix[i][0] = math.exp(t * a)
for i in range (1,9):
    x=0.1*i
    matrix[0][i]=(-1)*math.exp((-1)*a*a*x)
for i in range(0, 10):
    t = i * tow
    matrix[i][9] = math.exp(t * (b-1))
for i in range(1, 10):
    for j in range (1,9):
        matrix[i][j] = (s*matrix[i-1][j-1]+(1-2*s)*matrix[i-1][j]+s*matrix[i-1][j+1])
i = 0
for row in matrix:
    for a in row:
        print('%i' % (i/10), end='')
        print ('%10f' %  a, end='')
        i += 1
    print()


