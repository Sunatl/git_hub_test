
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





# import random
# def main(a):
#     l = 'abcdefghijklmnopqrstuvwxyz'
#     u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     t = '0123456789'
#     r = '!@#$%^&*()_+-=[]{}|;:,.<>?/'
#     c = l + u + t + r
#     password = ''.join(random.choice(c) for _ in range(a))
#     return password
# s = int(input("Enter the desired password length: "))
# password = main(s)
# print("Generated password:", password)



# import random
# s = ["Rock", "Paper", "Scissors"]
# c = int(input("Select your move (1 for Rock, 2 for Paper, 3 for Scissors): ")) - 1
# r = random.randint(0, 2)
# print("Computer chose", s[r],end="")
# if c == r:
#     print(".It's a tie!")
# elif (c == 0 and r == 2) or (c == 1 and r == 0) or (c == 2 and r == 1):
#     print(".You win!")
# else:
#     print(".You lose!")








import random
cnt = 0
lives = 5
r = random.randint(1, 100)
print("Guess the number between 1 and 100. You have 5 lives.")
while cnt < lives:
        a = int(input("Enter your guess: "))
        
        if a < 1 or a > 100:
            print("Please enter a number between 1 and 100.")
            continue
        cnt += 1
        if a == r:
            print("You win! The number was", r)
            break
        elif a < r:
            print("Too low")
        elif a > r:
            print("Too high")
        if cnt >= lives:
            print("Game over! The number was", r)
            break

        
        
    

