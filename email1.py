import smtplib
sender_email="arushimathur14@gmail.com"
rec_email="smartengineer0786@gmail.com"
password=input(str("please enter your password:"))
subject="Yo from Arushi"
message="""Name:Arushi Mathur
College:Govt. Women Engineering College,Ajmer
Branch:CSE"""
text=f"Subject:{subject}\n\n{message}"
server=smtplib.SMTP('smtp.gmail.com',587)
status_code,response=server.ehlo()
print(f"[*] Echoingb the server:{status_code}{response}")
status_code,response=server.starttls()
print(f"[*]Starting TLS connection:{status_code}{response}")
status_code,response=server.login(sender_email,password)
print(f"logging in{status_code}{response}")
print('login success')
server.sendmail(sender_email,rec_email,text)
print("email has been sent to",rec_email)