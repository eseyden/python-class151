# -------------------------------
# Assignment #4 Dice Simulation
# (dice.py)
# Eric Seyden
# 2023-01-27
# -------------------------------
# N = 2,500,000
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
        # compute difference and round to three places
        precision = 3
        difference = round(
            probability_list[combined_dice_value]
            -
            empirical_probability_list[combined_dice_value]
            ,
            precision
        )
        # output difference
        stdio.writeln(

            "Difference when sum is "
            + str(combined_dice_value) + ": "
            + str(difference)
        )
    # -----------------------------------------------------


# -------------------------------------------------------------------------
# Generate Empirical Probability
#
# Given a number of trials simulate rolling dice
# With the simulated dataset
# calculate the probability of getting a particular value
# -------------------------------------------------------------------------
def generate_empirical_probability(number_of_trials):
    # initialize result list with zero value
    # array index is the range of possible
    # combinations of two dice
    empirical_results_list = stdarray.create1D(13, 0.0)

    # run dice rolling simulation for requested number of trials
    for trial_count in range(0, number_of_trials):
        # add two random ints with values between one and six
        dice_roll_result = random.randint(1, 6) + random.randint(1, 6)
        # add one to tally list of results
        empirical_results_list[dice_roll_result] += 1.0

    # I was making a copy to see the tally totals
    # Replaced with pointer reference to save memory
    # empirical_probability_list = empirical_results_list[:]
    empirical_probability_list = empirical_results_list

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


if __name__ == "__main__":  # check if run from command line
    main(sys.argv[1])  # pass command line argument to main function
