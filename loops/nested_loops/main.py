produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# Combine lists into a single list
groceries = [produce, dairy]

# Nested loops to print each item
for section in groceries:
    for item in section:
        print(f"Item name: {item}")




# num1 = [1,2,3,4,5,6,7,8,9,10]
# num2 = [1,2,3,4,5,6,7,8,9,10]

# for first in num1:
#     for second in num2:
#         print((first)," x ",(second)," = ",first*second)