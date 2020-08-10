def get_percentage(number, round_digits=None):
    if round_digits == None:
        return f'{round(number * 100)}%'
    else:
        return "{}%".format(round(number * 100, round_digits))
