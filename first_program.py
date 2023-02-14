person = {}

while True :
    name = input('name :');
    age = input('age :');
    person[name]=age;

    another = input('another y/n :');

    if another == 'y':
        continue;
    else :
        break;

for (keys , values) in person.items():
    print(f'{keys} is {values} years old');
