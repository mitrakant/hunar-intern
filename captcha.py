import random
import string

def gen_capt(length=5):
    captcha=''
    for i in range(length):
        captcha += random.choice(string.ascii_letters + string.digits)
    return captcha
    
captcha= gen_capt(5)
print(captcha)
