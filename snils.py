import pyperclip
import re

# looping to check clipboard

while True:

    # checking if SNILS scheme exists in clipboard

    try:

        # copying from clipboard and find SNILS by scheme

        buffer = pyperclip.paste()
        buffer1 = re.findall(r'\d\d\d-\d\d\d-\d\d\d \d\d', buffer)
        buffer2 =  str(buffer1).replace("['", "").replace("']", "")

        # if clipboard is empty after modify then don't copy and modify clipboard

        if buffer2 != '[]':
            buf2 = str(buffer1).replace("['", "").replace("']", "")
            snils = str(buffer1).replace("-", "").replace(" ", "").replace("['", "").replace("']", "")
            pyperclip.copy(snils)
            print(snils)

    # можно и не ловить

    except:
        print('error')