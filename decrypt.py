
import codecs

with open("encrypted.txt", 'rb') as f:
    encrypted = f.read()

def decrypt(key, encrypted):
    content = list(' ' * 256)   
    for i in range(0,256):
        new_pos = (3**(key+i)) % 257
        content[i] = (new_pos-1)^i^encrypted[new_pos-1]
    return bytes(content)  


for key in range(1,1000): #trying 1000 different keys
        result = decrypt(key, encrypted)
        flag = codecs.decode(result, errors='ignore')
        if "{FLG:" in flag: 
	         print(flag)
        
