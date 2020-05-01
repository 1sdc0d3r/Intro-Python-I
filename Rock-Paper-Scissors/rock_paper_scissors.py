import random

# with open("stats.txt", "r") as stats:
#     history = stats.read().split(",")
#     return history


def show_welcome_message():
    welcome_message = "Welcome to Rock, Paper, Scissors!"
    print(welcome_message)


def load_stats():
    stats_file = open("stats.txt", "r")
    history = stats_file.read().split(",")
    stats_file.close()
    return history


def save_stats(w, t, l):
    stats_file = open("stats.txt", "w")
    stats_file.write("%i,%i,%i" % (w, t, l))
    stats_file.close()


results = load_stats()
show_welcome_message()

wins = int(results[0])
ties = int(results[1])
losses = int(results[2])
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("please choose to continue...")

computer = random.randint(1, 3)
user = int(input("[1] Rock  [2] Paper  [3] Scissors  [9] Quit \n"))

while not user == 9:
    # print("user: {}, computer: {}".format(user, computer))

    # user chooses ROCK
    if user == 1:
        if computer == 1:
            print("Computer chose rock...tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose paper...computer wins :(")
            losses += 1
        elif computer == 3:
            print("Computer chose scissors...you win :)")
            wins += 1

    # user chooses PAPER
    elif user == 2:
        if computer == 1:
            print("Computer chose rock...you win :)")
            wins += 1
        elif computer == 2:
            print("Computer chose paper...tie!")
            ties += 1
        elif computer == 3:
            print("Computer chose scissors...computer wins :(")
            losses += 1

    # user chooses SCISSORS
    elif user == 3:
        if computer == 1:
            print("Computer chose rock...computer wins :(")
            losses += 1
        elif computer == 2:
            print("Computer chose paper...you win :)")
            wins += 1
        elif computer == 3:
            print("Computer chose scissors...tie!")
            ties += 1
    else:
        print("Invalid selection. Please try again.")

    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
    computer = random.randint(1, 3)
    user = int(input("[1] Rock  [2] Paper  [3] Scissors  [9] Quit \n"))
save_stats(wins, ties, losses)
