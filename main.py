#Это Пиздабот, лучшее что придумало человечество. Работает в ВК, надо иметь под рукой это https://vk.com/dev/manuals
#по всем вопросам, как ниже написано, blnb yf[eq
#или сюда: @marksista

import vk_api
import random
import pickle
import time           
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id


f = open('token.txt', 'r')
tocen = f.read()
vk_session = vk_api.VkApi(token=tocen)                                                                              #загрузка токена VK API
longpoll = VkBotLongPoll(vk_session, '203496582')
f.close()


def write_message(chat, msg):
    vk_session.method('messages.send', {'peer_id': chat, 'message': msg, 'random_id': get_random_id()})             #для краткости метод отправки сообщения я определил так. Сообщение может включать в себя другие данные, подробнее в док-ии и ниже


def send_att(peer_id, att, freq):
    random.seed()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
    print('[',time_string,'] отправил в',peer_id, att)
    #if random.randint(0, 10) < freq[peer_id]:
        #vk_session.method('messages.send', {'peer_id': peer_id, 'attachment': att, 'random_id': get_random_id()})
    try:
        if random.randint(0, 10) < freq[peer_id]:
            vk_session.method('messages.send', {'peer_id': peer_id, 'attachment': att, 'random_id': get_random_id()})                                                                          
    except:
        vk_session.method('messages.send', {'peer_id': peer_id, 'attachment': att, 'random_id': get_random_id()})


def rply(peer_id, from_id, tekst, freq):
    random.seed()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
    print('[',time_string,']',from_id,"написал в",peer_id, tekst)
    #if freq[peer_id] is None:
     #   write_message(peer_id, tekst)
    try:
        if random.randint(0, 10) < freq[peer_id]:
            write_message(peer_id, tekst)                                                                           #блок if отвечает за шанс ракции на сообщние, что и хранится в словаре. если значения нет реагировать всегда
    except:
        write_message(peer_id, tekst)

def frequency(peer_id, from_id, freq):
    write_message(peer_id, "Тишина! Слушаю")
    temp_id = peer_id
    for event in longpoll.listen():
        if (event.type == VkBotEventType.MESSAGE_NEW and peer_id == temp_id and (
                event.message.text == "10" or event.message.text == "9" or event.message.text == "8" or event.message.text == "7" or event.message.text == "6" or event.message.text == "5" or event.message.text == "4" or event.message.text == "3" or event.message.text == "2" or event.message.text == "1")):
            freq[peer_id] = int(event.message.text)
            with open('freq.pickle', 'wb') as f:
                pickle.dump(freq, f)                                                                            #picle.dump сохраняет словарь значений частот в отдельный файл, чтобы при перезапуске ничего не слетало
            write_message(peer_id, "Cumming настроен")
        break
    print(from_id, "\tизменил частоту в\t", peer_id, "на", freq[peer_id])

#def tiktok(peer_id, from_id, freq):
          #  freq[peer_id] = int(event.message.text)
         #   with open('tt.pickle', 'wb') as f:
         #       pickle.dump(tiktok, f)                                                                            #picle.dump сохраняет словарь значений частот в отдельный файл, чтобы при перезапуске ничего не слетало
       #     write_message(peer_id, "Cumming настроен")
      #  break
  #  print(from_id, "\tизменил частоту в\t", peer_id, "на", freq[peer_id])

def sticker (peer_id, from_id, sticker_id):
    vk_session.method('messages.send',{'peer_id':peer_id,'sticker_id':sticker_id,'random_id':get_random_id()})
    print('отправил', sticker_id,'в', peer_id, from_id)                                                         #отправить стикер
def main():
    random.seed()

    freq = {}
    pik_video = ["video-203496582_456239017", "video-203496582_456239018"]
    pidor = ["пидора ответ)", "Пидора ответ)))0)", "педика ответ)"]
    cum = ["video-182584800_456239255","audio119515759_456240061","video-174907607_456241137", "video120599552_456239758", "video-155545674_456239357", "video-203496582_456239021", "video-203496582_456239022", "video-203496582_456239023", "video-154906069_456241392", "photo-203496582_457239290"
           "video-182584800_456239075", "video293505844_456240298", "video-189326537_456239453", "video-203496582_456239025", "video-154906069_456241993", "video-182584800_456239293", "video-190538111_456239106", "video-190538111_456239082", "video-182584800_456239079", "video-167123504_456244267"
           "audio2000256743_456244121", "video-184856829_456241383", "video540023085_456239123","video-203665610_456239018", "video-191974153_456239220","video-197421230_456239068", "video-161692375_456241639", "video-184586643_456239052", "video215229116_456242111", "video444751303_456239453",
           "video488925639_456239295", "video-161692375_456241674", "video-186330400_456239092", "video-187572210_456239892", "video276765818_456239519", "video-161692375_456241623", "video-147324244_456240159", "video-187572210_456239716",
           "video-184856829_456242432", "video-187193451_456240230", "video396495620_456239664", "video-165055094_456239558"]
    #tiktok = {}
    privet = ["Пукни в пакет", "Сделай минет", "Получи в еблет"]
    anecdotes = ["В Ереванское КБ приезжает японская делегация. Главный инженер-армянин рассказывает:"
    " \n — Вот тут у нас сидят 8 инженеров, вот тут 12, вот тут 16."
    "\n Японец:"
    "\n — А у нас на весь завод приходится всего 7 инженеров!"
    "\nДелегация уезжает, главный инженер задумчиво идёт домой, задумчиво ужинает, ложится в кровать, ворочается полночи и думает:"
    "\n— Ну шесть понятно. А с кем седьмой в нарды играет?!","Играют как - то армянин и еврей в нарды, еврей спрашивает армянина:"
    "\n– Почему вы, играя со мной в нарды, всегда выигрываете?"
    "\n– Потому что вы всегда проигрываете.",
    "Один армянин очень любил ржать с мемов и назвал сына Орик.",
    "Армянин решил баллотироваться в рейхстаг. У Гиммлера:"
    "\n- Род деятельности?"
    "\n- Машинист"
    "\n- Возраст?"
    "\n- 35 лет"
    "\n- Национальность?"
    "\n- Армянин"
    "\n- Характер?"
    "\n- Нордический",
    "Армянин-модник назвал своего сына Шарфик",
    "Eдут в купе русский, украинец, армянин. Проходит полчаса, надо знакомиться. Хохол протягивает руку, говорит:"
    "\n- Мыкола, запорожец."
    "\n- Сергей, москвич."
    "\n- Ашот, BМW.",
    "Два армянина, инвалида-колясочника едут по пустыне. Видят лампу. Один из них натирает её. Появляется джинн и говорит: «У вас одно желание на двоих»."
    "Те в один голос: «Хотим ходить». Джинн подумал и говорит: «Ну так как у вас одно желание на двоих, то ходить будете по очереди!». Ну и дал им нарды",
    "Как будут звать сына армянина, работающего в клубе? \n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n .\n . Барменчик",
    "В армянском детском саду воспитательница отчитывает мальчика: — Амасик, ты опять небритым пришёл?",
    "У памятника:"
    "\n— Ай, какой красивый армянин! Совсем молодой умер!"
    "\n— Ну что вы, это же Пушкин, русский поэт!"
    "\n— Какой Пушкин, какой русский!? Не видишь — надпись: ГАЗОН ЗАСЕЯН.",
    "В Армении даже автомат по выдаче билетиков в метро немного торгуется",
    "— Почему армяне не становятся космонавтами?"
    "\n Потому что шашлык не помещается в тюбике.",
    "Был у нас армянин - Канат. сидим сдаём экзамен, у каждого своя задача. И тут с конца аудитории раздаётся хохот, все спрашивают:"
    "\n— В чём дело?"
    "\n— Те, кто ещё не сполз под парту говорит: задача 67. \n— Задача 67. На" "столе лежит канат, конец свисает на 3 метра...",
    "\n— На необитаемом острове армян, грузин и русский находят пещеру. Жребий идти на разведку выпадает армянину. Он заходит внутрь и попадает в лапы циклопу, который из масленки капает в задний прход гостю и голубит пришельца. Оставшиеся снаружи слышат крик своего спутника, армянин через какое-то время появляется снаружи. Русский и грузин:"
    "\n — Что случилось? Армянин:"
    "\n — Там племя каких-то амазонок, полуголые все, красииивые!"
    "\n — А че кричал?"
    "\n — Так то от неожиданности. Парочку обслужил уже. Вот отлучился вас позвать. Грузин оказался менее доверчивым, а русский рванул в пещеру. В пещере та же картина: циклоп, масленка, серия гомосексуальных актов. Оставшиеся снаружи слышат крик русского. Армян ехидно улыбается. Грузин в недоумении. Появляется русский. Грузин к нему:"
    "\n — Ну что?"
    "\n — Да кайф, дружище, я че так быстро: только с зоны откинулся — бабы давно не было. И побежал грузин в пещеру. Из пещеры доносятся страшные крики, вопли, проклятия и матюки. Армянин говорит:"
    "\n — Да! Тяжело нашему брату — грузину!! Русский:"
    "\n — Да уж тяжелее, чем нам — я у циклопа масленку украл!",
    "\n — Приехал армянин после долгого отсутствия на родину...."
    "\n — Стоит на горе... Кругом природа... Красота... Он поднял голову и говорит:"
    "\n — И небо все то же..."
    "\n — Глубоко вздохнул...:"
    "\n — И воздух все тот же...."
    "\n — Наклонился за цветком:"
    "\n — И цветы все те же...."
    "\n — Вдруг, чувствует, что его сзади кто-то имеет...:"
    "\n — Ой! И люди все те же....",
    "\n Если Грузия объединится с Арменией, то новая страна будет называться: Giorgio Armani.",
    "\n Интим по телефону в Армении:"
    "\n — Алло, это интим по телефону?"
    "\n— Да, брат...",
    "Армен очень переживал из-за обильной растительности на своем теле. Особенно его огорчал папоротник."
    "\n– Сколько нужно времени, чтобы научиться играть в нарды?"
    "\n– Это зависит от наличия у вас таланта, воли, сообразительности."
    "\n – А если у меня нет этих качеств?"
    "\n – Пять минут.",
    " Поезд. Купе на три спальных места. На верхнем русский, посредине армянин, внизу грузин. Стало грузину скучно. Призадумался, чем бы поразвлечься, поднатужился, да как пернет! Двое бедолаг свесились с полок и в один голос вопрошают:"
    "\n — Эй, генацвале! Ты что творишь?!"
    "\n — Один—ноль в пользу 'Динамо' Тбилиси!"
    "\n Тут армянин напрягся и выдал дважды, да так, что свет померк."
    "\n — Ай—яй, ара, вай, как нехорошо!"
    "\n — Два—один в пользу 'Арарат' Ереван!"
    "\n Русский, не долго думая, достал свой конец и давай поливать нижних. Те вопят:"
    "\n — Ты, что, кацо, зачем так нехорошо делаешь?!"
    "\n — Несмотря на проливной дождь, матч продолжается!",
    "\n — Может ли забеременеть мужчина?"
    "\n — Над этой проблемой ведется работа в Армении. Пока положительных результатов нет.",
    "Армянин решил баллотироваться в горсовет. В регистратуре:"
    "\n - Род деятельности?"
    "\n - Машинист"
    "\n - Возраст?"
    "\n - 35 лет"
    "\n - Национальность?"
    "\n - Армянин"
    "\n - Партия?"
    "\n - Давайте",
    "Армянин решил баллотироваться в горсовет. В регистратуре:"
    "\n - Род деятельности?"
    "\n - Машинист"
    "\n - Возраст?"
    "\n - 35 лет"
    "\n - Национальность?"
    "\n - Армянин"
    "\n - Партия?"
    "\n - Давайте"
    "\n - Еще партия?"
    "\n - Давайте"
    "\n - Еще партия?"
    "\n - Давайте"
    "\n - Еще партия?"
    "\n - Давайте"
    "\n - Еще партия?"
    "\n - Давайте"
    "\n - Еще партия?"
    "\n - Давайте"
    "\n - Еще партия?"
    "\n - Давайте на обед схожу и сыграем.",
    "Армянин решил баллотироваться в горсовет. В регистратуре:"
    "\n -Веган?"
    "\n -Да."
    "\n -Генератор три блина, средний крутит...?"
    "\n -Сам себя."
    "\n -Шляпу есть где повесить?"
    "\n -Негде."
    "\n -Попу мыл?"
    "\n -Да."
    "\n Регистратор смеется так неприятно и гасит свечку.",
    "Армянин нетрадиционной ориентации играет в шашки.",
    "Армянская семья так любила извиняться, что взяла фамилию Сорян",
    "- Как зовут армянина-трубача?"
    "\n - Арагорн!",
    "Едут в поезде армянин, немец и русский. Ну, едут и едут. Ничего не происходит. Потому что Россия — единая многонациональная страна.",
    "Вопрос Армянскому радио:"
    "\n — Можно ли заниматься сексом с открытым окном?"
    "\n Армянское радио отвечает:"
    "\n — Можно, но лучше с женщиной.",
    "Знаете, почему в Мире армян больше, чем орков? Потому что в отличие от орков, размножающихся спорами, армяне размножаются Диаспорами!",
    "Армянский программист назвал сына Трафиком.",
    "Когда я работала в колл-центре, к нам иногда подсаживали стажеров. Девочкам достались девочки, а Игорь выторговал себе единственного мальчика-армянина. Прохожу мимо них и вижу склоненные головы и неистовый шепот. Прячусь за шкаф, до меня доносится:"
    "\n - Если хочешь выглядеть преуспевающим, у меня есть один секрет. Ты решил работать в смену 2/2? Прекрасно! Тогда тебе достаточно двух разных пиджаков. В первую смену надеваешь один, во вторую - второй, за выходные все забывают в чем ты был, и можешь опять надевать первый."
    "\n Чуть позже я отозвала Игоря в сторонку:"
    "\n - Серьезно? Пиджаки?"
    "\n - Света, мы же оба с тобой понимаем, что на работе главное казаться успешным."
    "\n Спустя несколько лет, Игорь нашел меня в ВК. На аватарке он был очень серьезен и в бурке. Пишет:"
    "\n - Привет!"
    "\n - Привет!"
    "\n - Нарды хочешь купить?",
    "Как-то раз я приехал на чемпионат Армении по нардам, а там армяне в нарды играют.",
    "Одна армянская семья так любила Линукс, что назвала сына Дебя́н.",
    "नूह ने सन्दूक बनाया, और वह और वह और उसके परिवार और दास और दास"
    "\n और उसके परिवार और उसने हवा के पक्षियों और रेंगने वाले चीजों और हर प्राणियों को जोड़ों में ले लिया।"
    "\n और आकाश खुल गया और सब मर गया, और केवल सन्दूक पर तैरता रहा"
    "\n लहरों ... और नूह ने एक कबूतर जारी किया, और वह जैतून की एक शाखा के साथ वापस आ गया। और"
    "\n नूह समझ गया कि यहोवा अपने दिल में दयालु था, और शुष्क भूमि प्रकट हुई थी।"
    "\n और"
    "सन्दूक अरारत में आया, और नूह ने जानवरों को छोड़ दिया। और पहाड़ पर, आर्मेनियाई बैकगैमौन खेलते हैं। एक दूसरे से कहता है:"
    "\n - अरे, देखो, सर्कस आ गया है!",
    "Пошел как-то русский с армянином в душ. Русский с собой взял мочало, гель для душа и шампунь.А армянин взял расчёску и 3 шампуня. Русский армянина спрашивает:"
    "\n - Ара, а зачем тебе так много шампуня?"
    "\n А армянин ему и отвечает"
    "\n - Как зачем, брат? Чтобы волосы были чистые и шелковистые."
    ]
    print("Загрузка...")
    
    with open('freq.pickle', 'rb') as f:
        freq = pickle.load(f)
    for key, value in freq.items():
        print(key, ":", value)
    print("Всё готово!")
    
    while True:                                                                                                 #на самом деле while true не нужен, потому что for event in longpoll.listen(): сам по себе бесконечный цикл
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                msg_txt = event.message.text
                msg_txt = msg_txt.lower()
                peer_id = event.message.peer_id
                from_id = event.message.from_id
                #print(event.message)
                if msg_txt == "да" or msg_txt == "да!" or msg_txt == "да?" or msg_txt == "lf":
                    rply(peer_id, event.message.from_id, "Пизда!", freq)
                elif msg_txt == "нет":
                    rply(peer_id, event.message.from_id, random.choice(pidor), freq)
                elif msg_txt == "пизда" or msg_txt == "пизда!":
                    rply(peer_id, event.message.from_id, "Да", freq)
                elif ("шлюхи аргумент" in msg_txt):
                    rply(peer_id, from_id, "Аргумент не нужен, пидор обнаружен", freq)
                elif msg_txt == "настроить частоту":
                    frequency(peer_id, event.message.from_id, freq)
                elif msg_txt == "где" or msg_txt == "где?":
                    rply(peer_id, event.message.from_id, "В пизде!", freq)
                elif "cum" in msg_txt:
                    send_att(peer_id, random.choice(cum), freq)
                elif "спасибо папаша" in msg_txt:
                    rply(peer_id, event.message.from_id, "за этот рено логан чёрного цвета 20 века?", freq)
                elif ("алё" in msg_txt):
                    rply(peer_id, from_id, "Да-да?", freq)
                elif ("как там с деньгами" in msg_txt):
                    rply(peer_id, from_id, "С какими деньгами?", freq)
                elif ("да да" in msg_txt):
                    rply(peer_id, from_id, "Ну как там с деньгами?", freq)
                elif ("ну как там с деньгами?" in msg_txt):
                    rply(peer_id, from_id, "А?", freq, )
                elif ("которые я вложил" in msg_txt):
                    rply(peer_id, from_id, "Куда вложил", freq)
                elif ("а?" == msg_txt):
                    rply(peer_id, from_id, "Как с деньгами-то там?", freq)
                elif ("а" == msg_txt):
                    rply(peer_id, from_id, "Хуй на!", freq)
                elif ("справедливо" in msg_txt):
                    sticker (peer_id, from_id, 163)
                elif ("ладно" in msg_txt):
                    rply(peer_id, event.message.from_id, "текст", freq)
                elif ("иди нахуй" in msg_txt):
                    rply(peer_id, from_id, "кусай за хуй", freq)
                elif ("справедливо" in msg_txt or "справебыдло" in msg_txt):
                    sticker (peer_id, from_id, 163)
                elif ("опа" == msg_txt or "опа!" == msg_txt):
                    rply(peer_id, from_id, "Жопа!", freq)
                elif ("барановичи" in msg_txt):
                    send_att(peer_id, 'audio96628634_456239019', freq)
                elif ("девять" in msg_txt or "9" == msg_txt):
                    rply(peer_id, from_id, "чи десять", freq)
                elif ("десят" in msg_txt):
                    rply(peer_id, from_id, "чи девять", freq)
                elif ("алло" == msg_txt):
                    rply(peer_id, from_id, "Хуем по лбу не дало?", freq)
                elif ("прощай" == msg_txt):
                    rply(peer_id, from_id, "Хуем провращай", freq)
                elif ("привет" == msg_txt):
                    rply(peer_id, from_id, random.choice(privet), freq)
                elif (("бауманка" in msg_txt) or ("мгту" in msg_txt) or ("бомонка" in msg_txt)):
                    if (random.randint(0, 10) < 4):
                        rply(peer_id, from_id, "то есть вы хотели сказать \n \n МОСКОВСКИЙ ГОСУДАРСТВЕННЫЙ ОРДЕНА КРАСНОГО ТРУДОВОГО ЗНАМЕНИ,"
                             " ОРДЕНА ВЛАДИМИРА ИЛЬИЧА ЛЕНИНА, ОРДЕНА ВЕЛИКОЙ ОКТЯБРЬСКОЙ РЕВОЛЮЦИИ ТЫСЯЧА ДЕВЯТЬСОТ СЕМНАДЦАТОГО ГОДА"
                             " ТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ ИМЕНИ ВЕЛИКОГО ГЕРОЯ-РЕВОЛЮЦИОНЕРА НИКОЛАЯ ЭРНЕСТОВИЧА БАУМАНА ПРЕДАТЕЛЬСКИ УБИТОГО"
                             "31 ОКТЯБРЯ 1905 ГОДА ОСКОЛКОМ ТРУБЫ ДЛИНОЙ 26 СМ ДИАМЕТРОМ ПОЛТОРА ДЮЙМА КУПЛЕННОЙ ЗА 5 ГРИВЕН СЛУЖИТЕЛЕМ ЦАРСКОЙ ОХРАНКИ ХАБИБУЛИНЫМ"
                             "НА ПЕРЕСЕЧЕНИИ ДАНИИЛОВСКОЙ И НЕНЕЦКОЙ (ныне - Бауманской) УЛИЦЫ ВО ВРЕМЯ РАБОЧЕ-КРЕСТЬЯНСКОГО ВОССТАНИЯ", freq)
                elif ("её величество елизавета" in msg_txt):
                    rply(peer_id, from_id, "Её Величество Елизавета II, Божией Милостью Королева Антигуа и Барбуда, Королева Содружества Багамских островов, Королева Барбадоса, Королева Белиза, Соединённого Королевства, Канады и Королева, "
                         "Глава Содружества, Защитница Веры, Королева Соединённого Королевства Великобритании и Северной Ирландии, и Гренады, Королева Ямайки, Королева Святого Кристофера и Невиса, Королева Санта-Лючии, Королева Сент-Винсента и Гренадин,"
                         "Герцогиня Нормандская, Владетельница Мэна, Королева Австралии, Королева Новой Зеландии, Королева Папуа — Новой Гвинеи, Королева Соломоновых Островов, Королева Тувалу, и Её иных Царств и Территорий, Глава Содружества, Мать всего народа,"
                         "Леди Королева, Адмирал Елизавета, Верховный Вождь Фиджи, Белая цапля, Темавелтище, Главнокомандующий Канадскими Вооружёнными Силами, Главнокомандующий Сил Обороны Новой Зеландии, Главнокомандующий Британскими Вооружёнными Силами,"
                         "Капитан-генерал Королевского полка Австралийской Артиллерии, Шеф Королевских Австралийских Инженеров, Шеф Королевского Австралийского Корпуса Пехоты, Шеф Королевского Австралийского Корпуса Тылового Обеспечения, Шеф Королевского"
                         "Австралийского Медицинского Корпуса, Шеф Австралийских Гражданских Воздушных Сил, Шеф Шодерийского пехотного полка, Шеф 48-го полка Канадской горной пехоты, Шеф Аргилльского и Сазерландского полка горной пехоты принцессы Луизы,"
                         "Капитан-генерал полка Королевской Канадской Артиллерии, Шеф Генерал-губернаторской конной гвардии, Шеф Собственного королевского полка Калгари, Шеф Королевского 22-го полка, Шеф Генерал-губернаторской пешей гвардии, Шеф Канадской гренадерской"
                         "гвардии, Шеф Канадской гвардии, Шеф Королевского Нью-Брунсвикского полка, Шеф военных инженеров, Шеф горной пехоты Калгари, Почётный комиссионер Королевской канадской конной полиции, Капитан-генерал полка Королевской Новозеландской Артиллерии,"
                         "Капитан-генерал Королевского Новозеландского бронетанкового корпуса, Шеф Королевского Новозеландского инженерного корпуса, Шеф Королевского Новозеландского пехотного полка, Шеф Территориальных Воздушных Сил Новой Зеландии, Почётный бригадир"
                         "женского королевского армейского корпуса, Шеф Конной гвардии, Шеф гвардейских гренадеров, Шеф Колдстримских гвардейцев, Шеф Шотландских гвардейцев, Шеф Ирландских гвардейцев, Шеф Валлийских гвардейцев, Капитан-генерал Королевского артиллерийского"
                         "полка, Шеф Корпуса Королевских Инженеров, Шеф Почётного артиллерийского отряда, Шеф Королевского танкового полка, Капитан-генерал молодёжной организации Министерства Обороны Великобритании, Объединённых Кадетских Сил, Почётный полковник"
                         "Собственных Королевских Уорвикширских и Уочестерширских Йоменов, Шеф Малавийских стрелков, почетный гражданин Виндзора и Мэйденхэда, Стерлинга, Лондона, Эдинбурга, Кардиффа, Белфаста, Филадельфии, почётный член Почтенной компании драпировщиков,"
                         "Института Гражданского строительства, Английского королевского хирургического колледжа, почётный бакалавр музыки и гражданского права", freq)
                elif ("men power" in msg_txt):
                    rply(peer_id, from_id, "♂", freq)
                elif ("что" == msg_txt or "что?" == msg_txt):
                    send_att(peer_id, "audio430223397_456239762", freq)
                elif ("id чата срочно" == msg_txt):
                    rply(peer_id, from_id, peer_id, freq)
                elif ("кокос" in msg_txt or "аристократ" in msg_txt or "эстет" in msg_txt):
                    sticker (peer_id, from_id, 131)
                elif ("армяне" == msg_txt):
                    rply(peer_id, from_id, random.choice(anecdotes), freq)
                elif ("темавелт" in msg_txt):
                    send_att(peer_id, "video-203496582_456239024", freq)
                    #    elif ("ебать за тикток: да" == msg_txt):
                    
            #    elif ("tiktok.com" in msg_txt):
                #    try:
                  #      if
                  #      vk_session.method('messages.delete', {'peer_id': peer_id, 'delete_for_all':1, 'conversation_message_ids':event.message.conversation_message_id, 'random_id': get_random_id()})
                  #  rply(peer_id, from_id, "За тикток тут ебут!", freq)
                
                    
                
                #elif event.message.attachments is not None:
                 #   if 'sticker' in event.message.attachments[0]["type"]:
                  #      if event.message.attachments['sticker']['sticker_id'] == 163:
                   #         sticker (peer_id, from_id, 163)
                            
                elif peer_id == 2000000003 or peer_id == 2000000017 or peer_id == 2000000002:                                                                                 #локальные мемы
                    if " пик " in msg_txt or msg_txt == "пик":
                        send_att(peer_id, random.choice(pik_video), freq)
                    elif "714" in msg_txt:
                        send_att(peer_id, "photo-203496582_457239030", freq)
                    elif "народное ополчение" in msg_txt:
                        rply(peer_id, from_id, "Нет, блин, Карамышевская", freq)
                    elif "карамышевская" in msg_txt:
                        rply(peer_id, from_id, "Нет, блин, Народное ополчение", freq)
                    elif "говно" in msg_txt:
                        rply(peer_id, from_id, "Скорее Нива Тревел", freq)
                    elif ("нива" in msg_txt):
                        send_att(peer_id, "video-203496582_456239019", freq)
                    elif ("нива тревел" in msg_txt):
                        send_att(peer_id, "video-203496582_456239019", freq)
                    elif ("кубик" in msg_txt):
                        send_att(peer_id, "video-203496582_456239026", freq)
                elif event.message.action is not None:                                                                      #приветсвенное сообщение при добавлении в беседу
                    print(event.message.action)
                    if event.message.action["type"] == "chat_invite_user" and event.message.action["member_id"] == -203496582:
                        write_message(peer_id,
                                      "Вершина программисткой мысли у вас в чате! Чтобы настроить шанс ответов (чтобы он не задолбал вас)"
                                      "напишите «Настроить частоту», отправьте, и после этого цифру от 1 до 10 (10 - реагировать всегда, 1 - шанс ответа 10%). По всем "
                                      "предложениям и вопросам ничего не делать, *marksista (я) оч ленивый. Чтобы вызвать это сообщение, напишите «Помощь» \n\n Не забудьте выдать боту доступ к всей переписке!")
                        print("Бота добавили в беседу", peer_id)
                        freq[peer_id] = 10
                    #elif event.message.action["type"] == "chat_kick_user" and event.message.action["member_id"] == 0:
                        #if freq.get(peer_id) is not None:
                            #del freq[peer_id]
                        #print("Бота удалили из беседы", peer_id)
                elif msg_txt == "помощь":
                    write_message(peer_id,
                                  "Вершина программисткой мысли у вас в чате! Чтобы настроить шанс ответа "
                                  "напишите «Настроить частоту» и после этого цифру от 1 до 10 (10 - реагировать всегда, 1 - шанс ответа 10%). По всем предложениям "
                                  "ничего не делать, *marksista (я) оч ленивый.\n\n Не забудьте выдать боту доступ к всей переписке!")


if __name__ == '__main__':
    main()
