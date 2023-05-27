from cryptography.fernet import Fernet
import time

def IWokeUpInANewBugatti(x):
    message = x # Put your message to encrypt
 
    key = Fernet.generate_key()
    fernet = Fernet(key)

    encMessage = fernet.encrypt(message.encode())
    print("Wait a bit more...")
    time.sleep(10)
    print(encMessage)
    print('Fuck, wrong message!')

    time.sleep(5)
    result = fernet.decrypt(encMessage).decode()
    print('Here is the result: ', result)