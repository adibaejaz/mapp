from tools import NUM_VERTICES, NUM_PAIRS
import random


def generate_graph():
    """Function to generate and print a random graph in specified format."""
    print("EDGES")
    for x in range(1, NUM_VERTICES + 1):
        print(f"{x}:", end=" ")
        randomlist = random.sample(range(1, 101), random.randint(5,10))
        for num in randomlist:
          if num!= x:
                print(num, end=" ")
        print("")

    print("PAIRS")
    randomlist = random.sample(range(1, NUM_VERTICES + 1), NUM_PAIRS * 2)
    for x in range(0, NUM_PAIRS * 2, 2):
        print(f"{randomlist[x]} {randomlist[x+1]}")


generate_graph()
