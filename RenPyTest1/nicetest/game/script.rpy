# Определение персонажей игры.
define boss = Character('Руководитель', color="#E60E20")
define analyst = Character('Аналитик', colo="#0000FF")

#Набор очков
define score = 0

# Начало игры:
label start:
    play music "audio/fonk_back.mp3" #запускаем музыку

    scene office
    show director with dissolve

    boss "Достаточно популярное мобильное приложение по доставке еды неожиданно
    стало терять пользователей."
    extend "Надо исправлять положение! Что делать в данной ситуации?"

    hide director with moveoutright

    menu:
        "Что делать?"

        "Сбор обратной связи от пользователей":
            jump feedback

        "Изучение конкурентов":
            jump competitors

        "Аналитика приложения":
            jump analysis

    return

label feedback:
    scene office
    show director3 with dissolve

    $ score += 2

    boss "Каким образом будет осуществляться обратная связь?"

    menu:
        "Какой функционал добавим в приложение?"

        "Расскажите, как сделать приложение лучше?":
            jump improve

        "Пожалуйста, оцените приложение по шкале от 1 до 5!":
            jump estimate

        "Функция 'Сообщить об ошибке'":
            jump bug
    return

label competitors:
    scene office
    show director3 with dissolve

    $ score += 1

    boss "Интерфейс приложения Яндекс.Доставка выглядит более современно, приложение легко ищется в плеймаркетах. Какими будут дальнейшие шаги?"
    return

label analysis:
    scene office
    show director3 with dissolve

    $ score += 1

    boss "Давайте подумаем, какие данные могут пригодиться для анализа?"
    return

label improve:
    "Пользователь оставил следующий комментарий: Хотелось бы иметь возможность формировать корзину заказов в оффлайн режиме."
    menu:
        "Какими будут ваши дальнейшие действия?"

        "Такое требование реализовать невозможно":
        "Было бы полезно включить этот функционал в приложение":
        "Это можно реализовать, но не стоит тратить ресурсы разработки ради одного клиента":
    return


label estiamte:

label bug:
