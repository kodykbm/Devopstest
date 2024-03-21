def main():
    while True:
        print_greeting()

        # Inputs
        while True:
            loseorgain = lose_or_gain()
            if loseorgain == "lose":
                weight = get_weight()
                goalweight = goal_weight()
                weightloss = calc_weight(weight, goalweight)
                weightgoals(weightloss)
                break
            elif loseorgain == "gain":
                weight = get_weight()
                goalweight = goal_weight()
                weightgain = calc_weight(goalweight, weight)
                weightgaingoals(weightgain)
                break
            else:
                print("Sorry, i didn't catch that, please enter gain or lose")

        recalc = restart()
        if recalc.lower() != "y":
            break


def print_greeting():
    print("Hey! Its time to get back in shape!\n")


def lose_or_gain():
    return input("Are you looking to gain weight or lose weight? (Type gain or lose)")


def get_weight():
    return float(input('How much do you weigh in pounds?'))


def goal_weight():
    return float(input('How much would you like to weigh?'))


def calc_weight(weight, goalweight):
    return weight - goalweight


def weightgoals(weightloss):
    print("The amount of weight you have to lose is ", format(weightloss, ".1f"), "pounds.")
    print("You can do it!")


def weightgaingoals(weightgain):
    print("The amount of weight you have to gain is ", format(weightgain, ".1f"), "pounds.")
    print("You can do it!")


def restart():
    return input("Would you like to set a different goal? (y/n): ")


main()
