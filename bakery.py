# Клиент приходит в кондитерскую.
# Он хочет приобрести один или несколько видов продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах).
# Предложите выбор: 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке: С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке

s = {
    'торт': [('мука', 'сахар', 'яйца', 'сливки'), 100, 4000],
    'маффин': [('мука', 'шоколад', 'яйца'), 50, 1000],
    'бисквит': [('мука', 'яйца', 'банан'), 45, 2000]
}
while True:
    a = input('выбирайте продукт: торт, маффин, бисквит или приступить к покупке "s": ')
    if a == 's':
        break
    elif a not in s.keys():
        print('у нас нет такого продукта, выбирайте новый')
        continue
    b = int(input('что вы хотите посмотреть: описание(1), цену(2), количество(3), всю информацию(4): '))
    if b == 1:
        print(a, ':', (', '.join(s[a][0])))
    elif b == 4:
        print(a, ':', s[a])
    else:
        print(a, ':', s[a][b - 1])
sale = {}
while True:
    s1 = input('что будете покупать (торт, маффин, бисквит) или n для завершения: ')
    if s1 == 'n':
        break
    elif s1 not in s.keys():
        print('у нас нет такого продукта, выбирайте новый')
        continue
    c = int(input('сколько будете брать в граммах: '))
    if c > s[s1][2]:
        print('у нас нет такого количества, выбирайте снова')
        continue
    elif c <= s[s1][2]:
        c1 = c / 100 * s[s1][1]
        s[s1][2] -= c
        if s1 in sale.keys():
            sale[s1][0] += c1
            sale[s1][1] += c
        else:
            sale[s1] = [c1, c]
total = 0
for i in sale.values():
    total += i[0]
print('Вы добавили в корзину: ')
for key, values in sale.items():
    print(f'    {key}, общим весом {values[1]} г., на сумму {values[0]} руб.')
print(f'Итого к оплате: {total} руб.')
print('В продаже остались:')
for key, val in s.items():
    print(f'  {key} - {val[2]} г.')
