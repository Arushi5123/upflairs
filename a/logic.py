#for getting the input of the list
def get_data():
  n=int(input("Enter the number of elements of the list:"))
  ls=[]
  for i in range(n):
    ls.append(int(input("enter the elements:")))
  return ls    
#for finding th minimum
def mini(ls):
  min=ls[0]
  for i in range(len(ls)):
    if ls[i]<min:
       min=ls[i]
  return min
#for finding the maximum
def maxi(ls):
  max=ls[0]
  for i in range(len(ls)):
    if ls[i]>max:
       max=ls[i]
  return max
#for sorting the list
def sorti(ls):
  for i in range(len(ls)-1):
     min=ls[i]
     k=i
     for j in range(i+1,len(ls)):
       if ls[j]<min:
        min=ls[j]
        k=j
     temp=ls[i]
     ls[i]=ls[k]
     ls[k]=temp    
  return ls
