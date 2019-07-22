# '''
# We have n events that the user can pick from and we 
# have a budget. Determine how we will select the events
# using knapsack algorithm
# '''
result = []
def knapsack(n, value, constraint, weights):
    if n == 0 or constraint == 0:
        return 0
    elif weights[n-1] > constraint:
        return knapsack(n-1, value, constraint, weights)
    else:
        # don't put it in the knapsack
        tmp1 = knapsack(n-1, value, constraint, weights)
        # add it to the knapsack 
        tmp2 = value[n-1] + knapsack(n-1, value, constraint-weights[n-1], weights)
        return max(tmp1, tmp2)



values = [1,2,3,4]
wt = [10,20,30,25]
w = 50 
n = len(values) 
print(knapsack(n, values, w, wt))

'''
given a dictionary of event and cost
return a new dictionary that only has events that cost below
a certain limit and is in cost ascending order
'''
# def sort_by_cost()

