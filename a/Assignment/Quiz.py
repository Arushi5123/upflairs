import os 
import shutil as sh
for i in os.listdir(r'C:\Users\DeLL\Desktop\a\Assignment\Data'):
    if i.endswith(".txt"):
          sh.move(r'C:\Users\DeLL\Desktop\a\Assignment\Data'+'\\'+i,r'C:\Users\DeLL\Desktop\a\Assignment\txt'+'\\'+i)
    elif i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
          sh.move(r'C:\Users\DeLL\Desktop\a\Assignment\Data'+'\\'+i,r'C:\Users\DeLL\Desktop\a\Assignment\image'+'\\'+i)
    elif i.endswith(".pdf"):
          sh.move(r'C:\Users\DeLL\Desktop\a\Assignment\Data'+'\\'+i,r'C:\Users\DeLL\Desktop\a\Assignment\pdf'+'\\'+i)
    
        