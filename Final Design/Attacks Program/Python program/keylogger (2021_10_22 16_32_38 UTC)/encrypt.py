import base64
import send_email
import os

from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt_file():
       
       password_provided = "password"# This is input in the form of a string
       password = password_provided.encode () #Convert to type bytes

       salt=b'\x80&<F\x8f\xaa;\\\xcc,J\xbf\xf1I\xd5y@\xb1\x1a\xcc'

       kdf = PBKDF2HMAC (
              algorithm=hashes.SHA256 (),
              length=32,
              salt=salt,
              iterations=100000,
              backend=default_backend ()
       )

       key = base64.urlsafe_b64encode (kdf.derive (password)) # Can only use kdf once

       print (key)  #This is the Key, Whivh is used


       #Encryption & Decryption code
       from cryptography.fernet import Fernet

       # Open the file to encrypt
       with open('data.txt','rb') as f:
              data = f.read()

       # Encrypt the file
       f = Fernet(key)
       encrypted = f.encrypt(data)

       # Write the Encrypted File
       with open('data.txt.encrypted','wb') as f:
              f.write(encrypted)
       print(encrypted)

       send_email.send_email()