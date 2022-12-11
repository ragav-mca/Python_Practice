"""
The cafe owner has his cafe's sales data that includes total amount of sales in each day of the month.
Find out the top 3 days when the sales was high and the 3 days when the sales was low.
"""
num1 = []
for i in range(1,31,1):
   num2 = int(input("Enter the total amount of sales for Day "+str(i)+":"))
   num1.append(num2)

print(num1)

print(num1.sort())
print(num1)
print("The maximum sales of three days in a month : ",num1[29],num1[28],num1[27])
print("The minimum sales of three days in a month : ",num1[0],num1[1],num1[2])