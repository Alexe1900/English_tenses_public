'''
This is a program that defines the tense structure of a regular verb.
Write the verb in the affirmative form!

Это программа, определяющая временную структуру правильного глагола.
Напишите глагол в утвердительной форме!

EXAMPLE:
ПРИМЕР:
are/is/am working - Present Continuous,
was/were working - Past Continuous,
shall/will be working - Future Continuous,

work - Present Simple,
worked - Past Simple,
shall/will work - Future Simple,

have/has worked - Present Perfect,
had worked - Past Perfect,
shall/will have worked - Future Perfect,

have/has been working - Present Perfect Continuous,
had been working - Past Perfect Continuous,
shall/will have been working - Future Perfect Continuous
'''

import re
from sys import exit

verb = input()

#Cheking Perfect Continuous
#Проверка Perfect Continuous

if (re.search(r'been', verb) and verb[-3:] == 'ing'):
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

#Verb-exception "need"
#Глагол-исключение "need"

if (verb == 'will need' or verb == 'shall need'):
	print('Future Simple')
	exit()

#Cheking Perfect
#Проверка Perfect

elif (' ' in verb and verb[-2:] == 'ed'):
	if (re.match(r'had', verb)):
		print('Past Perfect')
		exit()
	elif (re.match(r'will', verb) or re.match(r'shall', verb)):
		print('Future Perfect')
		exit()
	elif (re.match(r'have', verb) or re.match(r'has', verb)):
		print('Present Perfect')
		exit()
	else:
		print('Such a verb isn\'t possible. Check the spelling. \n Такой глагол невозможен. Проверьте написание.')

#Cheking Simple
#Проверка Simple

elif ((not ' ' in verb) and (verb[-2:] == 'ed') and (verb != 'need')):
	print('Past Simple')
	exit()
elif (not ' ' in verb):
	print('Present Simple')
	exit()
elif (re.match(r'will', verb) or re.match(r'shall', verb)):
	print('Future Simple')
	exit()
else:
	print('Such a verb isn\'t possible. Check the spelling. \n Такой глагол невозможен. Проверьте написание.')