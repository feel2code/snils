import re

import pyperclip


# checking if SNILS scheme exists in clipboard
# copying from clipboard and find SNILS by scheme
while True:
    buffer = re.findall(
        r'\d\d\d-\d\d\d-\d\d\d \d\d',
        pyperclip.paste()
        )
    try:
        pyperclip.copy(buffer[0])
    except IndexError:
        pass
    print(buffer)
