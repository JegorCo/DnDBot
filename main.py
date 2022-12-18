import telebot
import config
from telebot import types
bot = telebot.TeleBot(config.TOKEN)
"""
Функция Распределяет модификаторы в зависимости от характериститик
"""
def modificator(skill):
    if skill <= 1:
        return -5
    elif skill >= 2 and skill <= 3:
        return -4
    elif skill >= 4 and skill <= 5:
        return -3
    elif skill >= 6 and skill <= 7:
        return -2
    elif skill >= 8 and skill <= 9:
        return -1
    elif skill >= 10 and skill <= 11:
        return 0
    elif skill >= 12 and skill <= 13:
        return 1
    elif skill >= 14 and skill <= 15:
        return 2
    elif skill >= 16 and skill <= 17:
        return 3
    elif skill >= 18 and skill <= 19:
        return 4
    elif skill >= 20 and skill <= 21:
        return 5
    elif skill >= 22 and skill <= 23:
        return 6
    elif skill >= 24 and skill <= 25:
        return 7
    elif skill >= 26 and skill <= 27:
        return 8
    elif skill >= 28 and skill <= 29:
        return 9
    elif skill == 30:
        return 10
"""
Класс, описывающий характеристики пресонажей
"""
class character:

    def __init__(self, name, race, klass, strength, dexterety, constitution, intellegence, wisdom, charisma):
        self.name = name #имя
        self.race = race #раса
        self.klass = klass #класс

        self.strength = strength #сила
        self.dexterety = dexterety #ловкость
        self.constitution = constitution #телосложение
        self.intellegence = intellegence #интеллект
        self.wisdom = wisdom #мудрость
        self.charisma = charisma #харизма

        self.arcana = modificator(intellegence)#анализ
        self.acrbatics = modificator(dexterety)#акробатка
        self.athletics = modificator(strength)#атлетика
        self.history = modificator(intellegence)#история
        self.investigation = modificator(intellegence)#магия
        self.nature = modificator(intellegence)#природа
        self.religion = modificator(intellegence)#религия
        self.animal = modificator(wisdom)#обращение с животными
        self.insight = modificator(wisdom)#пронициательность
        self.medicine = modificator(wisdom)#медицина
        self.perception = modificator(wisdom)#восприятие
        self.persuasion = modificator(charisma)#убеждение
        self.survival = modificator(wisdom)#выживание
        self.stealth = modificator(dexterety)#скрытность
        self.sleigh = modificator(dexterety)#ловкость рук
        self.deception = modificator(charisma)#обман
        self.intimidation = modificator(charisma)#запугивание
        self.performance = modificator(charisma)#выступление

"""
Создаём исключение
"""
class DemoException(Exception):
    def __init__(self, exept):
        super().__init__(exept)
exept = "Exception Triggered! Something went wrong."

"""
Функция, триггерит исключение, когда характеристика больше 30
"""
def triggerException(num):
    if (num > 30):
        raise DemoException(exept)
    else:
        return num

"""
Функция, триггерит исключение, когда характеристика меньше 0
"""
def triggerZero(num):
    if (num < 0):
        raise DemoException(exept)
    else:
        return num

"""Задаём начальные переменные"""
mycharacter = character("Null", "Null", "Null", 0, 0, 0, 0, 0, 0)#объявление характеристик персонажа
statusstregh = False#статус ввода персонажа: Сила
statusdexterty = False#статус ввода персонажа: Ловкость
statusconstitutions = False#статус ввода персонажа: Телосложение
statusintellegence = False#статус ввода персонажа: Интеллект
statuswisdom = False#статус ввода персонажа: Мудрость
statuscharisma = False#статус ввода персонажа: Харизма
flagrace = False#Проверка на то была ли введена раса
flagclass = False#Проверка на то был ли введён класс

"""
Команда start
"""
@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    """
    Объявляем inline кнопки для рас
    """
    global flagrace, flagclass, charactercreated
    flagclass = False
    flagrace = False
    charactercreated = False
    markup = types.InlineKeyboardMarkup(row_width = 1)
    gnome = types.InlineKeyboardButton("Гном", callback_data = 'gnome')
    ork = types.InlineKeyboardButton("Орк", callback_data='ork')
    human = types.InlineKeyboardButton("Человек", callback_data='human')
    elf = types.InlineKeyboardButton("Эльф", callback_data='elf')
    markup.add(gnome, ork, human, elf)
    bot.send_message(message.chat.id, "*Здравствуй игрок, добро пожаловать в прекрасный и опасный мир игры Dungeons & Dragons.* \n Для того чтобы начать своё приключение, вам предстоит создать персонажа. Перед тем как начинать создание персонажа, рекомендуем прочесть краткий экскурс по команде /raceinfo или /classinfo, для более подробной информации рекомендуем прочесть Книгу Игрока:https://www.dungeonsanddragons.ru/bookfull/5ed/5e%20Players%20Handbook%20-%20Книга%20игрока%20RUS.pdf, или сайт:https://dnd.su/ \nЧтобы начать создание персонажа выберите расу.".format(message.from_user), reply_markup=markup, parse_mode='Markdown')

    """
    Объявляем inline кнопки, и реакцию на их нажатие
    """
    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        global mycharacter
        mycharacter = character("Null", "Null", "Null", 0, 0, 0, 0, 0, 0)
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        bard = types.InlineKeyboardButton("🎵 Бард", callback_data='bard')
        barbarian = types.InlineKeyboardButton("🪓 Варвар", callback_data='barbarian')
        fighter = types.InlineKeyboardButton("⚔️ Воин", callback_data='fighter')
        wizard = types.InlineKeyboardButton("🔮 Волшебник", callback_data='wizard')
        markup1.add(bard, barbarian, fighter, wizard)

        contine = types.InlineKeyboardMarkup()
        tbc = types.InlineKeyboardButton("Продолжить", callback_data='tbc')
        contine.add(tbc)
        """Вводим расы"""
        if call.message:
            if call.data == 'gnome':
                global raca, strenh, dexerty, constituton, intelegenc, wisdon, harizma, flagrace, flagclass#временные переменные к характеристикам
                if (flagrace == False):
                    raca = "Гном"
                    strenh = 0
                    dexerty = 0
                    constituton = 0
                    intelegenc = 2
                    wisdon = 0
                    harizma = 0
                    flagrace = True
                    bot.send_message(call.message.chat.id, "Вы выбрали гнома, выберите класс", reply_markup=markup1)
                else:
                    bot.send_message(call.message.chat.id, "Ошибка, вы уже выбрали расу, нажмите /start чтобы начать создание персоажа заново")
            elif call.data == 'ork':
                if (flagrace == False):
                    raca = "Орк"
                    strenh = 2
                    dexerty = 0
                    constituton = 1
                    intelegenc = 2
                    wisdon = 0
                    harizma = 0
                    flagrace = True
                    bot.send_message(call.message.chat.id, "Вы выбрали орка, выберите класс", reply_markup=markup1)
                else:
                    bot.send_message(call.message.chat.id, "Ошибка, вы уже выбрали расу, нажмите /start чтобы начать создание персоажа заново")
            elif call.data == 'human':
                if (flagrace == False):
                    raca = "Человек"
                    strenh = 1
                    dexerty = 1
                    constituton = 1
                    intelegenc = 1
                    wisdon = 1
                    harizma = 1
                    flagrace = True
                    bot.send_message(call.message.chat.id, "Вы выбрали человека, выберите класс", reply_markup=markup1)
                else:
                    bot.send_message(call.message.chat.id, "Ошибка, вы уже выбрали расу, нажмите /start чтобы начать создание персоажа заново")
            elif call.data == 'elf':
                if(flagrace == False):
                    raca = "Эльф"
                    strenh = 0
                    dexerty = 2
                    constituton = 0
                    intelegenc = 0
                    wisdon = 0
                    harizma = 0
                    flagrace = True
                    bot.send_message(call.message.chat.id, "Вы выбрали эльфа, выберите класс", reply_markup=markup1)
                else:
                    bot.send_message(call.message.chat.id, "Ошибка, вы уже выбрали расу, нажмите /start чтобы начать создание персоажа заново")

            """
            Вводим классы
            """
            if call.data == 'bard':
                global klas, flagclass
                if flagclass == False:
                    klas = "Бард"
                    flagclass = True
                    bot.send_message(call.message.chat.id, "Вы выбрали барда, чтобы продолжить создание персонажа нажмите на кнопку, рекомендуем распределять характеристики следующими значениями: 15, 14, 13, 12, 10, 8", reply_markup=contine)
                else:
                    bot.send_message(call.message.chat.id, "Ошибка, вы уже выбрали класс, нажмите /start чтобы начать создание персоажа заново")

            elif call.data == 'barbarian':
                if flagclass == False:
                    klas = "Варвар"
                    bot.send_message(call.message.chat.id, "Вы выбрали варвара, чтобы продолжить создание персонажа нажмите на кнопку, рекомендуем распределять характеристики следующими значениями: 15, 14, 13, 12, 10, 8", reply_markup=contine)
                    flagclass = True
                else:
                    bot.send_message(call.message.chat.id, "Ошибка, вы уже выбрали класс, нажмите /start чтобы начать создание персоажа заново")
            elif call.data == 'fighter':
                if flagclass == False:
                    klas = "Воин"
                    bot.send_message(call.message.chat.id, "Вы выбрали воин, чтобы продолжить создание персонажа нажмите на кнопку, рекомендуем распределять характеристики следующими значениями: 15, 14, 13, 12, 10, 8", reply_markup=contine)
                    flagclass = True
                else:
                    bot.send_message(call.message.chat.id, "Ошибка, вы уже выбрали класс, нажмите /start чтобы начать создание персоажа заново")

            elif call.data == 'wizard':
                if flagclass == False:
                    klas = "Волшебник"
                    bot.send_message(call.message.chat.id, "Вы выбрали волшебника, чтобы продолжить создание персонажа нажмите на кнопку, рекомендуем распределять характеристики следующими значениями: 15, 14, 13, 12, 10, 8", reply_markup=contine)
                else:
                    bot.send_message(call.message.chat.id, "Ошибка, вы уже выбрали класс, нажмите /start чтобы начать создание персоажа заново")
            """Продолжение создания персонажа"""
            if call.data == 'tbc':
                mycharacter.race = raca
                mycharacter.klass = klas
                mycharacter.strength = strenh
                mycharacter.dexterety = dexerty
                mycharacter.constitution = constituton
                mycharacter.intellegence = intelegenc
                mycharacter.wisdom = wisdon
                mycharacter.charisma = harizma
                bot.send_message(call.message.chat.id, "Вы выбрали \nРаса: " + mycharacter.race + "\nКласс: " + mycharacter.klass)
                bot.send_message(call.message.chat.id, "Введите значение силы")
                """Статусы ввода характеристик"""
                global statusstregh, statusdexterty, statusconstitutions, statusintellegence, statuswisdom, statuscharisma
                statusstregh = True
                statusdexterty = False
                statusconstitutions = False
                statusintellegence = False
                statuswisdom = False
                statuscharisma = False


    """
    Команда /help, выводит список комад
    """
    @bot.message_handler(commands=['help'])
    def mesanger(message):
        bot.send_message(message.chat.id, "Список команд \n/start - начать создание персонажа(начать заново) \n/raceinfo - узнать информацио о расах \n/classinfo - узнать информацию о классах \n/characteristics - узнать характеристики персонажа \n/skills - узнать навыки персонажа")

    """
    Команда /raceinfo, выводит информацию о расах
    """
    @bot.message_handler(commands=['raceinfo'])
    def raceinfo(message):
        bot.send_message(message.chat.id, "Информация о расах: \n*Гномы* - Нескончаемый гул трудолюбия слышен там, где селятся сплочённые общества гномов. Гномы восторгаются жизнью, каждый миг наслаждаясь новым изобретением, открытием, исследованием, созиданием или шалостью. Значение интеллекта при создании увеличивается на 2 \n*Орки* - Дикие и бесстрашные племена орков всегда находятся в поисках эльфов, дварфов и людей, чтобы уничтожить их. Мотив их ненависти к цивилизованным расам мира и необходимость утоления требований богов продиктован верой, что, если орки будут хорошо сражаться и принесут славу своему племени. Значение силы при создании увеличивается на 2, значение телосложения увеличивается на 1\n*Люди* - В большинстве миров люди — это самая молодая из распространённых рас. Они поздно вышли на мировую сцену и живут намного меньше, чем дварфы, эльфы и драконы. Возможно, именно краткость их жизней заставляет их стремиться достигнуть как можно большего в отведённый им срок. Значение всех характеристик при создании увеличивается на 1\n*Эльфы* - это волшебный народ, обладающий неземным изяществом, живущий в мире, но не являющийся его частью. значение ловкости увеличивается на 2".format(message.from_user), parse_mode='Markdown')

    """
    Команда /classinfo, выводит информацию о классах(пока не работает)
    """
    @bot.message_handler(commands=['classinfo'])
    def classinfo(message):
        bot.send_message(message.chat.id, "Информация о классах")

    """
    Команда /characteristics, выводит характеристики персонажа
    """
    @bot.message_handler(commands=['characteristics'])
    def characteristics(message):
        if(charactercreated == True):
            bot.send_message(message.chat.id, "Характеристики:" + "\nРаса - " + mycharacter.race + "\nКласс - " + mycharacter.klass + "\nСила - " + str(mycharacter.strength) + "\nЛовкость - " + str(mycharacter.dexterety) + "\nТелосложение - " + str(mycharacter.constitution) + "\nИнтеллект - " + str(mycharacter.intellegence) + "\nМудрость - " + str(mycharacter.wisdom) + "\nХаризма - " + str(mycharacter.charisma))
        else:
            bot.send_message(message.chat.id, "вы ещё не создали персонажа")

    """
    Команда /skills, выводит навыки персонажа
    """
    @bot.message_handler(commands=['skills'])
    def characteristics(message):
        if (charactercreated == True):
            bot.send_message(message.chat.id, "Навыки:"  + "\nАнализ - " + str(mycharacter.arcana) + "\nАкробатика - " + str(mycharacter.acrbatics) + "\nАтлетика - " + str(mycharacter.athletics) + "\nИстория - " + str(mycharacter.history) + "\nМагия - " + str(mycharacter.investigation) + "\nПрирода - " + str(mycharacter.nature) + "\nРелигия - " + str(mycharacter.religion) + "\nОбращение с животными - " + str(mycharacter.animal) + "\nПронициательность - " + str(mycharacter.insight) + "\nМедецина - " + str(mycharacter.medicine) + "\nВосприятие - " + str(mycharacter.perception) + "\nУбеждение - " + str(mycharacter.persuasion) + "\nВыживание - " + str(mycharacter.survival) + "\nСкрытность - " + str(mycharacter.stealth) + "\nЛовкость рук - " + str(mycharacter.sleigh) + "\nОбман - " + str(mycharacter.deception) + "\nЗапугивание - " + str(mycharacter.intimidation) + "\nВыступление - " + str(mycharacter.performance))
        else:
            bot.send_message(message.chat.id, "вы ещё не создали персонажа")

    """
    Принимает текстовые сообщения
    """
    @bot.message_handler(content_types=['text'])
    def mesanger(message):

        global mycharacter, statusstregh, statusdexterty, statusconstitutions, statusintellegence, statuswisdom, statuscharisma
        """
        Ввод значаения силы
        """
        if(statusstregh == True):
            """
            Проверка ввода на корректность
            """
            try:
                triggerZero(int(message.text))
                triggerException(int(message.text) + mycharacter.strength)
                mycharacter.strength += int(message.text)
                mycharacter.athletics = modificator(mycharacter.strength)
            except ValueError:
                bot.send_message(message.chat.id, "Неверно введённое значение, пожалуйста введите число")
            except DemoException:
                bot.send_message(message.chat.id, "Значение характеристики не может превышать 30 и не может быть меньше 0, введите заново")
            else:
                """
                Изменение значения силы, переключение статуса на изменение ловкости
                """
                bot.send_message(message.chat.id, "Значение силы = " + str(mycharacter.strength))
                bot.send_message(message.chat.id, "Введите значение ловкости")
                statusstregh = False
                statusdexterty = True
            """
            Ввод значаения ловкости
            """
        elif(statusdexterty == True):
            try:
                triggerZero(int(message.text))
                triggerException(int(message.text) + mycharacter.dexterety)
                mycharacter.dexterety += int(message.text)
                mycharacter.acrbatics = modificator(mycharacter.dexterety)
                mycharacter.stealth = modificator(mycharacter.dexterety)
                mycharacter.sleigh = modificator(mycharacter.dexterety)
            except ValueError:
                bot.send_message(message.chat.id, "Неверно введённое значение, пожалуйста введите число")
            except DemoException:
                bot.send_message(message.chat.id, "Значение характеристики не может превышать 30 и не может быть меньше 0, введите заново")
            else:
                bot.send_message(message.chat.id, "Значение ловкости = " + str(mycharacter.dexterety))
                bot.send_message(message.chat.id, "Введите значение телосложения")
                statusdexterty = False
                statusconstitutions = True
            """
            Ввод значаения телосложения
            """
        elif(statusconstitutions == True):
            try:
                triggerZero(int(message.text))
                triggerException(int(message.text) + mycharacter.constitution)
                mycharacter.constitution += int(message.text)
                bot.send_message(message.chat.id, "Значение телосложения = " + str(mycharacter.constitution))
            except ValueError:
                bot.send_message(message.chat.id, "Неверно введённое значение, пожалуйста введите число")
            except DemoException:
                bot.send_message(message.chat.id, "Значение характеристики не может превышать 30 и не может быть меньше 0, введите заново")
            else:
                bot.send_message(message.chat.id, "Введите значение интеллекта")
                statusconstitutions = False
                statusintellegence = True
            """
            Ввод значаения интеллекта
            """

        elif (statusintellegence == True):
            try:
                triggerZero(int(message.text))
                triggerException(int(message.text) + mycharacter.intellegence)
                mycharacter.intellegence += int(message.text)
                mycharacter.arcana = modificator(mycharacter.intellegence)
                mycharacter.investigation = modificator(mycharacter.intellegence)
                mycharacter.nature = modificator(mycharacter.intellegence)
                mycharacter.history = modificator(mycharacter.intellegence)
                mycharacter.religion = modificator(mycharacter.intellegence)
            except ValueError:
                bot.send_message(message.chat.id, "Неверно введённое значение, пожалуйста введите число")
            except DemoException:
                bot.send_message(message.chat.id, "Значение характеристики не может превышать 30 и не может быть меньше 0, введите заново")
            else:
                bot.send_message(message.chat.id, "Значение интеллекта = " + str(mycharacter.intellegence))
                bot.send_message(message.chat.id, "Введите значение мудрости")
                statusintellegence = False
                statuswisdom = True
                """
                Ввод значаения мудрости
                """

        elif (statuswisdom == True):
            try:
                triggerZero(int(message.text))
                triggerException(int(message.text) + mycharacter.wisdom)
                mycharacter.wisdom += int(message.text)
                mycharacter.animal = modificator(mycharacter.wisdom)
                mycharacter.insight = modificator(mycharacter.wisdom)
                mycharacter.medicine = modificator(mycharacter.wisdom)
                mycharacter.perception = modificator(mycharacter.wisdom)
                mycharacter.survival = modificator(mycharacter.wisdom)
            except ValueError:
                bot.send_message(message.chat.id, "Неверно введённое значение, пожалуйста введите число")
            except DemoException:
                bot.send_message(message.chat.id, "Значение характеристики не может превышать 30 и не может быть меньше 0, введите заново")
            else:
                bot.send_message(message.chat.id, "Значение мудрости = " + str(mycharacter.wisdom))
                bot.send_message(message.chat.id, "Введите значение харизмы")
                statuswisdom = False
                statuscharisma = True
                """
                Ввод значаения харизмы
                """

        elif (statuscharisma == True):
            try:
                triggerZero(int(message.text))
                triggerException(int(message.text) + mycharacter.charisma)
                mycharacter.charisma += int(message.text)
                mycharacter.persuasion = modificator(mycharacter.charisma)
                mycharacter.deception = modificator(mycharacter.charisma)
                mycharacter.intimidation = modificator(mycharacter.charisma)
                mycharacter.performance = modificator(mycharacter.charisma)
            except ValueError:
                bot.send_message(message.chat.id, "Неверно введённое значение, пожалуйста введите число")
            except DemoException:
                bot.send_message(message.chat.id, "Значение характеристики не может превышать 30 и не может быть меньше 0, введите заново")
            else:
                global charactercreated
                bot.send_message(message.chat.id, "Значение харизмы = " + str(mycharacter.charisma))
                bot.send_message(message.chat.id, "Вы успешно создали персонажа, чтобы посмотреть характеристики введите команду /characteristics \nЧтобы посмотреть навыки введите команду /skills")
                statuscharisma = False
                charactercreated = True
                """
                Конец создания персонажа
                """
            """
            Обработка текстовых сообщений
            """

        else:
            bot.send_message(message.chat.id, "Неверное значение, список команд /help")


bot.polling(none_stop=True)