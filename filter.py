def filter(x, y, z):
    if(x>=100):
        print("That's a big number")
    else:
        print("That's a small number")

    if(len(y)>=50):
        print("Long Sentence")
    else:
        print("Short Sentence")

    if(len(z)>=10):
        print("Big list")
    else:
        print("Small list")
    return;

filter(41, "Ruber baby buggy bumpers",[1,7,4,21])