import random

chars = "abcdeffghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!#*$&^%(`)"
while 10:
    password_len = int(input("your password should be the length of? "))
    password_count = int(input("how many passwords do you need: "))
    for x in range(0,password_count):
        password=""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password+ password_char
        print("here is your password: ",password)
