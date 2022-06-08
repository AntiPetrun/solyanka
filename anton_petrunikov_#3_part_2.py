from decimal import Decimal

gender, age = map(str, input('Enter your gender and age separated by a space: ').split())
weight, height = map(float, input('Enter your weight (kg) and body mass separated by a space: ').split())
bmi_index = round(Decimal(weight) / Decimal(height ** 2))
bmi_scale = '0' + '=' * (bmi_index - 1) + '|' + '=' * (49 - bmi_index) + '50'

underweight = ('Standart recomendations:\n\t'
    + '1. Eat more often\n\t'
    + '2. Eat nutrient-dense foods\n\t'
    + '3. Add calorie-dense snacks\n\t'
    + '4. Do exercise at home and outdoors\n\t'
    + '5. Organize regular sleep schedule\n\t'
)

normal_weight = ('Standart recomendations:\n\t'
    + '1. Keep going to eat often\n\t'
    + '2. Keep proper nutrition\n\t'
    + '3. Keep going eat nutrient-dense foods and calorie-dense snacks\n\t'
    + '4. Keep going do regular exercise\n\t'
    + '5. Keep proper nutrition\n\t'
    + '6. Keep regular sleep schedule\n\t'
)

overweight = ('Standart recomendations:\n\t'
    + '1. Boost your cooking skills\n\t'
    + '2. Eat more protein and more fiber\n\t'
    + '3. Try a probiotic\n\t'
    + '4. Get more sleep and reduce stress\n\t'
    + '5. Get more vitamin D\n\t'
    + '6. Serve food in multiple small portions, use a smaller plate and chew more\n\t'
    + '7. Cut out sugary beverages\n\t'
    + '8. Make snacks healthier\n\t'
    + '9. Do regular exercise\n\t'
)

obesity = ('Standart recomendations:\n\t'
    + '1. Healthy eating (choose a healthy diet)\n\t'
    + '2. Choose active lifestyles at home and outside\n\t'
    + '3. Get more sleep and reduce stress\n\t'
    + '4. Get more vitamins\n\t'
    + '5. Serve food in multiple small portions, use a smaller plate and chew more\n\t'
    + '6. Cut out sugary beverages\n\t'
    + '7. Make snacks healthier\n\t'
    + '8. Try to do regular exercise\n\t'
)

young = ('Bonus recomendations for young people:\n\t'
    + '1. Sit less and move more\n\t'
    + '2. Be active and spend more time outdoors\n\t'
    + '3. Make and follow a daily routine\n\t'
    + '4. Do more active sport'
)

avarage_age = ('Bonus recomendations for avarage age people:\n\t'
    + '1. Go outside\n\t'
    + '2. Hang out with friends'
    + '3. Have more sex'
    + '4. Be more like a vegetarian'
    + '5. Get health screenings and tests'
    + '6. Turn off your TV'
)

elder_people = ('Bonus recomendations for elder people:\n\t'
    + '1. Avoid risks\n\t'
    + '2. Lower your stress\n\t'
    + '3. Get health screenings and tests\n\t'
    + '4. Turn off your TV and go more outside\n\t'
    + '5. Find a passion or hobby\n\t'
    + '6. Daily walks with friends and acquaintances\n\t'
)

old_people = ('Bonus recomendations for old people:\n\t'
    + '1. Avoid risks\n\t'
    + '2. Lower your stress\n\t'
    + '3. Get health screenings and tests\n\t'
    + '4. Daily walks at home and outside\n\t'
    + '5. Find a passion or hobby\n\t'
    + '6. Hang out with friends, family or neighbors\n\t'
)

male = ('Extra recomendetions for male:\n\t'
    + '1. Do workout\n\t'
    + '2. Follow the daily routine and sleep\n\t'
    + '3. Have a regular sex\n\t'
    + '4. make and follow a diet\n\t' 
)

female = ('Extra recomendetions for female:\n\t'
    + '1. Follow the daily routine and sleep\n\t'
    + '2. Run and stretch\n\t'
    + '3. Have a regular sex\n\t'
    + '4. Make and follow a diet\n\t' 
)

if gender == 'male':
    if int(age) in range(18, 45):
        if bmi_index < 18.5:
            print(
                f'Your body mass index: {bmi_index} >>> Underweight!\n'
                + bmi_scale
                + f'\n\t{underweight}'
                + f'\n\t{male}'
                + f'\n\t{young}'
                )
        elif 18.5 <= bmi_index < 25:
            print(
                f'Your body mass index: {bmi_index} >>> Normal weight!\n'
                + bmi_scale
                + f'\n\t{normal_weight}'
                + f'\n\t{male}'
                + f'\n\t{young}'
                )
        elif 25<= bmi_index < 30:
            print(
                f'Your body mass index: {bmi_index} >>> Overweight!\n'
                + bmi_scale
                + f'\n\t{overweight}'
                + f'\n\t{male}'
                + f'\n\t{young}'
                )
        elif bmi_index > 40:
            print(
                f'Your body mass index: {bmi_index} >>> Obesity!\n'
                + bmi_scale
                + f'\n\t{obesity}'
                + f'\n\t{male}'
                + f'\n\t{young}'
                )
    elif int(age) in range(45, 60):
        if bmi_index < 18.5:
            print(
                f'Your body mass index: {bmi_index} >>> Underweight!\n'
                + bmi_scale
                + f'\n\t{underweight}'
                + f'\n\t{male}'
                + f'\n\t{avarage_age}'
                )
        elif 18.5 <= bmi_index < 25:
            print(
                f'Your body mass index: {bmi_index} >>> Normal weight!\n'
                + bmi_scale
                + f'\n\t{normal_weight}'
                + f'\n\t{male}'
                + f'\n\t{avarage_age}'
                )
        elif 25<= bmi_index < 30:
            print(
                f'Your body mass index: {bmi_index} >>> Overweight!\n'
                + bmi_scale
                + f'\n\t{overweight}'
                + f'\n\t{male}'
                + f'\n\t{avarage_age}'
                )
        elif bmi_index > 40:
            print(
                f'Your body mass index: {bmi_index} >>> Obesity!\n'
                + bmi_scale
                + f'\n\t{obesity}'
                + f'\n\t{male}'
                + f'\n\t{avarage_age}'
                )
    elif int(age) in range(60, 75):
        if bmi_index < 18.5:
            print(
                f'Your body mass index: {bmi_index} >>> Underweight!\n'
                + bmi_scale
                + f'\n\t{underweight}'
                + f'\n\t{male}'
                + f'\n\t{elder_people}'
                )
        elif 18.5 <= bmi_index < 25:
            print(
                f'Your body mass index: {bmi_index} >>> Normal weight!\n'
                + bmi_scale
                + f'\n\t{normal_weight}'
                + f'\n\t{male}'
                + f'\n\t{elder_people}'
                )
        elif 25<= bmi_index < 30:
            print(
                f'Your body mass index: {bmi_index} >>> Overweight!\n'
                + bmi_scale
                + f'\n\t{overweight}'
                + f'\n\t{male}'
                + f'\n\t{elder_people}'
                )
        elif bmi_index > 40:
            print(
                f'Your body mass index: {bmi_index} >>> Obesity!\n'
                + bmi_scale
                + f'\n\t{obesity}'
                + f'\n\t{male}'
                + f'\n\t{elder_people}'
                )
    elif int(age) in range(75, 90):
        if bmi_index < 18.5:
            print(
                f'Your body mass index: {bmi_index} >>> Underweight!\n'
                + bmi_scale
                + f'\n\t{underweight}'
                + f'\n\t{male}'
                + f'\n\t{old_people}'
                )
        elif 18.5 <= bmi_index < 25:
            print(
                f'Your body mass index: {bmi_index} >>> Normal weight!\n'
                + bmi_scale
                + f'\n\t{normal_weight}'
                + f'\n\t{male}'
                + f'\n\t{old_people}'
                )
        elif 25<= bmi_index < 30:
            print(
                f'Your body mass index: {bmi_index} >>> Overweight!\n'
                + bmi_scale
                + f'\n\t{overweight}'
                + f'\n\t{male}'
                + f'\n\t{old_people}'
                )
        elif bmi_index > 40:
            print(
                f'Your body mass index: {bmi_index} >>> Obesity!\n'
                + bmi_scale
                + f'\n\t{obesity}'
                + f'\n\t{male}'
                + f'\n\t{old_people}'
                )
elif gender == 'female':
    if int(age) in range(18, 45):
        if bmi_index < 18.5:
            print(
                f'Your body mass index: {bmi_index} >>> Underweight!\n'
                + bmi_scale
                + f'\n\t{underweight}'
                + f'\n\t{female}'
                + f'\n\t{young}'
                )
        elif 18.5 <= bmi_index < 25:
            print(
                f'Your body mass index: {bmi_index} >>> Normal weight!\n'
                + bmi_scale
                + f'\n\t{normal_weight}'
                + f'\n\t{female}'
                + f'\n\t{young}'
                )
        elif 25<= bmi_index < 30:
            print(
                f'Your body mass index: {bmi_index} >>> Overweight!\n'
                + bmi_scale
                + f'\n\t{overweight}'
                + f'\n\t{female}'
                + f'\n\t{young}'
                )
        elif bmi_index > 40:
            print(
                f'Your body mass index: {bmi_index} >>> Obesity!\n'
                + bmi_scale
                + f'\n\t{obesity}'
                + f'\n\t{female}'
                + f'\n\t{young}'
                )
    elif int(age) in range(45, 60):
        if bmi_index < 18.5:
            print(
                f'Your body mass index: {bmi_index} >>> Underweight!\n'
                + bmi_scale
                + f'\n\t{underweight}'
                + f'\n\t{female}'
                + f'\n\t{avarage_age}'
                )
        elif 18.5 <= bmi_index < 25:
            print(
                f'Your body mass index: {bmi_index} >>> Normal weight!\n'
                + bmi_scale
                + f'\n\t{normal_weight}'
                + f'\n\t{female}'
                + f'\n\t{avarage_age}'
                )
        elif 25<= bmi_index < 30:
            print(
                f'Your body mass index: {bmi_index} >>> Overweight!\n'
                + bmi_scale
                + f'\n\t{overweight}'
                + f'\n\t{female}'
                + f'\n\t{avarage_age}'
                )
        elif bmi_index > 40:
            print(
                f'Your body mass index: {bmi_index} >>> Obesity!\n'
                + bmi_scale
                + f'\n\t{obesity}'
                + f'\n\t{female}'
                + f'\n\t{avarage_age}'
                )
    elif int(age) in range(60, 75):
        if bmi_index < 18.5:
            print(
                f'Your body mass index: {bmi_index} >>> Underweight!\n'
                + bmi_scale
                + f'\n\t{underweight}'
                + f'\n\t{female}'
                + f'\n\t{elder_people}'
                )
        elif 18.5 <= bmi_index < 25:
            print(
                f'Your body mass index: {bmi_index} >>> Normal weight!\n'
                + bmi_scale
                + f'\n\t{normal_weight}'
                + f'\n\t{female}'
                + f'\n\t{elder_people}'
                )
        elif 25<= bmi_index < 30:
            print(
                f'Your body mass index: {bmi_index} >>> Overweight!\n'
                + bmi_scale
                + f'\n\t{overweight}'
                + f'\n\t{female}'
                + f'\n\t{elder_people}'
                )
        elif bmi_index > 40:
            print(
                f'Your body mass index: {bmi_index} >>> Obesity!\n'
                + bmi_scale
                + f'\n\t{obesity}'
                + f'\n\t{female}'
                + f'\n\t{elder_people}'
                )
    elif int(age) in range(75, 90):
        if bmi_index < 18.5:
            print(
                f'Your body mass index: {bmi_index} >>> Underweight!\n'
                + bmi_scale
                + f'\n\t{underweight}'
                + f'\n\t{female}'
                + f'\n\t{old_people}'
                )
        elif 18.5 <= bmi_index < 25:
            print(
                f'Your body mass index: {bmi_index} >>> Normal weight!\n'
                + bmi_scale
                + f'\n\t{normal_weight}'
                + f'\n\t{female}'
                + f'\n\t{old_people}'
                )
        elif 25<= bmi_index < 30:
            print(
                f'Your body mass index: {bmi_index} >>> Overweight!\n'
                + bmi_scale
                + f'\n\t{overweight}'
                + f'\n\t{female}'
                + f'\n\t{old_people}'
                )
        elif bmi_index > 40:
            print(
                f'Your body mass index: {bmi_index} >>> Obesity!\n'
                + bmi_scale
                + f'\n\t{obesity}'
                + f'\n\t{female}'
                + f'\n\t{old_people}'
                )
