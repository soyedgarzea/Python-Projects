'''
    _summary_

_extended_summary_
'''
bidders = {}
max_bidder = ["", 0]

keep_bidding = True


def add_bidder():
    bidder = input("What is your name?\n")
    amount = int(input("How much are you bidding? $"))
    bidders[bidder] = amount

    if amount > max_bidder[1]:
        max_bidder[0] = bidder
        max_bidder[1] = amount


while keep_bidding:
    add_bidder()

    answer = input("Are there more bidders? (Yes/No) \n").lower()

    if answer == "no":
        keep_bidding = False
        print(f"The winner is {max_bidder[0]} with ${max_bidder[1]}")
