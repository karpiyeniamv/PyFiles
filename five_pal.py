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
    b=99999
    while ( flag==False and b>10000):
        if (prime(b)==1):
            print(str(b)+" "+str(a%b))
            if ((a%b)==0):
                c=a//b
                if ((prime(c))==1):
                    print(str(c)+" result  "+str(b))
                    return 1
            if (b<(a/b)):
                flag=True
                return 0
        b=b-1

mn1=1
mn2=1
a=9778888779
while (a>1000000000):
    if (is_palindrome(str(a))==True):
        print(str(a))
        if (func(a)==1):
            a=1
    a=a-1




