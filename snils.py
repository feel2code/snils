import re

import pyperclip

# looping to check clipboard

while True:

    # checking if SNILS scheme exists in clipboard
    # copying from clipboard and find SNILS by scheme
    buffer1 = str(re.findall(r'\d\d\d-\d\d\d-\d\d\d \d\d', pyperclip.paste()))
    buffer2 = str(
        buffer1
    ).replace(
        "['", ""
    ).replace(
        "']", ""
    )

    # if clipboard is empty after modify
    # then don't copy and modify clipboard
    if buffer2 != '[]':
        buf2 = str(
            buffer1
            ).replace(
                "['", ""
            ).replace(
                "']", ""
            )
        snils = str(
            buffer1
            ).replace(
                "-", ""
            ).replace(
                " ", ""
            ).replace(
                "['", ""
            ).replace(
                "']", ""
            )
        pyperclip.copy(snils)
        print(snils)
