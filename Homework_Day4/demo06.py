prices = [105, 110, 108, 112, 115, 116, 114]
window_size = 3
rolling_averages = []

for i in range(len(prices) - window_size + 1):
    
    window = prices[i : i + window_size]
    
    window_average = sum(window) / window_size
    
    rolling_averages.append(round(window_average, 2))

print(f"The stock prices are: {prices}")
print(f"The 3-day rolling averages are: {rolling_averages}")
