from logo import logo


def secret_auction():
    bids = accept_bids()
    find_highest_bid(bids)


def accept_bids(bids={}):
    print(logo)
    name = input("What is your name: ")
    amount = int(input("What is your bid: $"))
    bids[name] = amount
    continue_bid = input(
        "Are there any other players? Please type 'yes' or 'no'"
    ).lower()
    if continue_bid == "yes":
        return accept_bids(bids)
    else:
        return bids


def find_highest_bid(
    bids, highest_bidder=None, highest_bid=float("-inf")
):
    for bidder in bids:
        bid = bids[bidder]
        if bid > highest_bid:
            highest_bidder = bidder
            highest_bid = bid
    print(f"The winner is {highest_bidder} with a bid of {highest_bid}!")


def main():
    play_again = True
    while play_again:
        secret_auction()
        restart_game = input("Restart the game? Type 'yes' or 'no': ")
        if restart_game == "no":
            play_again = False
    print("Thanks for participating in the blind auction!")


if __name__ == "__main__":
    main()
