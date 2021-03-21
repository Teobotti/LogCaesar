# LogCaesar
Challenge from 2019 Reply Cyber Security Challenge

Two files are given. One containing the encryption algorithm, the other containing the encrypted text.
In encrypt.py we can find how the digest is created:

new_pos = (3**(key+i)) % 257 

content[i] = (new_pos-1)^i^encrypted[new_pos-1]

In the first line new_pos is calculated using a key. Finding out this key would put us in front a complex discrete logarithm problem to solve.
The second line gives us the solution as any ciphertext element is the result of a three-way XOR between content[i], i and new_pos-1.

In decrypt.py the solution I propose is to try a brute force attack using several keys (approximately 1000) and calculate new_pos as made in encrypt.py.
for key in range(1,1000):

new_pos = (3**(key+i)) % 257

Once found new_pos we can obtain every element of the original text as the result of a three-way XOR between new_pos-1,i and encrypted[new_pos-1].

content[i] = (new_pos-1)^i^encrypted[new_pos-1]

Eventually we have to decode the result and check if "{FLG:" is present in the string, as the flag we are looking for starts with this substring.

flag = codecs.decode(result, errors='ignore')
if "{FLG:" in flag: print(flag)

In the output we can easily find "{FLG:but_1_th0ught_Dlog_wa5_h4rd}" which is the correct answer to the challenge.
