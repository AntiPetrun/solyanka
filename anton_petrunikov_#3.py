first_num, sec_num, third_num = map(int, input().split())
print(first_num and sec_num and third_num and 'Нет нулевых значений!!!')
print(first_num or sec_num or third_num or 'Введены все нули!')

if first_num > (sec_num + third_num):
    print(first_num - sec_num - third_num)
elif first_num < (sec_num + third_num):
    print(sec_num + third_num - first_num)

if first_num > 50:
    if sec_num > first_num or third_num > first_num:
        print('Вася')
if first_num > 5 or sec_num == 7 and third_num == 7:
    print('Петя')
