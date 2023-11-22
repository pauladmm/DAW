# 1. B Backward countdown, printing 'E' instead of 3 and 'A' insted of 4
# it is better to declare constants instead of hard-coding numbers
VALUE_E = 3
OUTPUT_E = 'E'
VALUE_A = 4
OUTPUT_A = 'A'

for i in range (9, -1, -1):
  if i == VALUE_E:
    output_i = OUTPUT_E
  elif i == VALUE_A:
    output_i = OUTPUT_A
  else:
    output_i = str(i)
  for j in range (9, -1, -1):
    if j == VALUE_E:
      output_j = OUTPUT_E
    elif j == VALUE_A:
      output_j = OUTPUT_A
    else:
      output_j = str(j)
    print(output_i + output_j)

# 1. B Same as previous but with an input
VALUE_E = 3
OUTPUT_E = 'E'
VALUE_A = 4
OUTPUT_A = 'A'

counter = 0
limit = input('Please enter a number: ')
limit = int(limit)
for i in range(0, 10):
    if i == VALUE_E:
        output_i = OUTPUT_E
    elif i == VALUE_A:
        output_i = OUTPUT_A
    else:
        output_i = str(i)
    for j in range(0, 10):
        if j == VALUE_E:
            output_j = OUTPUT_E
        elif j == VALUE_A:
            output_j = OUTPUT_A
        else:
            output_j = str(j)
        print(output_i + output_j)
        counter += 1
        if counter == limit:
            break
    if counter == limit:
        break
  
# 2 Taxes calculations by sections
user = input('Type a your annual income')
income = int(user)
PERCENT_1 = 0.19
LOWEST_LIMIT = 12450
PERCENT_2 = 0.24
LIMIT_1 = 20200
PERCENT_3 = 0.30
LIMIT_2 = 35000
PERCENT_4 = 0.37
LIMIT_3 = 60000
PERCENT_5 = 0.45
HIGHEST_LIMIT = 300000
PERCENT_6 = 0.47
SECOND_SECTION = LIMIT_1 - LOWEST_LIMIT
THIRD_SECTION = LIMIT_2 - LIMIT_3
FOURTH_SECTION = LIMIT_3 - HIGHEST_LIMIT
FIFTH_SECTION = income - HIGHEST_LIMIT
if income <= LOWEST_LIMIT:
  tax_rate = '19% section. Less than' + str(LOWEST_LIMIT)
  taxes = income * PERCENT_1
  net_amount = income - taxes
elif income > LOWEST_LIMIT and income < LIMIT_1:
  tax_rate = '24% section. From ' + str(LOWEST_LIMIT) + ' to ' + str(tax_1)
  taxes = LOWEST_LIMIT*PERCENT_1 + (income - SECOND_SECTION)*PERCENT_2
  net_amount = income - taxes
elif income > LIMIT_1 and income <= LIMIT_2:
  tax_rate = '30% section. From ' + str(LIMIT_1) + ' to ' + str(LIMIT_2)
  taxes = LOWEST_LIMIT*PERCENT_1 + SECOND_SECTION*PERCENT_2+ (income - LOWEST_LIMIT - SECOND_SECTION)*PERCENT_3
  net_amount = income - taxes
elif income > LIMIT_1 and income < LIMIT_3:
  tax_rate = '37% section. From ' + str(LIMIT_2) + ' to ' + str(LIMIT_3)
  taxes = LOWEST_LIMIT*PERCENT_1 + SECOND_SECTION*PERCENT_2+ SECOND_SECTION*PERCENT_3 + (income - LOWEST_LIMIT - SECOND_SECTION - THIRD_SECTION)*0.37
  net_amount = income - taxes
elif income > LIMIT_3 and income < HIGHEST_LIMIT:
  tax_rate = '45% section. From ' + str(LIMIT_3) + ' to ' + str(HIGHEST_LIMIT)
  taxes = LOWEST_LIMIT*PERCENT_1 + LIMIT_2*PERCENT_2 + SECOND_SECTION*PERCENT_3 + THIRD_SECTION*PERCENT_4+ (income - LOWEST_LIMIT - SECOND_SECTION - THIRD_SECTION - FOURTH_SECTION)*PERCENT_5
  net_amount = income - taxes
else:
  tax_rate = '47% section. More than' + str(HIGHEST_LIMIT)
  taxes = LOWEST_LIMIT*PERCENT_1 + SECOND_SECTION*PERCENT_2 + SECOND_SECTION*PERCENT_3 + THIRD_SECTION*PERCENT_4+ FOURTH_SECTION*PERCENT_5 + (income - LOWEST_LIMIT - SECOND_SECTION - THIRD_SECTION - FOURTH_SECTION - HIGHEST_LIMIT)*PERCENT_6
  net_amount = income - taxes
print(tax_rate, taxes, net_amount)