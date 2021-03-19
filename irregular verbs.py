'''
This is a program that defines the tense structure of a irregular verb.
Write the verb in the affirmative form!

Это программа, определяющая временную структуру неправильного глагола.
Напишите глагол в утвердительной форме!

EXAMPLE:
ПРИМЕР:
are/is/am becoming - Present Continuous,
was/were becoming - Past Continuous,
shall/will be becoming - Future Continuous,

become - Present Simple,
became - Past Simple,
shall/will become - Future Simple,

have/has become - Present Perfect,
had become - Past Perfect,
shall/will have become - Future Perfect,

have/has been becoming - Present Perfect Continuous,
had been becoming - Past Perfect Continuous,
shall/will have been becoming - Future Perfect Continuous
'''
import re
from sys import exit

verb = input()

all_form = ['read', 'set', 'cost', 'let', 'put', 'bid',
'cut', 'input', 'output', 'hit', 'cast', 'forecast',
'spread', 'wet', 'split', 'broadcast', 'bet',
'hurt', 'shut', 'quit', 'rid', 'shed', 'burst',
'knit', 'bust', 'thrust', 'slit']

first_form = ['have', 'get', 'find', 'buy', 'make', 'send', 'think', 'learn', 'say',
'sell', 'pay', 'light', 'keep', 'tell', 'meet', 'feel', 'speed', 'mean',
'build', 'leave', 'lead', 'win', 'deal', 'hold', 'feed', 'bring', 'string',
'hear', 'stand', 'dream', 'fight', 'sleep', 'spend', 'lose', 'seek',
'stick', 'slide', 'catch', 'sit', 'teach', 'strike', 'shoe', 'lay',
'burn', 'swing', 'shoot', 'spin', 'hang', 'bend', 'breed', 'dig', 'bind',
'smell', 'lean', 'shine', 'leap', 'spill', 'sweep', 'lend', 'sting',
'grind', 'wring', 'spit', 'dwell', 'bleed', 'creep', 'flee',
'sling', 'fling', 'gainsay', 'heave', 'rend', 'slink', 'spoil', 'weep',
'come', 'become', 'run', 'spell', 'see', 'take', 'give', 'write', 'drive',
'choose', 'fall', 'break', 'speak', 'rise', 'eat', 'beat', 'hide', 'ride',
'forget', 'wake', 'arise', 'shake', 'steal', 'bite', 'freeze',
'strive', 'forgive', 'awake', 'swell', 'forbid', 'weave', 'thrive', 'sew',
'tread', 'know', 'show', 'saw', 'blow', 'fly', 'grow', 'draw', 'throw',
'be', 'do', 'go', 'spring', 'ring', 'begin', 'bear', 'wear', 'drink',
'lie', 'sing', 'swim', 'sink', 'tear', 'bless', 'shrink', 'swear', 'stink']

second_form = ['had', 'got', 'found', 'bought', 'made', 'sent', 'thought',
'learnt', 'said', 'sold', 'paid', 'lit', 'kept', 'told', 'met', 'felt',
'sped', 'meant', 'built', 'left', 'led', 'won', 'dealt', 'held', 'fed',
'brought', 'strung', 'heard', 'stood', 'dreamt', 'fought', 'slept',
'spent', 'lost', 'sought', 'stuck', 'slid', 'caught', 'sat', 'taught',
'struck', 'shod', 'laid', 'burnt', 'swung', 'shot', 'spun', 'hung', 'bent',
'bred', 'dug', 'bound', 'smelt', 'leant', 'shone', 'leapt', 'spilt', 'swept',
'lent', 'stung', 'ground', 'wrung', 'spat', 'dwelt', 'bled', 'crept', 'fled',
'slung', 'flung', 'gainsaid', 'heaved', 'rent', 'slunk', 'spoilt', 'wept',
'came', 'became', 'ran', 'spelt', 'saw', 'took', 'gave', 'wrote', 'drove',
'chose', 'fell', 'broke', 'spoke', 'rose', 'ate', 'beat', 'hid', 'rode',
'forgot', 'woke', 'arose', 'shook', 'stole', 'bit', 'froze', 'strove',
'forgave', 'awoke', 'swelled', 'forbade', 'wove', 'throve', 'sewed', 'trod',
'knew', 'showed', 'sawed', 'blew', 'flew', 'grew', 'drew', 'threw',
'was', 'were', 'did', 'went', 'sprang', 'rang', 'began', 'bore',
'wore', 'drank', 'lay', 'sang', 'swam', 'sank', 'tore', 'blessed',
'shrank', 'swore', 'stank']

#Cheking Perfect Continuous
#Проверка Perfect Continuous

if (re.search(r'been', verb) and verb[-3:] = 'ing'):
	if (re.match(r'had', verb)):
		print('Past Perfect Continuous')
		exit()
	elif (re.match(r'will', verb) or re.match(r'shall', verb)):
		print('Future Perfect Continuous')
		exit()
	elif (re.match(r'have', verb) or re.match(r'has', verb)):
		print('Present Perfect Continuous')
		exit()
	else:
		print('Such a verb isn\'t possible. Check the spelling. \n Такой глагол невозможен. Проверьте написание.')
        
#Cheking Continuous
#Проверка Continuous

elif (verb[-3:] == 'ing'):
	if (re.match(r'was', verb) or re.match(r'were', verb)):
		print('Past Continuous')
		exit()
	elif (re.match(r'will', verb) or re.match(r'shall', verb)):
		print('Future Continuous')
		exit()
	elif (re.match(r'am', verb) or re.match(r'are', verb) or re.match(r'is', verb)):
		print('Present Continuous')
		exit()
	else:
		print('Such a verb isn\'t possible. Check the spelling. \nТакой глагол невозможен. Проверьте написание.')

#Cheking Perfect and Future Simple
#Проверка Perfect и Future Simple

elif (' ' in verb):
	if (re.match(r'had', verb)):
		print('Past Perfect')
		exit()
	elif ((re.match(r'will', verb) or re.match(r'shall', verb)) and re.search(r'have', verb)):
		print('Future Perfect')
		exit()
	elif (re.match(r'have', verb) or re.match(r'has', verb)):
		print('Present Perfect')
		exit()
	elif (re.match(r'will', verb) or re.match(r'shall', verb)):
		print('Future Simple')
		exit()
	else:
		print('Such a verb isn\'t possible. Check the spelling. \n Такой глагол невозможен. Проверьте написание.')

#Cheking Simple
#Проверка Simple

elif (' ' not in verb):
	if (verb in all_form):
		print('Present Simple / Past Simple')
		exit()
	elif (verb in first_form):
		print('Present Simple')
		exit()
	elif (verb in second_form):
		print('Past Simple')
		exit()
	else:
		print('Such a verb isn\'t possible. Check the spelling. \n Такой глагол невозможен. Проверьте написание.')