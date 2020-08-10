# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
max_value = max(test_dict.values())
min_value = min(test_dict.values())

for name, value in test_dict.items():
    if min_value == value:
        print("min: {}".format(name))

for name, value in test_dict.items():
    if max_value == value:
        print("max: {}".format(name))
