meat = ["Ham",3.99,50,"Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

#print(meat)
#print(cheese)
#print(condiment)

deli_dept = [meat, cheese, condiment]

print("Initial Deli List:", deli_dept)

if deli_dept[0][0] == "Ham" and deli_dept[0][2] < 100:
    #print(deli_dept[0][2])
    deli_dept[0][2] = 100
    #print(deli_dept)

seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
#print(deli_dept)

deli_dept.pop(2)
#print(deli_dept)

deli_dept.sort()
#print(deli_dept)

print("Updated Deli List:", deli_dept)
