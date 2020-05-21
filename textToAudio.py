from gtts import gTTS
import os
myText = "Ayesha is Beautifull girl in MCA Depertment one and Only"
language='en'
output=gTTS(text=myText,lang=language,slow=False)
output.save('output.mp3')
os.system('start output.mp3')
