# use the function blackbox(lst) that is already defined

lst = [2, 4, 2, 5, 6]

if id(lst) == id(blackbox(lst)):
    print("modifies")
else:
    print("new")
