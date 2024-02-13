def max_subsequence_sum_1(values):

    size = len(values)
    max_sum = 0
    i = 0

    while(i < size):
        j = i
        while j < size:
            this_sum = 0
            k = i
            while k <= j:
                this_sum += values[k]
                k += 1