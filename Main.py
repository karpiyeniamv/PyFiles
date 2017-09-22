#task 4##########################
print ("Введите ширину таблицы ")
a= int ( input() )
a=1
a=(a-1)/2 #количество проходимых кругов
print ("a="+str(a))
result=1
i=1
j=0
temp=1
while (i<a+1):
    print("i=" + str(i))
    while (j<4):
        temp=temp+2*i
        j=j+1
        result=result+temp
        print("temp= "+ str(temp))
    j=0
    i = i + 1
print ("result= "+ str(result))

#task 2#############################
def func (a,q):
    b=[]
    b=list (str(a))
    c=[]
    index=0
    while (index<10):
        c.append(0)
        index=index+1
    for i in b:
        c[int(i)]=c[int(i)]+1
    a=a*q

    bb=[]
    bb=list (str(a))
    cc=[]
    index=0
    while (index<10):
        cc.append(0)
        index=index+1
    for j in bb:
        cc[int(j)]=cc[int(j)]+1
    if (c==cc):
        return 0
    else:
        return 1

flag=0
a=1
while (flag==0):

    if ((func (a,2)==0)&(func (a,6)==0)):
        print ("Искомое число = "+str (a))
        print(str(a) + "*" + str(2) + "=" + str(a*2))
        print(str(a) + "*" + str(6) + "=" + str(a * 6))

        flag=1
    a=a+1

#task3

#print ("Введите число a")
a=3
#print ("Введите число b")
b=3
#c=a**b
#print (str (a)+" в степени "+str(b)+" = "+str(c))
arr=[]
while (a<128):
    while (b<106):
        c=a**b
        print ("c="+str (c))
        if c not in arr :
            arr.append(c)
        b=b+1
    a=a+1
    b=3
print ("Всего уникальных элементов "+str (len (arr)))


#task1#########################################################################
def fun (r,q,t,v,u):
    firstNum=100*r+10*q+r
    secondNum=1000*r+100*t+10*v+u
    thirdNum=1000*r+100*u+10*v+v
    if (firstNum+secondNum==thirdNum):
        print (str(firstNum)+"+"+str(secondNum)+"="+str(thirdNum)+" ("+str(firstNum+secondNum)+")")
        return 1
    else:
        print(str(firstNum) + "+" + str(secondNum) + "!=" + str(thirdNum)+" ("+str(firstNum+secondNum)+")")
        return 0



arr=[]
index=0
while (index<10):
    arr.append(0)
    index=index+1
r=1
temp=0
h=0
while (r<10):

    index = 0
    while (index < 10):
        arr[index]=0
        index=index+1
    arr[r]=1
    index = 0
    q=0
    while (q<10):
         if (arr[q]==0):
             arr[q]=1
             t=0
             while (t<10):
                if (arr[t]==0):
                    arr[t]=1
                    v = 0
                    while (v<10):
                        if (arr[v]==0):
                            arr[v] = 1
                            u=0
                            while (u<10):
                                if (arr[u]==0):

                                    temp=temp+fun (r,q,t,v,u)
                                    h=h+1
                                    u = u + 1
                                else:
                                    u=u+1
                            arr[v]=0
                            v = v + 1
                        else:
                            v=v+1
                    arr[t]=0
                    t = t + 1
                else:

                    t=t+1
             arr[q] = 0
             q=q+1
         else:
             q=q+1
    r = r + 1
print(str (temp))
print(str (h))
print(str (81*8*7*6))




