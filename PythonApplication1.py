#strings
b =  " Admiraljoy Ayaya"
b[:5]
b[:-5]
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("Adm", "Sp"))
goof = """Suppose you are in your confidence food stall, trying to buy your confidence food. 
Then, when you finished your shopping, you ended up forgot to buy your confidence food instead. Imagine. o_o"""
print(goof.split("."))
bgoof = b +" "+ goof
bgoof
t = 123
c =  "kappa {}"
print(c.format(t))
c = "imagine having {} apples idling in your table when you can just make {} cup of juices out of those apples and sell each cup for {} dollars"
numapp = 12
numjuice = 6
pricejuice = 2.25
print(c.format(numapp, numjuice, pricejuice))
print(c.title())


#biggest number between 3
def pepega(x,y,z):
 if x >= y:
     if x >= z:
         n1 = x
 elif y >= z:
    n1 = y
 else:
    n1 = z
 print("the biggest number is " + str(n1))

pepega(-2,12,12)

#selection sort for biggest number
def pepehand():
    x_array = list()
    x = input("Enter how many number(s) you want to compare:")
    print('Enter numbers in array: ')
    for i in range(int(x)):
            x = input("num :")
            x_array.append(float(x))
    for j in range(len(x_array)):
            min_atm =  j
            for k in range(j+1,len(x_array)):
                if x_array[min_atm] > x_array[k]:
                    min_atm = k

            x_array[j], x_array[min_atm] = x_array[min_atm], x_array[j]
    print('BIGGEST NUMBER IS: '+ str(x_array[len(x_array)-1]))

pepehand()

#sort 3 numbers
def compare3(x,y,z):
 n2 = x+y+z
 if x >= y:
     if x >= z:
         n1 = x
     else:
         n1 = z
 elif y >= z:
    n1 = y
 else:
     n1 = z
 n2 = n2 - n1
 if x <= y:
     if x <= z:
         n3 = x
     else:
         n3 = z
 elif y <= z:
     n3 = y
 else:
     n3 = z
 n2 = n2 - n3
 print("the order of the number " + str(n1) + " "+ str(n2) + " "  + str(n3))

 #selection sort to compare list of numbers
import sys
def ayaya():
    x_array = list()
    x = input("Enter how many elements you want:")
    print('Enter numbers in array: ')
    for i in range(int(x)):
            x = input("num :")
            x_array.append(float(x))
    for j in range(len(x_array)):
            min_atm =  j
            for k in range(j+1,len(x_array)):
                if x_array[min_atm] > x_array[k]:
                    min_atm = k

            x_array[j], x_array[min_atm] = x_array[min_atm], x_array[j]
    print('SORTED ARRAY: '+ str(x_array))
    
   

ayaya()
     

compare3(12,12,12)
compare3(12,123,1234)
compare3(12,1234,123)
compare3(1234,12,123)
compare3(1234,123,12)
compare3(123,1234,12)
compare3(123,12,1234)

c = [1.2,2,3,4]
n = len(c)
s = sum(c)
mean = s/n
mean*c[0]
ss = 0
ss4 = 0
for i in range(n):
    ss = ss + c[i]**2
    diff4 = (c[i]-mean)**2
    ss4 = ss4 + diff4
var = ss/n - mean**2
kurto = ss4/(n*var**2)
print(kurto)

#calculate kurtosis
def kurtosis(x):
    if (type(x) != list and type(x) != int and type(x) != tuple and type(x) != range and type(x) != float):
        print("only number input")
        return
    elif (type(x) == int or type(x) == float):
        print("NaN")
        return
    else:
        n = len(x)
        s = sum(x)
        mean = s/n
        ss = 0
        ss4 = 0
        for i in range(len(x)):
            ss = ss + x[i]**2
            diff4 = (x[i]-mean)**4
            ss4 = ss4 + diff4
        var = ss/n - mean**2
        kurto = ss4/(n*var**2)
    print(kurto)
    
kurtosis((9,12))
kurtosis(9.3)
kurtosis(c)
b = "pepega"
kurtosis(b)

#Recursion
def recurs(k):
  if(k > 0):
    res = k + recurs(k - 1)**2 - recurs(k-2)
    print(res)
  else:
    res = 0
  return res

recurs(2)

#lambda
def mylamb(n):
  return lambda a : a * n 
tralala = mylamb(3)
tralala(111)

