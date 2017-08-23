import random

messages = ['It is cerstain',
            'It is decidely so',
            'Yes defintely',
            'Reply hazy, ask again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

