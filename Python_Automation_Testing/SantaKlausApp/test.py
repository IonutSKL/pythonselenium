import copy
import random
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

emails = ['scarlatalinn@gmail.com', 'andrada.marin5@gmail.com', 'dragosdm22@gmail.com', 'andrei.tenea93@gmail.com', 'andreea.madalinavulpe@gmail.com', 'robert.buica@gmail.com', 'roxana.barran@yahoo.ro', 'denisa_vatulescu@yahoo.com', 'alex.dragomir95@yahoo.com', 'christian.cuna89@gmail.com']
names = ['Ionut', 'Andrada', 'Dragos', 'Andrei', 'Andreea', 'Robert', 'Roxana', 'Denisa', 'Alex', 'Cristi']

#emails = ['scarlatalinn@gmail.com', 'denisa_vatulescu@yahoo.com']
#names = ['Ionut', 'Denisa']


def secret_santa(names):
    my_list = names
    choose = copy.copy(my_list)
    result = []
    lovers = [('Ionut', 'Denisa'), ('Andrei', 'Andreea'), ('Cristi', 'Andrada'), ('Alex', 'Roxana'),('Denisa', 'Ionut'), ('Andreea', 'Andrei'), ('Andrada', 'Cristi'), ('Roxana', 'Alex')]
    for i in my_list:
        names = copy.copy(my_list)
        names.pop(names.index(i))
        chosen = random.choice(list(set(choose)&set(names)))
        result.append((i,chosen))
        choose.pop(choose.index(chosen))
        love = any(check in result for check in lovers)
        while love == 'true':
            secret_santa(names)
            return result
        '''
        if love:
            print('true')
            secret_santa(names)
            return result
        else:
            print('false')'''
    return result


ss_result = secret_santa(names)

final = zip(ss_result,emails)
print(ss_result)