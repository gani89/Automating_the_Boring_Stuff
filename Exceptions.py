

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol needs to be a string of length 1")
    if (width < 2) or (height < 2):
        raise Exception('Width and Height must be greater or equal than 2')
    print(symbol*width)

    for i in range(height - 2):
        print(symbol + ' '*(width-2) + symbol)

    print(symbol * width)

print(boxPrint('*',10,5))

import traceback

try:
    raise Exception('This is the error message')
except:
        errorFile = open('errorInfo.txt', 'a')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was wrriten to errorInfo.txt')