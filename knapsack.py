'''
We have n events that the user can pick from and we 
have a budget. Determine how we will select the events
using knapsack algorithm
'''
def printknapSack(W, wt, val, n): 
    return_values = []
    return_indices = []
    return_weights = []
    K = [[0 for w in range(W + 1)] 
            for i in range(n + 1)] 
              
    # Build table K[][] in bottom 
    # up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i - 1] <= w: 
                K[i][w] = max(val[i - 1]  
                  + K[i - 1][w - wt[i - 1]], 
                               K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w] 
  
    # stores the result of Knapsack 
    res = K[n][W] 
      
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        # either the result comes from the 
        # top (K[i-1][w]) or from (val[i-1] 
        # + K[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if res == K[i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            return_values.append(val[i - 1])
            return_weights.append(wt[i - 1])
            return_indices.append(i-1)
              
            # Since this weight is included 
            # its value is deducted 
            res = res - val[i - 1] 
            w = w - wt[i - 1] 
    return return_indices

hello = printknapSack(50,[30,20,10,10,10],[2,5,7,4,8],5)
print(hello)