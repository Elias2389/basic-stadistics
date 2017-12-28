import statistics

# Data for apply median, mean and mode
data_mean = [1525, 257, 378, 9543, 7854, 152]
data_median = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
data_mode = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]


# Method of get mean
def get_mean(array_data):
    return statistics.mean(array_data)


# Method of get mode
def get_mode(array_data):
    return statistics.mode(array_data)


# Method for get median
def get_median(array_data):
    return statistics.median(array_data)


# Print each result
print('Mean:', get_mean(data_mean))
print('Mode:', get_mode(data_mode))
print('Median:', get_median(data_median))
