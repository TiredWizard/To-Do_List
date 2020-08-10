def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
    return x + (5 - x % 5)


# n1 = input()
# n2 = int(n1)
# print(closest_higher_mod_5(n2))
