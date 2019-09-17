from Crypto.Cipher import DES
from Crypto import Random
import sys
import time
#cbc_key = b"\x01\x23\x45\x67\x89\xab\xcd\xef"
#cbc_key = b"\x40\xfe\xdf\x38\x6d\xa1\x3d"
# iv = Random.get_random_bytes(8)
#iv = b"\xfe\xdc\xba\x98\x76\x54\x32\x10"

try:
    iv_input = sys.argv[1]
    if len(iv_input) != 16:
        raise ValueError
    iv = bytes.fromhex(iv_input)              # str -> bytes
    cbc_key_input = sys.argv[2]
    if len(cbc_key_input) != 16:
        raise ValueError
    cbc_key = bytes.fromhex(cbc_key_input)
except ValueError:
    print("The value of iv and key must be hexadecimal digits and the length must be 8 bytes!")
    sys.exit()
try:
    file_name = sys.argv[3]
    #file_name = 'test.txt'
    f = open(file_name,'rb')
    plain_text = f.read()
except:
    print("Wrong file name!")
    sys.exit()

plain_text_array = bytearray(plain_text)
del plain_text_array[-1]
plain_text = bytes(plain_text_array)

des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
des2 = DES.new(cbc_key, DES.MODE_CBC, iv)

pad = 8 - len(plain_text) % 8
if pad != 8:
    for i in range(pad):
        plain_text = plain_text.__add__(b'\x00')

#print(plain_text)

time_encrypt_start = time.time()
cipher_text = des1.encrypt(plain_text)
time_encrypt_end = time.time()
time_encrypt = time_encrypt_end - time_encrypt_start
print(f'encrypt time is {time_encrypt}s.')

#print(cipher_text)
file_output = sys.argv[4]
with open(file_output, 'wb') as f:
    f.write(cipher_text)
    
time_decrypt_start = time.time()
msg=des2.decrypt(cipher_text)
time_decrypt_end = time.time()
time_decrypt = time_decrypt_end - time_decrypt_start
print(f'decrypt time is {time_decrypt}s.')
#print(msg)

