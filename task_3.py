print('Задача 3. Микроволновка')

# Мы разрабатываем микропрограмму — таймер обратного отсчёта для микроволновых печей.
# Некоторым пользователям не нравится пищащий звук.
# Есть задача убрать звук по готовности и заменить его сообщением на LED-экране.
# В нашем случае будем выводить в консоль сообщение с обратным отсчётом в секундах от reverse_timer до момента готовности,
# то есть 0 секунд, и спрашивать пользователя, готов ли он забрать еду.

# Пользователь в любой момент может прервать режим разогрева, введя «1»,
# то есть ответив «Да, еда готова».
# Тогда программа выведет на экран сообщение «Ваша еда готова, можете забрать» и покажет, на какой секунде был прерван таймер.
# Если пользователь ответит «0», что равноценно «Нет», то таймер уменьшится. Когда он достигнет 0 секунд, выводим сообщение «Ваша еда готова. Осторожно, горячo!».

# Напишите программу, которая выполняет обратный отсчёт таймера для микроволновой печи, учитывая описанные условия.

# Пример 1
# Введите время для обратного отсчёта (в секундах): 5
# Таймер установлен на 5 секунд.
# Осталось: 5 секунд
# Введите 1, если еда готова, или 0, чтобы продолжить: 0
# Осталось: 4 секунд
# Введите 1, если еда готова, или 0, чтобы продолжить: 0
# Осталось: 3 секунд
# Введите 1, если еда готова, или 0, чтобы продолжить: 1
# Ваша еда готова, можете забрать! Таймер был прерван на 3 секундах.

# Пример 2
# Введите время для обратного отсчёта (в секундах): 3
# Таймер установлен на 3 секунд.
# Осталось: 3 секунд
# Введите 1, если еда готова, или 0, чтобы продолжить: 0
# Осталось: 2 секунд
# Введите 1, если еда готова, или 0, чтобы продолжить: 0
# Осталось: 1 секунд
# Введите 1, если еда готова, или 0, чтобы продолжить: 0
# Ваша еда готова. Осторожно, горячo!