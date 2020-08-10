def final_deposit_amount(*interest, amount=1000):
    for i in interest:
        amount *= (1 + (i / 100))
    return round(amount, 2)
