# -------------------------------
# Assignment #4 Dice Simulation
# (dice.py)
# Eric Seyden
# 2023-01-27
# -------------------------------
# N = 2,000,000
# for empirical probability to
# match exact probability
# at 3 decimal places consistently.
# -------------------------------

import sys
import stdio
import stdarray
import random


def main(arg1):  # main function

    trials = int(arg1)  # cast argument 1 as integer for number of trials to run

    probability_list = generate_probability_list()  # call function to get probability list

    # call function to get empirical probability
    # based on a fixed number of trials
    empirical_probability_list = generate_empirical_probability(trials)

    possible_combined_dice_values = range(2, 13)  # range is all possible combinations of two dice

    # -------------------------------------------------------
    # output exact results
    # -------------------------------------------------------
    stdio.writeln("Exact results")
    for combined_dice_value in possible_combined_dice_values:
        stdio.writeln(
            "Probability the sum of die is "
            + str(combined_dice_value) + ": "
            + str(probability_list[combined_dice_value])
        )
    # -------------------------------------------------------

    # ------------------------------------------------------------
    # output empirical results
    # ------------------------------------------------------------
    stdio.writeln("\nEmpirical results")
    for combined_dice_value in possible_combined_dice_values:
        stdio.writeln(
            "Results the sum of die is "
            + str(combined_dice_value) + ": "
            + str(empirical_probability_list[combined_dice_value])
        )
    # ------------------------------------------------------------

    # -----------------------------------------------------
    # output difference between empirical and exact results
    # -----------------------------------------------------
    stdio.writeln("\nDifference")
    for combined_dice_value in possible_combined_dice_values:
        precision = 3
        # compute difference and round
        difference = round(
            probability_list[combined_dice_value]
            -
            empirical_probability_list[combined_dice_value]
            ,
            precision
        )
        stdio.writeln(

            "Difference when sum is "
            + str(combined_dice_value) + ": "
            + str(difference)
        )
    # -----------------------------------------------------


# -------------------------------------------------------------------------
# Exercise 1.4.20 Example code for generating dice roll probability list
# -------------------------------------------------------------------------
def generate_empirical_probability(number_of_trials):

    empirical_results_list = stdarray.create1D(13, 0.0)

    for trial_count in range(0, number_of_trials):
        dice_roll_result = random.randint(1, 6) + random.randint(1, 6)
        empirical_results_list[dice_roll_result] += 1.0

    empirical_probability_list = empirical_results_list[:]

    for combined_dice_value in range(2, 13):
        empirical_probability_list[combined_dice_value] /= number_of_trials

    return empirical_probability_list


# -------------------------------------------------------
# Exercise 1.4.20
# Example code for generating dice roll probability list
# -------------------------------------------------------
def generate_probability_list():
    probabilities = stdarray.create1D(13, 0.0)
    for die1_value in range(1, 7):
        for die2_value in range(1, 7):
            probabilities[die1_value + die2_value] += 1.0
    for combined_dice_value in range(2, 13):
        probabilities[combined_dice_value] /= 36.0
    return probabilities


def get_random_dice_value():
    return


if __name__ == "__main__":
    main(sys.argv[1])
