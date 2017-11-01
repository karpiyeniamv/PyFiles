import math

def prime(n):
    if (math.factorial(n-1) + 1) % n != 0:
        #print("Это составное число")
        return 0
    else:
        #print("Это простое число")
        return 1

def is_palindrome(word):
   for i in range(len(word)//2):
         if word[i] != word[-1-i]:
                 return False
   return True


#print (str(10000*10000)+"-"+str (99999*99999))

def func (a):
    flag=False
    tempMin=0
    tempMax=0
    b=tempMax
    while (flag==False & b>=tempMin):




mn1=1
mn2=1
a=9999799999
while (a>9000000008):
    if (is_palindrome(str(a))==True):


        print(str(a))
    a=a-1



# a=9999799999
# while (a>9000000008):
#     if (is_palindrome(str(a))==True):
#         print(str(a))
#     a=a-1

# a=10000
# count=0
# while (a<99999):
#     if (prime(a)==1):
#         print(str(a))
#         count=count+1
#     a=a+1
# print (str(count))



# a=100000000
# count=0
# while (a<9999800001):
#     if (is_palindrome(str(a))==True):
#         print(a)
#         count=count+1
#     a=a+1
#
# print ("all count: "+str(count))


# a=99999
# flag=0
# max=1
# maxA=1
# maxB=1
# b=a
# while(a>9000):
#     if (prime(a)==1):
#         print(a)
#         while (b>9000):
#             if (prime(b)==1):
#                 temp=a*b
#                 if (temp>max):
#                     if (is_palindrome(str(temp))==True):
#                         print(temp)
#                         maxA=a
#                         maxB=b
#                         max=temp
#             b=b-1
#     a=a-1
#     b=a
#
# print (str(max)+"="+str(maxA)+"*"+str(maxB))





##проверка на простоту
