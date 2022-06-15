#---------------------------- imports
import telebot
from telebot import types
import re
import funcs
import ipclass
import json
#---------------------------- token
bot_config_file = open("bot_config.json", encoding="utf-8") # opening bot_config.json
bot_config_dict: dict = json.loads(bot_config_file.read()) # extracting from json to dict
bot_config_file.close() # closing bot_config.json 
bot_token = bot_config_dict["token"] # token
bot = telebot.TeleBot(bot_token)
#---------------------------- globals
ip = ''
mask = ''
objofdata = ''
#---------------------------- functions 
def masks(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
    b1 = types.KeyboardButton("0.0.0.0")
    b2 = types.KeyboardButton("128.0.0.0")
    b3 = types.KeyboardButton("192.0.0.0")
    b4 = types.KeyboardButton("224.0.0.0")
    b5 = types.KeyboardButton("240.0.0.0")
    b6 = types.KeyboardButton("248.0.0.0")
    b7 = types.KeyboardButton("252.0.0.0")
    b8 = types.KeyboardButton("254.0.0.0")
    b9 = types.KeyboardButton("255.0.0.0")
    b10 = types.KeyboardButton("255.128.0.0")
    b11 = types.KeyboardButton("255.192.0.0")
    b12 = types.KeyboardButton("255.224.0.0")
    b13 = types.KeyboardButton("255.240.0.0")
    b14 = types.KeyboardButton("255.252.0.0")
    b15 = types.KeyboardButton("255.254.0.0")
    b16 = types.KeyboardButton("255.255.0.0")
    b17 = types.KeyboardButton("255.255.128.0")
    b18 = types.KeyboardButton("255.255.192.0")
    b19 = types.KeyboardButton("255.255.224.0")
    b20 = types.KeyboardButton("255.255.240.0")
    b21 = types.KeyboardButton("255.255.248.0")
    b22 = types.KeyboardButton("255.255.252.0")
    b23 = types.KeyboardButton("255.255.254.0")
    b24 = types.KeyboardButton("255.255.255.0")
    b25 = types.KeyboardButton("255.255.255.128")
    b26 = types.KeyboardButton("255.255.255.192")
    b27 = types.KeyboardButton("255.255.255.224")
    b28 = types.KeyboardButton("255.255.255.240")
    b29 = types.KeyboardButton("255.255.255.248")
    b30 = types.KeyboardButton("255.255.255.252")
    b31 = types.KeyboardButton("255.255.255.254")
    b32 = types.KeyboardButton("255.255.255.255")
    markup.add(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32)
    bot.send_message(msg.chat.id, '(можешь написать, а можешь выбрать)', parse_mode = 'html', reply_markup = markup)

def testip (newip):
    global ip
    newip = str(newip).split('.')
    for i in range(4):
        if int(newip[i]) > 255:
            return 0
    ip = '.'.join(newip)
    return 1

def testmask (testmask):
    if len(testmask) < 7 or len(testmask) > 15:
        return False
    global mask
    zero = 0
    testmask = testmask.split('.')
    for i in range(4):
        if int(testmask[i]) > 255:
            return False
    testmask = '.'.join(testmask)
    newmask = funcs.test(testmask).replace('.', '')
    count = 0
    if newmask[len(newmask) - 1] == '0':
        if newmask[0] == '0':
            zero = 32
        else:
            zero = 1
    elif newmask[len(newmask) - 1] == '1' and newmask[0] == '0':
        return False
    for i in range(len(newmask) - 1):
        if count == 0:
            if newmask[i] != newmask[i+1]:
                count = 1
        else:
            zero += 1
            if newmask[i] != newmask[i+1]:
                return False
    mask = zero
    return 1

def choice (message):
    global objofdata
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    b1 = types.KeyboardButton("бинарный ip")
    b2 = types.KeyboardButton("Максимальное количество компьютеров")
    b3 = types.KeyboardButton("ip сети")
    b4 = types.KeyboardButton("Номер в сети")
    b5 = types.KeyboardButton("широковещательный адрес")
    b6 = types.KeyboardButton("количество нулей в маске")
    b7 = types.KeyboardButton("все сразу")
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    bot.send_message(message.chat.id, 'Хорошо, теперь выбери то, что ты хочешь посчитать!', parse_mode = 'html', reply_markup = markup)
#---------------------------- commands
@bot.message_handler(commands = ['start'])
def start (msg):
    global ip, mask
    ip = mask = ''
    message = f'Привет, <b>{msg.from_user.full_name}</b>! Введи айпи и маску в десятичном виде, а я посчитаю то, что ты хочешь! Вот примеры, что бы тебе было удобнее: \n 12.12.12.12 255.255.254.0 или 12.12.12.12/24, или тоже самое, но разными сообщениями. На случай подсчета нового ip напиши /new'
    bot.send_message(msg.chat.id, message, parse_mode = 'html')

@bot.message_handler(commands = ['help'])
def help(msg):
    global ip, mask
    ip = mask = ''
    message = 'Введи айпи и маску в десятичном виде, а я посчитаю то, что ты хочешь! Вот примеры, что бы тебе было удобнее: \n 12.12.12.12 255.255.254.0 или 12.12.12.12/24, или тоже самое, но разными сообщениями. На случай подсчета нового ip напиши /new'
    bot.send_message(msg.chat.id, message, parse_mode = 'html')

@bot.message_handler(commands = ['new'])
def new (msg):
    global ip, mask
    ip = mask = ''
    bot.send_message(msg.chat.id, 'Хорошо, введи ip и маску, ты уже знаешь что делать', parse_mode = 'html')
#---------------------------- main code
@bot.message_handler()
def main (msg):
    global objofdata
    global ip
    global mask
    if msg.text.lower().strip() == 'привет':
        bot.send_message(msg.chat.id, 'И тебе привет!', parse_mode = 'html')
    elif ip == '':
        if msg.text.lower().strip() == "бинарный ip" or msg.text.lower().strip() == "максимальное количество компьютеров" or msg.text.lower().strip() == "ip сети" or msg.text.lower().strip() == "широковещательный адрес" or msg.text.lower().strip() == "количество нулей в маске" or msg.text.lower().strip() == "номер в сети" or msg.text.lower().strip() == "все сразу":
            bot.send_message(msg.chat.id, 'пока что рано, сначала введи ip-адрес и маску', parse_mode = 'html')
        elif re.sub('\d','', msg.text) == '...':
            if funcs.noerr(msg.text) == 0:
                bot.send_message(msg.chat.id, 'ip указан неправильно', parse_mode = 'html')
            elif testip(msg.text) == 0:
                bot.send_message(msg.chat.id, 'ip указан неправильно', parse_mode = 'html')
            else:
                bot.send_message(msg.chat.id, 'Хорошо, теперь маску', parse_mode = 'html')
                masks(msg)
        elif re.sub('\d','', msg.text) == '... ...':
            getip = msg.text.split(' ')[0]
            getmask = msg.text.split(' ')[1]
            if testip(getip) == 0 and testmask(getmask) == False:
                bot.send_message(msg.chat.id, 'ip и маска указаны неправильно', parse_mode = 'html')
            elif testip(getip) == 0:
                getip = ''
                bot.send_message(msg.chat.id, 'ip указан неправильно', parse_mode = 'html')
            elif testmask(getmask) == False:
                getmask = ''
                bot.send_message(msg.chat.id, 'маска указана неправильно', parse_mode = 'html')
            else:
                objofdata = ipclass.Ip(f'{ip}/{32 - mask}')
                choice(msg)
        elif re.sub('\d', '', msg.text).replace(' ', '') == '.../':
            getip = msg.text.replace(' ', '').split('/')[0]
            getmask = msg.text.replace(' ', '').split('/')[1]
            if funcs.noerr(getip) == 0:
                getip = getmask = mask = ip = ''
                bot.send_message(msg.chat.id, 'ip указан неправильно', parse_mode = 'html')
            elif testip(getip) == 0 and int(getmask) > 32:
                getip = getmask = mask = ip = ''
                bot.send_message(msg.chat.id, 'маска и ip указан неправильно', parse_mode = 'html')
            elif testip(getip) == 0:
                getip = getmask = mask = ip = ''    
                bot.send_message(msg.chat.id, 'ip указан неправильно', parse_mode = 'html')
            elif re.sub('\D', '', getmask) == '':
                getip = getmask = mask = ip = ''
                bot.send_message(msg.chat.id, 'маска указана неправильно', parse_mode = 'html')
            elif int(re.sub('\D', '', getmask)) > 32:
                getip = getmask = mask = ip = ''
                bot.send_message(msg.chat.id, 'маска указана неправильно', parse_mode = 'html')
            else:
                mask = 32 - int(getmask)
                objofdata = ipclass.Ip(f'{ip}/{32 - mask}')
                choice(msg)
        else:
            bot.send_message(msg.chat.id, 'Я тебя не понимаю', parse_mode = 'html')
    elif mask == '':
        if msg.text.lower().strip() == "бинарный ip" or msg.text.lower().strip() == "максимальное количество компьютеров" or msg.text.lower().strip() == "ip сети" or msg.text.lower().strip() == "широковещательный адрес" or msg.text.lower().strip() == "количество нулей в маске" or msg.text.lower().strip() == "номер в сети" or msg.text.lower().strip() == "все сразу":
            bot.send_message(msg.chat.id, 'пока что рано, сначала введи маску', parse_mode = 'html')
        elif re.sub('\d','', msg.text) == '...':
            if funcs.noerr(msg.text) == 0:
                bot.send_message(msg.chat.id, 'Маска указана неправильно', parse_mode = 'html')
            elif testmask(msg.text) == False:
                bot.send_message(msg.chat.id, 'Маска указана неправильно', parse_mode = 'html')
            else:
                objofdata = ipclass.Ip(f'{ip}/{32 - mask}')
                choice(msg)
        elif re.sub('\D', '', msg.text) == '':
            bot.send_message(msg.chat.id, 'Маска указана неправильно', parse_mode = 'html')
        elif int(re.sub('\D', '', msg.text)) > 32:
            bot.send_message(msg.chat.id, 'Маска указана неправильно', parse_mode = 'html')
        elif int(re.sub('\D', '', msg.text)) <= 32:
            mask = 32 - int(re.sub('\D', '', msg.text))
            objofdata = ipclass.Ip(f'{ip}/{mask}')
            choice(msg)
        else:
            bot.send_message(msg.chat.id, 'Я тебя не понимаю', parse_mode = 'html')
    else:
        if msg.text.lower().strip() == "бинарный ip":
            bot.send_message(msg.chat.id, f'бинарный ip: {objofdata.binip}', parse_mode = 'html')
        elif msg.text.lower().strip() == "максимальное количество компьютеров":
            bot.send_message(msg.chat.id, f'максимальное количество компьютеров: {objofdata.maxHosts}', parse_mode = 'html')
        elif msg.text.lower().strip() == "ip сети":
            bot.send_message(msg.chat.id, f'ip сети: {objofdata.ipOfLink}', parse_mode = 'html')
        elif msg.text.lower().strip() == "номер в сети":
            bot.send_message(msg.chat.id, f'номер в сети: {objofdata.numberInLink}', parse_mode = 'html')
        elif msg.text.lower().strip() == "широковещательный адрес":
            bot.send_message(msg.chat.id, f'широковещательный адрес: {objofdata.broadcastaAddress}', parse_mode = 'html')
        elif msg.text.lower().strip() == "количество нулей в маске":
            bot.send_message(msg.chat.id, f'количество нулей в маске: {objofdata.amoutOfZero}', parse_mode = 'html')
        elif msg.text.lower().strip() == "все сразу":
            mes = f'бинарный ip: {objofdata.binip} \n максимальное количество компьютеров: {objofdata.maxHosts} \n количество нулей в маске: {objofdata.amoutOfZero} \n ip сети: {objofdata.ipOfLink} \n номер в сети: {objofdata.numberInLink} \n широковещательный адрес: {objofdata.broadcastaAddress}'
            bot.send_message(msg.chat.id, mes, parse_mode = 'html')
        else:
            bot.send_message(msg.chat.id, 'Я тебя не понимаю', parse_mode = 'html')
#---------------------------- none_stop
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass



