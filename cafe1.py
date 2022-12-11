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

Output:
Enter the total amount of sales for Day 1:2893
Enter the total amount of sales for Day 2:2637
Enter the total amount of sales for Day 3:2727
Enter the total amount of sales for Day 4:2748
Enter the total amount of sales for Day 5:2657
Enter the total amount of sales for Day 6:3256 
Enter the total amount of sales for Day 7:3784
Enter the total amount of sales for Day 8:3921
Enter the total amount of sales for Day 9:3483
Enter the total amount of sales for Day 10:2838
Enter the total amount of sales for Day 11:3485
Enter the total amount of sales for Day 12:2657
Enter the total amount of sales for Day 13:2747 
Enter the total amount of sales for Day 14:2737
Enter the total amount of sales for Day 15:4274
Enter the total amount of sales for Day 16:3784
Enter the total amount of sales for Day 17:2943
Enter the total amount of sales for Day 18:3845
Enter the total amount of sales for Day 19:3929
Enter the total amount of sales for Day 20:3175
Enter the total amount of sales for Day 21:3490
Enter the total amount of sales for Day 22:3567
Enter the total amount of sales for Day 23:3092
Enter the total amount of sales for Day 24:3475
Enter the total amount of sales for Day 25:3849
Enter the total amount of sales for Day 26:4267
Enter the total amount of sales for Day 27:3289
Enter the total amount of sales for Day 28:2838 
Enter the total amount of sales for Day 29:3847
Enter the total amount of sales for Day 30:3474
[2893, 2637, 2727, 2748, 2657, 3256, 3784, 3921, 3483, 2838, 3485, 2657, 2747, 2737, 4274, 3784, 2943, 3845, 3929, 3175, 3490, 3567, 3092, 3475, 3849, 4267, 3289, 2838, 3847, 3474]
None
[2637, 2657, 2657, 2727, 2737, 2747, 2748, 2838, 2838, 2893, 2943, 3092, 3175, 3256, 3289, 3474, 3475, 3483, 3485, 3490, 3567, 3784, 3784, 3845, 3847, 3849, 3921, 3929, 4267, 4274]
The maximum sales of three days in a month :  4274 4267 3929
The minimum sales of three days in a month :  2637 2657 2657
