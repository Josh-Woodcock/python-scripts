def andList(list):
    for x in range(len(list)-1):
        
        print(list[x], end = ', ')

    print('and ' + list[-1])




randomList = ['apples', 'bananas', 'tofu', 'cats']

andList(randomList)
