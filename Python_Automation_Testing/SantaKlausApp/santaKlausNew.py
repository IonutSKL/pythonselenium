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


for x in final:
    fromaddr = 'santaklausautomation@gmail.com'
    toaddr = x[1]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "FINAL SECRET EMAIL FOR SECRET SANTA!"

    body1 = "Hello, " + str( x[0][0] )
    body2 = '''!\n This is an automated email from Ionut's Secret Santa Python Program.\n\nYou drew\n.......\n........\n........\n''' + str(
        x[0][1] ) + "!!\n\nRule Number 1: Please do not tell anyone!\n"
    body3 = "Rule Number 2: The budget is 50 lei! \nWhat are you waiting for? Go ahead and get something nice for " + str(
        x[0][1] ) + "!\n\n\n"
    body = body1 + body2 + body3
    msg.attach( MIMEText( body, 'plain' ) )

    filename = "santa.jpg"
    attachment = open( "santa.jpg", "rb" )

    part = MIMEBase( 'application', 'octet-stream' )
    part.set_payload( (attachment).read() )
    encoders.encode_base64( part )
    part.add_header( 'Content-Disposition', "attachment; filename= %s" % filename )

    msg.attach( part )

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, 'SantaKlaus1234#')
    text = msg.as_string()
    server.sendmail( fromaddr, toaddr, text )
    server.quit()
    print("mail sent to", x[1])