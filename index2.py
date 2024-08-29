
import random
a1 = [random.randint(0, 1) for _ in range(5)]
a2 = [random.randint(0, 1) for _ in range(5)]
arl = a1 == a2
print("First array:")
print(a1)
print("Second array:")
print(a2)
print("Test above two arrays are equal or not!")
print(arl)

