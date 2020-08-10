def congratulations(*developers):
    namelist = list()
    for i in developers:
        for names in i.split():
            namelist.append(names)

    print("Happy New Year! Take care of yourself and your loved ones!")
    print("For:")

    for name in namelist:
        print(name)
