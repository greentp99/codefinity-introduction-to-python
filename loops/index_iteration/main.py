
# List of product prices
prices = [29.99, 45.50, 12.75, 38.20]

# Applying discounts based on index position
for index in range(len(prices)):
    original_price = prices[index]
    if index == 0:
        discount = 0.10  # 10% discount
    elif index == 1:
        discount = 0.20  # 20% discount
    elif index == 2:
        discount = 0.15  # 15% discount
    elif index == 3:
        discount = 0.05  # 5% discount
    else:
        discount = 0.0   # No discount for indices greater than 3
    
    # Calculate updated price
    updated_price = original_price * (1 - discount)
    prices[index] = updated_price  # Update the price in the list
    
    # Print updated price
    print(f"Updated price for item {index}: ${updated_price:.2f}")
    # Print with original_price
    # print(f"Original price for item {index}: ${original_price:.2f}")
    # print(f"Updated price for item {index}: ${updated_price:.2f}")
    #print without ".2f" formatting
    # print(f"Updated price for item {index}: ${updated_price:}")

