import random
from config import token
import telebot
from telebot import types

bot = telebot.TeleBot(token)

hero = ""

def kub(message):
    x = random.randint(1, 6)
    return x

def game_over(message):
        heroes = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Волшебник")
        btn2 = types.KeyboardButton("Друид")
        btn3 = types.KeyboardButton("Варвар")
        btn4 = types.KeyboardButton("Плут")
        heroes.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id, "Ты проиграл!", reply_markup=heroes)
        bot.send_photo(message.chat.id, photo=open("Game/Start_PNG/Choose_hero.png", 'rb'))

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать игру")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Здарова, нажимай на кнопку", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def menu(message):
    if message.text == "Начать игру":
        heroes = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Волшебник")
        btn2 = types.KeyboardButton("Друид")
        btn3 = types.KeyboardButton("Варвар")
        btn4 = types.KeyboardButton("Плут")
        heroes.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id, "Выбери персонажа", reply_markup=heroes)
        bot.send_photo(message.chat.id, photo=open("Game/Start_PNG/Choose_hero.png", 'rb'))

    elif message.text == "Нет, не хочу":
        heroes = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Волшебник")
        btn2 = types.KeyboardButton("Друид")
        btn3 = types.KeyboardButton("Варвар")
        btn4 = types.KeyboardButton("Плут")
        heroes.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id, "Выбери персонажа", reply_markup=heroes)
        bot.send_photo(message.chat.id, photo=open("Game/Start_PNG/Choose_hero.png", 'rb'))
    # Ветка варвара
    elif message.text == "Варвар":
        approve = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Да, хочу стать варваром")
        btn2 = types.KeyboardButton("Нет, не хочу")
        approve.add(btn1, btn2)

        bot.send_message(message.chat.id, "Вы уверены, что хотите выбрать этого персонажа?", reply_markup=approve)
        bot.send_photo(message.chat.id, photo=open("Game/Barbarian/icons/Full.jpg", 'rb'))
        bot.send_photo(message.chat.id, photo=open("Game/Barbarian/icons/Token.png", 'rb'))

    elif message.text == "Да, хочу стать варваром":
        bot.send_message(message.chat.id, "Теперь ты варвар, поздравляю!")
        bot.send_message(message.chat.id, "Предисловие варвара")
        bot.send_photo(message.chat.id, photo=open("Game/Barbarian/akt_1/Chapter_1/Scene_1/images/1.0.png", 'rb'))

        scene_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 Подойти к бармену")
        btn2 = types.KeyboardButton("🪓 Пройтись и осмореть таверну")
        btn3 = types.KeyboardButton("🪓 Присесть за пустой столик")
        btn4 = types.KeyboardButton("🪓 Закричать 'Пидорасы!! ПАПОЧКА вернулся'")
        scene_1.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id, "Открывая дверь в таверну, вы ошушаете приятный запах еды и алкоголя. Где то слева играет бард, а перед тобой разворачивается приятная картина, За ближайшем столом происходи какой то ожесточенный спор, за столом подальше можешь заметить пару старых знакомых, они не оброщают на тебя внимания и о чем-то говорят. Бармен медленно потирает бокалы и разливает пиво по кружкам.", reply_markup=scene_1)

    elif message.text == "🪓 Подойти к бармену":
        bot.send_photo(message.chat.id, photo=open("Game/Barbarian/akt_1/Chapter_1/Scene_1/images/1.1.2.png", 'rb'))

        scene_1_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 Эль!")
        btn2 = types.KeyboardButton("🪓 Не, может че интересного происходит?")
        btn3 = types.KeyboardButton("🪓 Ты че падла не помнишь кто я?")
        scene_1_1.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id, "Подходя к бармену он кивает тебе и спрашивает 'Чего налить солага?'", reply_markup=scene_1_1)
    # Сцена 1.1.1
    elif message.text == "🪓 Эль!":
        bot.send_message(message.chat.id, "'Вот держи кружку и серебряк не забудь на стол положить'")

        # Сцена 2.1.1
        scene_2_1_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 Подойти к мужику и предложить побороться ?")
        btn2 = types.KeyboardButton("🪓 Посмотреть на борца и сказать 'Лучше бы сходил мешки потоскал а не бухал'")
        btn3 = types.KeyboardButton("🪓 Слышь здоровяк давай побросаем мечи?")
        scene_2_1_1.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         "Изрядно выпив ты начинаешь наслождаться музыкой и в какой то момент ты замечаешь сильного мужика за столом. Ты вспоминаешь что он чемпион по армреслингу.",
                         reply_markup=scene_2_1_1)


    # Сцена 1.1.2
    elif message.text == "🪓 Не, может че интересного происходит?":
        bot.send_message(message.chat.id, "Ну ничего интересного еще не было, может хочешь мечи побросать?")

        # Сцена 2.1.2
        scene_2_1_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 А твоя мать как, говорят она до сих по 100 мужиков за день обслуживает?")
        btn2 = types.KeyboardButton("🪓 Отлично а ты как ? может выпьем ?")
        btn3 = types.KeyboardButton("🪓 Да пошли вы, я лучше напьюсь чем с вами общаться буду")
        scene_2_1_2.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         "Подходя к мишени ты вынимаешь пару кинжалов и начинаешь их метать, твоя голова чиста а руки не дрожат ты с легкостью втыкаешь пару кинжалов в центр. Как в друг слышишь 'Кифа, где ты пропадал тысячу лет тебя не видели, давай к нам выпьем по кружечке Грога'",
                         reply_markup=scene_2_1_2)

    # Сцена 1.1.3
    elif message.text == "🪓 Ты че падла не помнишь кто я?":
        bot.send_message(message.chat.id, "Парни тут какой то мусор сидит выбросьте его на улицу!!") # (тут идет битва с чуваком который сидит за вторым столом от входа ближе всего к углу))
        kubik = kub(message)
        if kubik < 3:
            game_over(message)
        else:
            # Сцена 2.1.3
            scene_2_1_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🪓 Так то лучше а то всего декаду не появляся а уже забыли.")
            btn2 = types.KeyboardButton("🪓 Тото же, а если продолжишь залупаться то и ты получешь.")
            btn3 = types.KeyboardButton("🪓 Ну все пизда всем я разозлился!")
            scene_2_1_3.add(btn1, btn2, btn3)

            bot.send_message(message.chat.id,
                             "После парочки точных ударов ты отправляешь паренька в накаут бармен разводит руками и говорит 'Не признал Кифа, Эль за наш счет'",
                             reply_markup=scene_2_1_3)


    # Сцена 1.2
    elif message.text == "🪓 Пройтись и осмореть таверну":
        bot.send_photo(message.chat.id, photo=open("Game/Barbarian/akt_1/Chapter_1/Scene_1/images/1.2.2.png", 'rb'))

        scene_1_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 Подойти к бармену")
        btn2 = types.KeyboardButton("🪓 Присесть за пустой столик")
        btn3 = types.KeyboardButton("🪓 Закричать 'Пидорасы!! ПАПОЧКА вернулся'")
        scene_1_2.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id, "Пройдясь по таверне вы замечаете еще парочку столов они стоят отдельно ото всех и по всей видимости более приватные, за одни столом эльфы с картой, за другим же  пара богатеньких мужиков играющих в карты.'", reply_markup=scene_1_2)



    # Сцена 1.3
    elif message.text == "🪓 Присесть за пустой столик":
        bot.send_photo(message.chat.id, photo=open("Game/Barbarian/akt_1/Chapter_1/Scene_1/images/1.3.2.png", 'rb'))

        scene_1_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 А что такое грог ?")
        btn2 = types.KeyboardButton("🪓 Да давай парася и кружку эля да по крепче")
        btn3 = types.KeyboardButton("🪓 Неси все и побыстрее")
        scene_1_3.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id, "Присаживаясь за ближайший стол вы видите как к вам подходит официантка и спрашивает что желаете покушать?  а может быть и выпить? так же у нас проходит акциия выпей 10 кружек грога и не проблюйся", reply_markup=scene_1_3)


    # Сцена 2.3.1
    elif message.text == "🪓 А что такое грог ?":
        bot.send_message(message.chat.id, "Грог - это напиток орков он очень ванюч и крепок")
        scene_2_3_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 Да, пожалуй")
        btn2 = types.KeyboardButton("🪓 Не грог это слишком давай лучше эль и похлебку")
        btn3 = types.KeyboardButton("🪓 Я вообще не голоден, может у вас тут слухи какие ходят?")
        scene_2_3_1.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id, "Вам принести грог или может еще и курочку возьмете ?", reply_markup=scene_2_3_1)

    # Сцена 2.3.2
    elif message.text == "🪓 Да давай парася и кружку эля да по крепче":
        bot.send_message(message.chat.id, "Как скажете, будет готово минут через 10, пока еда готовиться вы можете пометать ножи")

        scene_2_3_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 Бросить пару кинжалов в мишень")
        btn2 = types.KeyboardButton("🪓 Вновь окинуть взглядом таверну и крикнуть 'Есть тут кто то с яйцами?, может мечи побросаем.'")
        btn3 = types.KeyboardButton("🪓 Эй блять! есть тут кто нибудь сильный я поборотьсся хочу")
        scene_2_3_2.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Кивнув вам, она уходит на кухню. Осматрев таверну вы замечаете за своей спиной доску для метания ножей", reply_markup=scene_2_3_2)
    # Сцена 2.3.3
    elif message.text == "🪓 Неси все и побыстрее":
        bot.send_message(message.chat.id, "Как скажите но деньги в перед")
        scene_2_3_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 У меня сейчас нет денег")
        btn2 = types.KeyboardButton("🪓 Сейчас могу дать 2 зм. и когда все пренесете еще 8зм.")
        btn3 = types.KeyboardButton("🪓 Ты че овца тащи жратву я потом расплачусь")
        scene_2_3_3.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Вы осматриваете свои карманы и находите всего 2 зм.", reply_markup=scene_2_3_3)

    # Сцена 1.4
    elif message.text == "🪓 Закричать 'Пидорасы!! ПАПОЧКА вернулся'":
        bot.send_photo(message.chat.id, photo=open("Game/Barbarian/akt_1/Chapter_1/Scene_1/images/1.4.2.png", 'rb'))

        scene_1_4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 А твоя мать как, говорят она до сих по 100 мужиков за день обсуживает?")
        btn2 = types.KeyboardButton("🪓 А не ахуел ли ты ЧМО!!")
        btn3 = types.KeyboardButton("🪓 Закрой рот и налей мне Грога!")
        scene_1_4.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id, "Ты замечаешь на себе почти все взгляды в таверне, при чем некоторые из людей уже хотят что то выкрикнуть тебе в ответ как вдруг один из давних знакомых встает и кричит 'Грог сколько лет сколько зим, как ты ? как мать? ахах'", reply_markup=scene_1_4)

    # Сцена 1.4.1
    elif message.text == "🪓 А твоя мать как, говорят она до сих по 100 мужиков за день обсуживает?":
        kubik = kub(message)
        bot.send_message(message.chat.id, "'Ты че офигел, щас я тоби захуярю'")
        if kubik < 3:
            game_over(message)
        # Сцена 2.4.1
        else:
            scene_2_4_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🪓 Тото же сучка! если еще кто залупнеться на меня так же зубы собирать будет!")
            btn2 = types.KeyboardButton("🪓 Били ты бы себя поберек а то уже как мать твоя")
            btn3 = types.KeyboardButton("🪓 Ладно парень, хватит с тебя. Присаживаясь за стол ты берешь кружку Били и падаешь на стул")
            scene_2_4_1.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, "Пара точных ударов и твой давний знакомый собирает зубы с пола",
                             reply_markup=scene_2_4_1)

    # Сцена 1.4.2
    elif message.text == "🪓 А не ахуел ли ты ЧМО!!" or message.text == "🪓 Че за чмыри расскажи по подробнее" or message.text == "🪓 Ладно парень, хватит с тебя. Присаживаясь за стол ты берешь кружку Били и падаешь на стул":
        if message.text == "🪓 А не ахуел ли ты ЧМО!!":
            bot.send_message(message.chat.id, "Все все не ори, садись лучше выпий, мы кстати тут такое нашли закочаешься")
        elif message.text == "🪓 Ладно парень, хватит с тебя. Присаживаясь за стол ты берешь кружку Били и падаешь на стул":
            bot.send_message(message.chat.id, "Такс 'Кифа' дело есть мы тут с парнями собрались группу идиотов отпинать. Они тут местных чмырят")
        else:
            pass
        # Сцена 2.4.2
        scene_2_4_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 Да парни я с вами. Начистим им ебальнички, тогда давайте завтра утром тут за этим столом и соберемся")
        btn2 = types.KeyboardButton("🪓 Ну парни если денег на платят то я против.")
        btn3 = types.KeyboardButton("🪓 Я за но для начала пусть Били извиниться и вы тоже а то сидите а хари как у свиней!!!")
        scene_2_4_2.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Носят красные плащи и постоянно деньги тресут с местных, говорят они в поместье заброшенном ошиваются", reply_markup=scene_2_4_2)

    # Сцена 1.4.3
    elif message.text == "🪓 Закрой рот и налей мне Грога!":
        bot.send_message(message.chat.id, "Как скажешь, но в следуюущий рай повежлевее со мной")
        # Сцена 2.4.3
        scene_2_4_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 Че за чмыри расскажи по подробнее")
        btn2 = types.KeyboardButton("🪓 Не парни я че то перебрал пойду пожалуй спать.")
        btn3 = types.KeyboardButton("🪓 Парни давайте завтра утром тут встретимся и все обговарим а то башка совсем не варит. Я пойду лучше бабу найду.")
        scene_2_4_3.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Изрядно выпив Грога тебя чуть пошатывает а в глазах двоиться, один из седящих рядом с тобой говорит. 'Кифа' тут парочка чмырей есть надо их отпинать.", reply_markup=scene_2_4_3)

#####################

    # Сцена 3.1.1
    elif message.text == "🪓 Подойти к мужику и предложить побороться":
        bot.send_message(message.chat.id, "")

    # Сцена 3.1.2
    elif message.text == "🪓 Посмотреть на борца и сказать 'Лучше бы сходил мешки потоскал а не бухал'":
        bot.send_message(message.chat.id, "Ты ловишь на себе лукавый взгляд 'Может пометаем мечи раз ты так в себе уверен ?'")

        scene_3_1_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🪓 А твоя мать как, говорят она до сих по 100 мужиков за день обслуживает?")
        btn2 = types.KeyboardButton("🪓 Отлично а ты как ? может выпьем ?")
        btn3 = types.KeyboardButton("🪓 Да пошли вы, я лучше напьюсь чем с вами общаться буду")
        scene_3_1_2.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id,
                         "Подходя к мишени ты вынимаешь пару кинжалов и начинаешь их метать, мечи летят криво и ты не попадаешь. Как в друг слышишь 'Кифа, как ты, где ты пропадал, тысячу лет тебя не видели, давай к нам выпьем по кружечке Грога'",
                         reply_markup=scene_3_1_2)

    # Сцена 2.4.3
    elif message.text == "🪓 Слышь здоровяк давай побросаем мечи?":
        bot.send_message(message.chat.id, "Да давай!")
    elif message.text == "🪓 Не парни я че то перебрал пойду пожалуй спать.":
        bot.send_message(message.chat.id, "Вы пытаеть встать, это дается вам с трудом но вы идете пройдя пару столов ваши ноги слабеют а вы садитесь за ближайший стол и засыпаете.")
        game_over(message)
    elif message.text == "🪓 Подойти к мужику и предложить побороться":
        bot.send_message(message.chat.id, "Вставая из за стола вы оглядываетесь тут полно народа но вот девок почти нет, а за барной стойкой сидит 'Джек' он задолжал вам денег и явно не собирался их возвращать.")


    elif message.text == "🪓 Да парни я с вами. Начистим им ебальнички, тогда давайте завтра утром тут за этим столом и соберемся":
        bot.send_message(message.chat.id, "Как скажешь 'Кифа' и свою сикиру не забудь.")
    elif message.text == "🪓 Ну парни если денег на платят то я против.":
        bot.send_message(message.chat.id, "Не Кифа, это от доброй души, ну как хочешь. Мы то думали ты настояший мужик эх...")
    elif message.text == "🪓 Я за но для начала пусть Били извиниться и вы тоже а то сидите а хари как у свиней!!!":
        bot.send_message(message.chat.id, "Парни он че ахуел пиздем его")
        kubik = kub(message)
        if kubik <= 5:
            game_over(message)
        else:
            bot.send_message(message.chat.id, "Красава")

    elif message.text == "🪓 Парни давайте завтра утром тут встретимся и все обговарим а то башка совсем не варит. Я пойду лучше бабу найду.":
        bot.send_message(message.chat.id, "Вставая из за стола вы оглядываетесь тут полно народа но вот девок почти нет, а за барной стойкой сидит 'Джек' он задолжал вам денег и явно не собирался их возвращать.")

bot.polling(0)