def make_trading_card(name, mana_value, power, toughness):
    return tuple([name, mana_value, power, toughness])

def trading_value(card):
    return card[2] + card[3]

def trading_card_sort_key(card):
    return trading_value(card)

def main():
    card1 = make_trading_card("Borborygmos", "3RRGG", 6, 7)
    print(card1)
    card2 = make_trading_card("Shivan Dragon", "4RR", 5, 5)
    print(card2)
    card3 = make_trading_card("Magic3", "3RGG", 6, 7)
    print(card3)
    card4 = make_trading_card("Magic4", "7G", 3, 7)
    print(card4)
    card5 = make_trading_card("Magic5", "0RGG", 6, 9)
    print(card5)

    print(trading_value(card2))
    l = [card1, card2, card3, card4, card5]
    print(l)
    l.sort(key=trading_card_sort_key, reverse=True)
    print(l)

if __name__  == "__main__":
    main()