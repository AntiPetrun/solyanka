from decimal import Decimal
weight = Decimal(input('Enter your weight in kg: '))
height = Decimal(input('Enter your height in m: '))
bmi_index = round(Decimal(weight) / Decimal(height ** 2))
bmi_scale = '20' + '=' * (bmi_index - 21) + '|' + '=' * (49 - bmi_index) + '50'
print(f'Your body mass inde: {bmi_index}\n' + bmi_scale)
