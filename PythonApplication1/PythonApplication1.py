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

def kurtosis(x):
    if (type(x) != list and type(x) != int and type(x) != tuple and type(x) != range and type(x) != float):
        print("input number you retard")
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

def ayaya():
    num_array = list()
    num = input("Enter how many elements you want:")
    print ('Enter numbers in array: ')
    for i in range(int(num)):
        n = input("num :")
        num_array.append(int(n))
    print ('ARRAY: '+ num_array)
append
ayaya()