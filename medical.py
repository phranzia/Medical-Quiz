import random

qas = [
    ('What is the brand name for acetaminophen? ', 'Tylenol'),
    ('What is the brand name for lacosamide? ', 'Vimpat'),
    ('What is the brand name for levetiracetam? ', 'Keppra')
    ]
random.shuffle(qas)
numRight = 0

for question, rightAnswer in qas:
    answer = input(question + '')
    if answer.lower() == rightAnswer.lower():
        print('Right')
        numRight = numRight + 1
    else: 
        print('Nope! It\'s ' + rightAnswer)

print('You got %d right and %d wrong.' %(numRight, len(qas) - numRight))