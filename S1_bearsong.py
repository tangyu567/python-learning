word = "bottles"

for bear_num in range(99, 0, -1):
    print (bear_num, word, "of beer on the wall.")
    print ("bear_num", "bottles of bear.")
    print ("Take one down.")
    print ("Pass it atound.")
    if bear_num == 1:
        print ("No more bear on the wall.")
    else:
        new_num = bear_num - 1
        if new_num == 1:
            word = "bottle"
        print (new_num, word, "of bear on the wall.")
        print()
    
