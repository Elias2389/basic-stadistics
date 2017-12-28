import math

# Calculate linear regression

houses = [
    {'month': 1, 'mts': 5, 'price': 375},
    {'month': 2, 'mts': 15, 'price': 487},
    {'month': 3, 'mts': 20, 'price': 450},
    {'month': 4, 'mts': 25, 'price': 500},
]

# Calculate pending
total = 0
total_sum_prices = 0
total_sum_sqrt = 0
total_sum_sqrt_all = 0
multiply_array = []

for data in houses:
    # 1 multiply each month with your price and after sum
    result = data['month'] * data['price']
    multiply_array.append(result)
    total = total + result

    # Sum prices
    total_sum_prices = total_sum_prices + data['price']

    # Sqrt of each month
    result_sqrt = math.sqrt(data['month'])
    total_sum_sqrt = total_sum_sqrt + result_sqrt

    # Sqrt of all month
    total_sum_sqrt_all = total_sum_sqrt_all + data['month']
    total_sqrt_all = math.sqrt(total_sum_sqrt_all)

print('Each multiply:', multiply_array)
print('Result:', total)
print('Result sum prices:', total_sum_prices)
print('Result sum sqrt:', total_sum_sqrt)
print('Result sqrt general of month:', total_sqrt_all)
