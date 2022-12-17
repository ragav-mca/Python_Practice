"""
Same as above, but there is a change in the way commission is calculated.
For the first 10 phones sold, commission is 13%, for the next 10 phones sold,it is 15%, 
and one percent increse for every 5 phones sold after that. 
(Hint -  write down the percent of commission for different number of phones sold and 
understand the problem,  before writing the  program)
"""

base_pay = 10000
exp = int(input("Enter the year of experience: "))
leave_count = int(input("Enter the no of days leave: "))
lop = leave_count * 200
percentage1 = 13/100
percentage2 = 15/100
phone_sold = int(input("Enter the no of phones sold: "))
print("Loss of pay is: ",lop)
x=0
y=0
b=0
if(exp >= 1):
   increment = exp * 2000
   print("Increment:",increment)
else:
    print("No Increment")

if(phone_sold >= 10):
    x = percentage1 * base_pay 
    y = phone_sold - 10
    print(y)
    total_salary1 = x + base_pay 
    print("Salary for first 10 phones sold is:",total_salary1)

if(y >= 10):
    a = percentage2 * base_pay
    b = y - 10
    print(b)
    total_salary2 = a + base_pay
    print("Salary for second 10 phones sold is:",total_salary2)

    
while b >= 5:
    percentage3 = percentage2 + 1/100
    b -= 5
j = percentage3 * base_pay
total_salary3 = j + base_pay
    
print("Salary for next 5 phones sold is:",total_salary3)

if(exp >= 1 and phone_sold >= 10 and leave_count >=1):
    total_salary4 = increment + total_salary1 - lop
    print("Total amount of salary is:",total_salary4)
elif(exp >= 1 and y >= 10 and leave_count >=1):
    total_salary5 = increment + total_salary2 - lop
    print("Total amount of salary is:",total_salary5)
elif(exp >= 1 and b >= 5 and leave_count >=1):
    total_salary6 = increment + total_salary3 - lop
    print("Total amount of salary is:",total_salary6)

    
