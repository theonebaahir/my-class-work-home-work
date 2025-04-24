r = 12 # bodmas
# precendence

e = 45
f = 67
i = 34
t = 23
b = 68
g = 98
print(r+e)
print(e*f)
z = (e+f) *e*r/g
print(z)

age = 11
name = "baahir"
if name == "baahir" and age == 11: 
    print("hello")
    
else: 
    print("goodbye")
    print("enter a number (numerater):")
    num = int(input())
 
    
    
    
    print("it is an even number")
    # corrected mean
mean = 38
wrong_number = 36
correct_number = 56
total_numbers = 40
sum = mean * total_numbers
print("the sum of total numbers  ",sum)
sum2 = sum - wrong_number+correct_number
print("corrected ", sum2)
mean2 = sum2 / total_numbers
print("corrected mean", mean2)
# average speed of cycleists
s1 = int(input("enter the speed of c1 "))
s2 = int(input("enter the speed of c2 "))
s3 = int(input("enter the speed of c3 "))
avg = s1+s2+s3/3

if s1 < avg:
    print("c1 is slower ", avg - s1)

if s2 < avg:
    print("c2 is slower ", avg - s2)
    
if s3 < avg:
    print("c3 is slower ", avg - s3)
    
    


