import socket as sk
s=sk.socket(sk.AF_INET, sk.SOCK_DGRAM) #network=internet,user datagram protocal
#ip_address=" 192.168.1.117"
ip_address="127.0.0.1"
port_no= 2525
address=(ip_address,port_no)
s.bind(address) #register
# while True:
#        data=s.recvfrom(100)#100 is character limit
#        message=data[0]
#        ip_address=data[1][0]
#        message=message.decode('ascii')
#        print(ip_address,message)
#        file_name = "ip_address.txt"
#        with open(file_name,'a+') as file:
#           file.write(str(message)+'\n') 
#           file.close()
with open("demo1.txt",'wb') as file:
   while True:
     a,addr=s.recvfrom(100)
     print(f"Recieved message from {addr}: {a}")
     if not a:
         break
     file.write(a) 
     file.close()
print("File transfer complete")
    