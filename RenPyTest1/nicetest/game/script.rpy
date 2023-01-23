# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Определяем переменные

# Счет игрока (количество правильных ответов)
define score = 0

# История начинается здесь
label start:  # (В процессе)/(Завершено)

    play music "audio/fonk_back.mp3"  # запускаем музыку

    scene bg room  # появляется сцена
    with fade  # затемнение при переходе

    show eileen happy  # появляется тетя

    e "Достаточно популярное мобильное приложение по доставке еды неожиданно стало терять пользователей."
    
    menu optional_name:
        "Что вы сделаете первым делом как аналитик в данной ситуации?"
        "Собрать обратную связь":
            jump feedback
        "Изучить конкурентов":
            jump competitor
        "Провести анализ приложения":
            jump analysisq
        


    return

# Сбор обратной связи
label feedback:  # 
    "tratata"
    "bum"
    return

# Изучение конкурентов
label competitor:  # 
    "Интерфейс приложения Яндекс.Доставка выглядит более современно, приложение легко ищется в плеймаркетах."
    menu optional_name2:
        "Какими будут дальнейшие шаги?"
        "Обновить дизайн приложения":
            $ score = score+1
        "Сделать страницу приложения более заметной в плеймаркетах":
            $ score = score+1
            jump playmarket
    return

# Анализ приложения
label analysis:  # 
    "xoba?        xoba? xoba?"

    return

# Сделать страницу приложения более заметной в плеймаркетах
label playmarket:  # 
    "xoba?"
    if score == 2:
        jump start
    if score == 1:
        jump feedback
    if score > 2:
        jump analysis


    return
    