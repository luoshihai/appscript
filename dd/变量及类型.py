

i = 0


while i < 9:

    j = 0
    while j < i:
        print("%d * %d = %d\t" %(j + 1,i + 1,(j +1)*(i + 1)), end="")
        j += 1

    print("")
    i += 1


