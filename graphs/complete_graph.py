for x in range(100):
    print(x, end=":")
    for y in range(100):
        if y - x:
            print("",  y, end="")
    print("")
