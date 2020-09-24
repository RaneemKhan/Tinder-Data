def tinder_data():
    tinder = open("tinderdata.txt", "r")
    category = tinder.readline().strip()
    lst = tinder.readlines()
    count = 0
    i = 1
    dict = {}
    print("TINDER DATA")
    while i < len(lst):
        num = int(lst[i].strip())
        count += num
        i += 2
        try:
            if len(lst[i].strip()) == 11:
                print(category + ": " + str(count))
                dict[category] = count
                count = 0
                category = lst[i-1].strip()
                i +=1
        except IndexError:
            break
    print("STATISTICS")
    match_rate = round(dict["matches"]/dict["swipes_likes"]*100, 2)
    swipe_right_rate = round((dict["swipes_likes"]/dict["swipes_passes"]*100), 2)
    swipe_left_rate = round((dict["swipes_passes"]/dict["swipes_likes"]))
    print("Match Rate: " + str(match_rate))
    print("Swipe Right Rate: " + str(swipe_right_rate))
    print("One swipe right for every " + str(swipe_left_rate) + " swipes left")


tinder_data()