
# import random
# a1 = [random.randint(0, 1) for _ in range(5)]
# a2 = [random.randint(0, 1) for _ in range(5)]
# arl = a1 == a2
# print("First array:")
# print(a1)
# print("Second array:")
# print(a2)
# print("Test above two arrays are equal or not!")
# print(arl)





import random
def main(a):
    l = 'abcdefghijklmnopqrstuvwxyz'
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    t = '0123456789'
    r = '!@#$%^&*()_+-=[]{}|;:,.<>?/'
    c = l + u + t + r
    password = ''.join(random.choice(c) for _ in range(a))
    return password
s = int(input("Enter the desired password length: "))
password = main(s)
print("Generated password:", password)







