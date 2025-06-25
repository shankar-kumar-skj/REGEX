# #string
# #extract 

# #slicing operator
# #[start:end:step]

# state = "Rajasthan"
# print(state[0:3])
# print(state[2:])
# print(state[:4])
# print(state[1:9:2])
# print(state[4:0:-1])
# print(state[-1:-4]) 
# print(state[-5:-2:-1])

# #loop =>repeation

# #for loop
# total=0
# for i in range(1,6):
#     total=total+i
#     print(i,total)


# for i  in range (2,27):
#     if (i%2==0):
#         print("even no ",i)
#     else:
#         print("odd",i)


# for i in range(57,22,-1):
#     print(i)
    
    


# for i in range(57,22,-1):
#     if(i%6==0):
#         print("This number is divided by 6",i)
    

sum = 0
for i in range(57,22,-1):
    if(i%6==0):
        sum = sum+i
        print("This number is divided by 6 :- ",i)
        print("sum is :- ", sum)


n=int(input("Enter any number "))
for i in range(1,n+1):
    if (n%i==0):
        print("factor  => ",i)


n=int(input("Enter any number "))
count = 0
for i in range(1,n+1):
    if (n%i==0):
        
        print("factor  => ",i)
        count+=1
        print(count)
    if(count>2):
        print("Not prime",n)
    else:
        print("prime",n)


#for loop 
#break

for i in range(1,4):
    print("hii",i)
    break
    print("hii")


#cointue = statement ko skip karedaga
for i in range(1,11):
    if(i==5):
        continue
    print("hey", i)


y =1
while(y<15):
    print(y)
    y+=1


total=0
z=1
while(z<61):
    total+=z
    z+=1
print(total)

total=0
m = 97
while(m>57):
    if(m%2==0):
        print(m)
        total=total+m
    m=m-1
print(total)


num=334
a = num//10
print(a)

total=0
num=253
while(num>0):
    rem=num%10
    num=num//10
    print(rem,num)
    total+=rem
print(total)


total=0
temp =num
num=253
while(num>0):
    rem=num%10
    num=num//10
    print(rem,num)
    total+=rem**3
print(total)

if(total==temp):
    print("Armstrong number :- ", total)
else:
    print("Not armstrong number :- ", total)