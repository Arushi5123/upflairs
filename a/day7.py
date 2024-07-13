# r=int(input("enter the number of rows:"))
# c=int(input("enter the number of column:"))
# matrix=[]
# print("enter the elements rowwise:")
# for i in range(r):
#       a=[]
#       for j in range(c):
#           a.append(int(input()))
#       matrix.append(a)
# for i in range(r):
#     for j in range(c):
#         print(matrix[i][j],end=" ")
#     print()
# r1=int(input("enter ")=
# try:
#  name =input("plz enter your good name:")
#  age=int(input("enter your age:"))
#  print("i am ",name,"and i am",age,"year old")
# except:
#     print("error is occured but don't worry we will execute your remaining lines")
# else:
#     print("error is not occured")
# finally:
#     print("i will always")
# print("i am important pls execute me")
# try:
#  num1=int(input("enter number 1:"))
#  num2=int(input("enter number 2:"))
#  result=num1/num2
#  print(result)
# except ZeroDivisionError:
#     print("plz don't put 0 as denominator")
# except ValueError:
#     print("pls enter an integer")
try:
   ls=[1,2,3,4,5,6,7,8,9,10]
   target=int(input("enter your target:"))
   position=int(input("plz enter a position:"))
   for i in range(len(ls)):
       if ls[i]==target:
         print(i) 
       elif target not in ls:
         print("plz enter the elements inside the list")
         break
   for i in range(len(ls)):
       if i==position:
         print(ls[position])
       else:
         print(ls[position])
   print(ls[position])
except ValueError:  
      print("pls enter integer")
except IndexError:
      print("plz enter inside the index")
