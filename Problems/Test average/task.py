def average_mark(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return round(sum / len(numbers), 1)
