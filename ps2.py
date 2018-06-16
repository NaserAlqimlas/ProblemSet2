import numpy as np  #you may need to install this package
from timeit import default_timer as timer


def part_A(cups_of_gold):
    max_gold_so_far = 0
    for i in range(len(cups_of_gold)-1):
        for j in range(i+1, len(cups_of_gold)):
            gold = cups_of_gold[j] - cups_of_gold[i]
            if gold > max_gold_so_far:
                max_gold_so_far = gold
    return max_gold_so_far

def d_helper(cups_of_gold):
    M = list(range(len(cups_of_gold)))
    M[0] = cups_of_gold[0]

    for i in range(len(cups_of_gold)):
        if(cups_of_gold[i] < M[i-1]):
            M[i] = cups_of_gold[i]
        else:
            M[i] = M[i-1]
    return M

def part_D(cups_of_gold):
    max_gold_so_far = 0
    M = d_helper(cups_of_gold)

    for i in range(len(cups_of_gold)):
        check = cups_of_gold[i]-M[i]
        if check > max_gold_so_far:
            max_gold_so_far = check

    return max_gold_so_far



times = []
print('Part D results:')
for seed in range(10):  #running the loop for 10 iterations, using seed for the random generator
    np.random.seed(seed)  # sets the seed for the random generator
    cups_of_gold = np.random.randint(low=1,high=1001, size=1000)#cups_of_gold is list with 1000 elements, where the elements are positive integers in range(1, 1000)

    start_A = timer()   #start the timer for part A
    result_A = part_A(cups_of_gold) #run part A algorithm
    total_time_A = timer() - start_A    #calculate total time for part A

    start_D = timer()   #start the timer for part D
    result_D = part_D(cups_of_gold) #run part D algorithm
    print(result_D)
    total_time_D = timer() - start_D    #calculate total time for part D

    times.append([total_time_A, total_time_D])  #add the times to the list

    if result_A != result_D:    #checks if the algorithms are calculating the same result
        print('One of your algorithms has a mistake.')
        quit()

times = np.array(times) #makes the list print nicely
print()
print('[Part A Times, Part D Times]')
print(times)


