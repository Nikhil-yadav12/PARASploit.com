import base64
import send_email
import os

from cryptography.fernet import Fernet

def decrypt_file():
    # Get the password from the user
    password_provided = "password"
    password = password_provided.encode()

    # Generate the same salt used during encryption
    salt = b'\x80&<F\x8f\xaa;\\\xcc,J\xbf\xf1I\xd5y@\xb1\x1a\xcc'

    # Derive the key using the same key derivation function
    kdf = PBKDF2HMAC (
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    # Open the encrypted file and decrypt its contents
    with open('data.txt.encrypted', 'rb') as f:
        encrypted_data = f.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)

    # Write the decrypted data to a new file
    with open('data_decrypted.txt', 'wb') as f:
        f.write(decrypted_data)
    print('File decrypted successfully!')
