
# def main(a):
#     if a == "Darth Vader":
#         print(f"Luke,I am your father")
#     elif a == "Leia":
#         print(f"Luke,I am your sister")
#     elif a == "Han":
#         print(f"Luke,I am your brother")
#     elif a == "R2D2":
#         print(f"Luke,I am your droid")
# main("Darth Vader")
# main("Leia")
# main("Han")
# main("R2D2")
# main("Darth Vader")



# def main(a):
#     for i in a[1:]:
#         print(i,end="")
# main("apple")
# print()
# main("cherry")
# print()
# main("plum")



# def dis(a, s):
#     return a * (1 - s / 100)
# print(dis(1500, 50))
# print(dis(89, 20)) 
# print(dis(100, 75))

        
        
# def potatoes(s):
#     return sum(1 for i in range(len(s)) if s[i:i+6] == "potato")
# print(potatoes("potato"))
# print(potatoes("potatopotato")) 
# print(potatoes("potatopotatoorange"))



# def main(lst):
#     return sum(x for x in lst if x > 5)
# print(main([1, 5, 20, 30, 4, 9, 18])) 
# print(main([1, 2, 3,4])) 
# print(main([10, 12, 28,47,55,100])) 




# def main(a):
#     s = a[:2]
#     stuttered = f"{s}... {s}... {a}?"
#     return stuttered
# print(main("incredible")) 




# def reverser(s):
#     return s[::-1].swapcase()
# print(reverser("Hello World"))
# print(reverser("ReVeRsE"))




# def main(n):
#     a = n // 2
#     if n % 2 == 0:
#         return [a, a]
#     else:
#         return [a, a + (1 if n > 0 else -1)]
# print(main(4))
# print(main(10))





def main(a, b, c):
    n = a - b
    s = (c + n - 1) // n
    return s
print(main(4000, 2000, 77000))
print(main(3000, 2000, 50699))
print(main(30000, 25000, 390205))





