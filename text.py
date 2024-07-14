from gtts import gTTS
import os
text="k xa hau solti"
lang = "en"
obj= gTTS(text=text,lang=lang,slow=False)
obj.save('hello.mp3')
os.system('hello.mp3')