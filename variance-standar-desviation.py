import statistics,math

# Data for apply variance and standard deviation
data_variance = [13, 14, 15, 15, 15, 16, 17, 18, 20]


# Method of calculate variance
def get_variance(array_data):
    variance = statistics.mean(array_data)
    sum_data = 0
    for data in array_data:
        sum_data += (data - variance)**2
    return sum_data/array_data.__len__()


# Print variance
print('Variance:', get_variance(data_variance))

# Print standard deviation
print('Standard deviation:', math.sqrt(get_variance(data_variance)))

