hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage *= 2
double_damage()


def disarmed():
    global hero_damage
    hero_damage *= 0.1
disarmed()


def power_potion():
    global hero_damage
    hero_damage += 100
power_potion()
