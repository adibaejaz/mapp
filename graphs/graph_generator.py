import random


print("EDGES")
for x in range(1, 101):
    print(f"{x}:", end=" ")
    randomlist = random.sample(range(1, 101), random.randint(5,10))
    for num in randomlist:
      if num!= x:
            print(num, end= " ")
    print("")

print("PAIRS")
randomlist = random.sample(range(1,101), 20)
for x in range(0, 18, 2):
    print(f"{randomlist[x]} {randomlist[x+1]}")



