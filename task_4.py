print('Задача 4. Функция')

# Перед изучением функций из программирования Саша решил освежить знания о функциях математики.
# Помогите Саше написать программу, которая будет считать значение функции в каждой точке отрезка с нужным шагом, начиная с конца.

# Напишите программу, которая получает на вход начало и конец отрезка, а также шаг (отрицательный),
# а затем высчитывает функцию y в каждой точке отрезка и выводит ответ на экран с нужным шагом, начиная с конца.

# Обратите внимание, что пользователь может ввести некорректные значения для диапазона или шага.
# Вам необходимо исправить эти значения таким образом, чтобы вывод результата не зависел от ошибочно введённых данных.

# Сама функция выглядит так: y = 𝑥³ + 2 ∙ 𝑥² - 4 ∙ x + 1

# ‌Пример 1
# Введите начало отрезка: −2
# Введите конец отрезка: 2
# Введите шаг: −1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке −1 функция равна 6
# В точке −2 функция равна 9

# ‌Пример 2 (пользователь ввёл некорректный шаг)
# Введите начало отрезка: 2
# Введите конец отрезка: −2
# Введите шаг: 1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке −1 функция равна 6
# В точке −2 функция равна 9

start = int(input("Введите начало отрезка: "))
stop = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))
if start < stop:
    stop, start = start, stop
if step > 0:
    step *= -1
for point in range(start, stop - 1, step):
    func = point**3 + 2 * point**2 - 4 * point + 1
    print("В точке", point, "функция равна", func)