import random

emails = ['scarlatalinn@gmail.com', 'andrada.marin5@gmail.com', 'Dragosdm22@gmail.com', 'andrei.tenea93@gmail.com', 'andreea.madalinavulpe@gmail.com', 'robert.buica@gmail.com', 'roxana.barran@yahoo.ro', 'denisa_vatulescu@yahoo.com', 'alex.dragomir95@yahoo.com', 'christian.cuna89@gmail.com']
names = ['Ionut', 'Andrada', 'Dragos', 'Andrei', 'Andreea', 'Robert', 'Roxana', 'Denisa', 'Alex', 'Cristi']
#print(emails)

#emails_dict = {'scarlatalinn@gmail.com': 'Ionut Scarlat', 'andrada.marin5@gmail.com': 'Andrada Marin'}
#print(emails_dict)


def pop_random(emails):
    idx = random.randrange(0, len(emails))
    return emails.pop(idx)


pairs = []

while len(emails) > 0:
    rand1 = pop_random(emails)
    rand2 = pop_random(names)
    pair = rand1, rand2
    pairs.append(pair)


for i in pairs:
    print(i)