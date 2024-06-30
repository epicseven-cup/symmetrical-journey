import re


input_text = "!add  Character Name: supertf \
    Discord Name: _latitude\
    Character Backstory: Overwatch streamer that was teleported to another world \
    Class: wizard\
    Alignment: evil"


character_name = re.search(r'Character Name:.(\w+)', input_text).group(1)


print(character_name)