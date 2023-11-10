# 1. B Backward countdown, printing 'E' instead of 3 and 'A' insted of 4
for i in range (9, -1, -1):
  if (i == 3):
    i = 'E'
  elif (i == 4):
    i = 'A'
  for j in range (9, -1, -1):
    if (j == 3):
      
      j = 'E'
    elif (j == 4):
      j = 'A'
    print(i,j)

# 1. B Same as previous but with and input
user = input('Type a number under 100')
n = int(user)
final = ''
for i in range (0, n+1):
 
  final = i
  if i <= 9:
    final = '0' + str(i)
  
  print (final)
  
# 2 Taxes calculations by sections
user = input('Type a your annual income')
income = int(user)
lowest = 12450
tax_1 = 20200
tax_2 = 35000
tax_3 = 60000
greatest = 300000
second_section = tax_1 - lowest
third_section = tax_2 - tax_3
fourth_section = tax_3 - greatest
fifth_section = income - greatest
if income <= lowest:
  tax_rate = '19% section. Less than' + str(lowest)
  taxes = income * 0.19
  net_amount = income - taxes
elif income > lowest and income < tax_1:
  tax_rate = '24% section. From ' + str(lowest) + ' to ' + str(tax_1)
  taxes = lowest*0.19 + (income - second_section)*0.24
  net_amount = income - taxes
elif income > tax_1 and income <= tax_2:
  tax_rate = '30% section. From ' + str(tax_1) + ' to ' + str(tax_2)
  taxes = lowest*0.19 + second_section*0.24 + (income - lowest - second_section)*0.3
  net_amount = income - taxes
elif income > tax_2 and income < tax_3:
  tax_rate = '37% section. From ' + str(tax_2) + ' to ' + str(tax_3)
  taxes = lowest*0.19 + second_section*0.24 + second_section*0.3 + (income - lowest - second_section - third_section)*0.37
  net_amount = income - taxes
elif income > tax_3 and income < greatest:
  tax_rate = '45% section. From ' + str(tax_3) + ' to ' + str(greatest)
  taxes = lowest*0.19 + second_section*0.24 + second_section*0.3 + third_section*0.37+ (income - lowest - second_section - third_section - fourth_section)*0.45
  net_amount = income - taxes
else:
  tax_rate = '47% section. More than' + str(greatest)
  taxes = lowest*0.19 + second_section*0.24 + second_section*0.3 + third_section*0.37 + fourth_section*0.45 + (income - lowest - second_section - third_section - fourth_section - greatest)*0.47
  net_amount = income - taxes
print(tax_rate, taxes, net_amount)