"""
 Calculate the salary for the phone salesman. Base pay is Rs10000. 
Based on the years of experience of the saleman the basepay increses.
Rs 2000 will be added for each year of experience.
For every 10 phones sold, he gets 13% of the base pay as commission
"""

base_pay = 10000
exp = int(input("Enter the year of experience: "))

increment = exp * 2000
print("Increment:",increment)

phone_sold = int(input("Enter the no of phones sold: "))

if(phone_sold >= 10):
   commission = 13/100 * base_pay  
   print("Commission:",commission)
   total_salary1 = base_pay + commission
   print("Amount of salary 1:",total_salary1)
    
else:
    print("No Commission")

if(exp >= 1):
   total_salary2 = base_pay + increment
   print("Amount of salary 2:",total_salary2)

else: 
   print("No Increment")

if(phone_sold >= 10 and exp >= 1):
    total_salary3 = base_pay + increment + commission
    print("Total amount of salary is: ", total_salary3)

Output:
Enter the year of experience: 1
Increment: 2000
Enter the no of phones sold: 10
Commission: 1300.0
Amount of salary 1: 11300.0
Amount of salary 2: 12000
Total amount of salary is:  13300.0
