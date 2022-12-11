"""
The cafe owner has his cafe's sales data that includes total amount of sales in each day of the week.
Find out when the sales was high and when it was low.

"""
num1 = []
for i in range(1,8,1):
   num2 = int(input("Enter the total amount of sales for Day "+str(i)+":"))
   num1.append(num2)

print(num1)
print("Highest sales of the week is: ",max(num1))
print("Least sales of the week is: ",min(num1))

max_index = num1.index(max(num1))
min_index = num1.index(min(num1))

print("The highest sales of the week is day: ",max_index+1)
print("The highest sales of the week is day: ",min_index+1)