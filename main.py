from mmpy_bot.bot import Bot
import re
from mmpy_bot.bot import listen_to
from mmpy_bot.bot import respond_to
from random import randint
from datetime import datetime
from mmpy_bot.scheduler import schedule

@respond_to('test 1 2')
def test(message):
    message.reply('Oui Allo ?')

@listen_to('\btintin', re.IGNORECASE)
def test(message):
    message.reply('Encore vous ?!')

@listen_to('barnabé', re.IGNORECASE)
def test(message):
    message.reply('Hahahahaha !')
@listen_to(r'\bart\b', re.IGNORECASE)
def test(message):
    message.reply("Il faut dire non à l'égoïsme artistique !")
@listen_to('RCVA$', re.IGNORECASE)
def test(message):
    message.reply('Sujet sensible...')
@listen_to(r'\btruche\b', re.IGNORECASE)
def test(message):
    message.reply('Taurine Cruche ?')
@listen_to('\btg$', re.IGNORECASE)
def test(message):
    message.reply("Ouais, ferme là un peu, on s'entend plus troller ici...")
@listen_to('\bdouc\b', re.IGNORECASE)
def test(message):
    message.reply('Never forget : http://www.allocine.fr/video/player_gen_cmedia=18851448&cfilm=125109.html')
@listen_to('\brm -rf\b', re.IGNORECASE)
def test(message):
    message.reply('À ta place, je ne ferai pas ça !')
@listen_to(r'\bjeanne\b', re.IGNORECASE)
def test(message):
    message.reply('Au secours !')
@listen_to(r'\bmagique\b', re.IGNORECASE)
def test(message):
    message.reply('https://pbs.twimg.com/profile_images/509033596804268032/FYSJikQw.jpeg')
@listen_to(r'\bimpossible\b', re.IGNORECASE)
def test(message):
    message.reply("Mais si, c'est possible, avec la carte Kiwi !")
@listen_to(r'\bsel\b', re.IGNORECASE)
def test(message):
    message.reply('https://i.imgur.com/MDtg8Ch.gif')
@listen_to(r'\bsuus\b', re.IGNORECASE)
def test(message):
    message.reply('SUUS !')
@listen_to(r'\bgay\b', re.IGNORECASE)
def test(message):
    message.reply('http://img11.hostingpics.net/pics/601949gay2.png')
@listen_to(r"\bn'est-ce pas\b", re.IGNORECASE)
def test(message):
    message.reply('https://i.imgur.com/cjHERMh.gif')
@listen_to(r'\bstar wars\b', re.IGNORECASE)
def test(message):
    message.reply('https://www.youtube.com/watch?v=VSpEo8Onqiw')
@listen_to(r'\bjul\b', re.IGNORECASE)
def test(message):
    message.reply('Wesh alors !')
    
@listen_to(r'\bphilippe\b', re.IGNORECASE)
def test(message):
    message.reply("Je sais où tu te caches ! Viens ici que ch'te bute enculé !")
@listen_to(r'\bmdr\b', re.IGNORECASE)
def test(message):
    message.reply("https://media.tenor.co/images/ba10f07355029341cb0f92f3ac1cec7b/tenor.gif")
@listen_to(r"\bj'ai pas compris\b", re.IGNORECASE)
def test(message):
    message.reply("http://trombi.tem-tsp.eu/photo.php?uid=gillet_f&h=320&w=240")
@listen_to(r'\brespect\b', re.IGNORECASE)
def test(message):
    message.reply("Le respect, je l'ai mangé.")
@listen_to(r'\btristesse\b', re.IGNORECASE)
def test(message):
    message.reply('http://gph.is/2ni6rjy')
@listen_to(r'\bmort de rire\b', re.IGNORECASE)
def test(message):
    message.reply('Mort de Reich NESPA !')
@listen_to(r'migration\b', re.IGNORECASE)
def test(message):
    message.reply('https://image.noelshack.com/fichiers/2017/39/4/1506611240-sqqsdsd.jpg')
@listen_to(r'communis', re.IGNORECASE)
def test(message):
    message.reply('Meurs, pourriture communiste !')
@listen_to(r'\bbluf', re.IGNORECASE)
def test(message):
    message.reply("Tu bluffes Martoni ! Ton arme n'est pas chargée !")
@listen_to(r'\bcomment est votre blanquette\b', re.IGNORECASE)
def test(message):
    message.reply('Elle est bonne.')
@listen_to(r'\bBK\b', re.IGNORECASE)
def test(message):
    message.reply('RTFW : Read The Fucking Wiki ! https://club-intech.minet.net/index.php/Codes_burger_king')
@listen_to(r'\bracis', re.IGNORECASE)
def test(message):
    message.reply('Votez Robert ! http://media.rtl.fr/cache/flas3kVAqKIKmrJq5axY-A/795v530-0/online/image/2015/1216/7780882999_robert-menard-lors-d-un-meeting-de-campagne-a-nimes-le-2-decembre.jpg')

def reply_random_quote(message):
    file = open('citations.txt', "r")
    citations = file.readlines()
    number = len(citations)
    rnum = int(randint(0, number)/2)
    content = citations[2*rnum]
    author = citations[2*rnum+1]
    response = '"'+content[:len(content)-3]+'"'+ "  -  " + author
    file.close()
    message.send(response)
    #TODO : trouver comment send vers general ou random
    #message.send(response, channel_id="town-square", files=None, props=None, pid='')
    

@respond_to('citation', re.IGNORECASE)
def reply_every_seconds(message):
    message.reply("Voici une citation : ");
    reply_random_quote(message)

quote_enabled=False
    
@listen_to('citation-auto', re.IGNORECASE)
def citation_auto(message):
    global quote_enabled
    if(quote_enabled==False):
        message.reply("Citations activées : une citation toute les 12 heures")
        schedule.every(12*3600).seconds.do(reply_random_quote, message)
        quote_enabled=True
    else:
        message.reply("Citations désactivées")
        schedule.clear()
        quote_enabled=False
    

@listen_to('stop-citation', re.IGNORECASE)
def cancel_jobs(message):
    schedule.clear()
    message.reply('Job arrêté')
    global quote_enabled
    quote_enabled=False

if __name__ == "__main__":
     
    Bot().run()

