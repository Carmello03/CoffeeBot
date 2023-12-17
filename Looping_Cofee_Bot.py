LARGE = "large"
MEDIUM = "medium"
SMALL = "small"


def coffee_bot():
    print('Welcome to the cafe!')

    order_drink = "y"
    drinks = []
    while order_drink == "y":
        size = get_size()
        drink_type = get_drink_type()

        drink = f'{size} {drink_type}'
        print(f'Alright, that\'s a {drink}!')
        drinks.append(drink)

        while True:
            order_drink = order_input("Would you like to order another drink? (y/n)")
            if order_drink in ["y", "n"]:
                break

    print("Okay so i have")
    for drink in drinks:
        print(f"- {drink} ")

    name = order_input('Can I get your name please? \n> ')
    print(f'Thanks, {name}! Your order will be ready shortly.')


def get_size():
    res = order_input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>")
    drink_size = ""
    if res == "a":
        drink_size += SMALL
        return drink_size
    elif res == "b":
        drink_size += MEDIUM
        return drink_size
    elif res == "c":
        drink_size += LARGE
        return drink_size
    else:
        print_message()
        get_size()


def get_drink_type():
    res = order_input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

    if res == 'a':
        return order_brewed_coffee()
    elif res == 'b':
        return order_mocha()
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()


def order_brewed_coffee():
    while True:
        res = order_input("Would you like to try coffee brewed from the finest Brazilian grounds? \n[a] Yes! \n[b] No "
                          "way, Mister! \n>")
        if res == "a":
            return "Brazilian grounds coffee"
        elif res == "b":
            return "ordinary brewed coffee"
        print_message()


def order_mocha():
    while True:
        res = order_input('What type of drink would you like? \n  [a] Sure! \n[b] Maybe next time! \n> ')
        if res == "a":
            return "peppermint mocha"
        elif res == "b":
            return "mocha"
        else:
            print_message()


def order_latte():
    res = order_input("What type of drink would you like? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n>")
    if res == "a":
        return "latte"
    elif res == "b":
        return "non-fat latte"
    elif res == "c":
        return "soy latte"
    else:
        print_message()
        order_latte()


def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response")


def order_input(text):
    res = input(text)
    if res == "stop":
        print("Order cancelled!")
        coffee_bot()
    else:
        return res


coffee_bot()
