import socket as sk
s=sk.socket(sk.AF_INET, sk.SOCK_DGRAM) #network=internet,user datagram protocal
#target_ip="192.168.1.65"
target_ip="127.0.0.1"
port_no=2525
target_address=(target_ip,port_no)#complete address
# quiet=True
# while quiet:
#      message=input("plz enter the message")
#      message.encode("ascii")
#      message_encrypt=message.encode("ascii")
#      s.sendto(message_encrypt,target_address)
    
#      user_input=input('do you want to exit it press Y/y')
#      if user_input=="Y" or user_input=="y":
#          quiet=False
    
    
file_name="demo1.txt"
with open(file_name,'rb') as file:
  while True:
    a=file.read()
    if not a:
        break
    s.sendto(a,(target_ip,port_no))
    print(f"send data:{a}")
print("file transfer complete")
#with open("ip_address.txt",'r') as file:
 #    file.read()