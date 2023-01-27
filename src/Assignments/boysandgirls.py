# ----------------------------------------------------
# Assignment #3
# ( boysandgirls.py )
#
# Eric Seyden
# 2023-01-27
#
# A couple beginning a family decides to keep having children
# until they have at least one of either sex.
# Estimate the average number of children
# they will have via simulation.
# The number of trials is given as a command-line argument.
# Also estimate the most common outcome
#  - record the frequency counts for 2, 3, and 4 children
#  - also for 5 and above
#  Assume that the probability p of having a boy or girl is 1/2.
# -----------------------------------------------------
import sys
import stdio
import stdarray
import random


def main(arg1):  # main entrypoint handles iterating over trials
    trials = int(arg1)  # cast argument 1 as int
    results = stdarray.create1D(trials, None)  # initialize trial results aray with null values
    distribution_list = stdarray.create1D(6, 0)  # init array to hold distribution stats

    for c in range(0, trials):  # iterate for the number of trials requested
        result = run_trial()  # call trial function and store the number of children
        if result > 5:  # bin results with more than 5 as 5
            result = 5
        distribution_list[result] += 1  # increment corresponding result counter

        results[c] = result  # store result with the trial number as index

    average_child_count = sum(results) // trials  # calculate average number of children

    # output results
    stdio.writeln("Avg # children: " + str(average_child_count))
    stdio.writeln("Trials with 2 children: " + str(distribution_list[2]))
    stdio.writeln("Trials with 3 children: " + str(distribution_list[3]))
    stdio.writeln("Trials with 4 children: " + str(distribution_list[4]))
    stdio.writeln("Trials with 5 or more children: " + str(distribution_list[5]))


# run trial function
# randomly generates the number of children
# required to have one boy and one girl
def run_trial():
    # initialize child counters
    boy_counter = 0
    girl_counter = 0

    # continue to generate random children until
    # both counters are not zero
    while boy_counter == 0 or girl_counter == 0:
        if random.randint(0, 1) == 0:  # randomly pick 1 or 0
            girl_counter += 1  # increment girl counter if zero
        else:
            boy_counter += 1  # increment boy counter if not zero

    return girl_counter + boy_counter  # return total of boys and girls


if __name__ == "__main__":  # if script is run via command line pass first argument to main function
    main(sys.argv[1])
