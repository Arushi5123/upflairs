#for i in range(10):
#print("welcome to you at our office in upfliairs",i)
#st ="upflairs"
#for char in st:
#   print(char)
#ls=[10,20,30,40,50,60,70,80,90]
#for item in ls:
 # if item >50:
  #  print(item)
#st={85,96,45,85,63,45,96,74}
#for item in st:
 #   print(item)
#dt={'A':10,'B':20,'C':30}
#for item in dt.items():
 #   print(item)
#dt={'A':10,'B':20,'C':30}
#for item in dt.values():
 #   print(item)
#ls=[52,41,63,96,85,75,48,96,93,12,5,45,74,96,85,3,22,1,23,4]
#count = 0
#odd=0
#for i in ls:
#    if i>50:
 #      if (i % 2 == 0):
  #      count=count+1
   #    else:
    #    odd=odd+1
#print(count)
#print(odd)
#i=0
#while(i<10):
 # print(i)        
  #i+=1
#for i in range(10):
 #   print(i)
 #   continue
#ls=[85,74,96,5,452,36,52,85,74,96,85,41,52,63,3,2,1,4]
#max=ls[0]
#for i in range(len(ls)):
   # if(ls[i]> max):
    #    max=ls[i]
#print(max)
#ls=[85,74,96,5,452,36,52,85,74,96,85,41,52,63,3,2,1,4]
#min=ls[0]
#for i in range(len(ls)):
#    if ls[i]<min:
 #       min=ls[i]
#print(min)
#ls=[1,1.2,"upflairs",True,]
#f=0
#inte=0
#bo=0
#st=0
#for i in range(len(ls)):
#   if type(ls[i])==float:
#       f+=1
#       print("number of float values:",f)
#for i in range(len(ls)):
#   if type(ls[i])==int:
#       inte+=1
#       print("number of integer values:",inte)
#for i in range(len(ls)):
#   if type(ls[i])==bool:
#       bo+=1
#       print("numberof boolean values:",bo)
#for i in range(len(ls)):
#   if type(ls[i])==str :
#       st+=1
#       print("number of strings:",st)
#n=int(input("Enter the number you want an factorial of: "))
#fact=1
#for i in range (1,n+1):
#  fact*=i
#print("The factorialof number",n,"is:",fact)  
#n=input('Enter the number of which you want to check for palindrome of:')
#if n== n[::-1]:
#         print("The number is a paliindrome number")
#else:
#         print("Thenumber is not a palindrome number")
#ls=[1,1.2,"upflairs",True,]
#f=0
#inte=0
#bo=0
#st=0
#for i in range(len(ls)):
#  if type(ls[i])==float:
#       f+=1
#  elif type(ls[i])==int:
#       inte+=1
#  elif type(ls[i])==bool:
#       bo+=1 
#  elif type(ls[i])==str :
#       st+=1
#print("number of float values:",f)
#print("number of integer values:",inte)
#print("numberof boolean values:",bo)
#print("number of strings:",st)
#n=int(input("Enter the number of which you want to check for armstrong number:"))
#m=n
#res=0
#while (m!=0) :
#     rem=m%10
#     res+=rem**3
#     m//=10
#if res==n:
#   print("The number is an armstrong number")
#else:
#   print("The number is not an armstrong number")
#ls=[]
#n=int(input("Enter the number odf elements in the list:"))
#for i in range(n):
#    ls.append(int(input("Enter the element:")))
#print(ls)
#import math
#x1,x2,y1,y2=map(int,input("Enter the coordinates by space:").split())
#distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
#print("The distance of the two points is",distance)

num= int(input("plz enter the value where you till there you want to print the series"))
num1=0
num2=1
count=1
next_number=num2
listf = [0,1,1]
print(0,1,end=" ")
while count<num:
   print(next_number,end=" ")
   count +=1
   num1,num2=num2,next_number
   next_number=num1+num2
   listf.append(next_number)#
print("/n")
evenElements=[]

evenSum=0
for i in listf:
  if(i%2==0):
    if(evenSum < 1000000):
       evenSum=evenSum+i
       print("Sum of even fib elements: ",evenSum)
    else:
       print("Invalid")
    evenElements.append(i)
    print("Even F elements: ", evenElements)      



#x= list(filter((lambda a:a%2==0),[1,2,3,4,5,6,7,8,9,10]))
#print(x)
# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
 
 
# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
 
# # using filter function
# filtered = filter(fun, sequence)
 
# print('The filtered letters are:')
# for s in filtered:
#     print(s)

    
    


    
    

    
    
