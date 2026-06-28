import speech_recognition as sr



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga algo")
    audio = r.listen(source)

try:
       print("Voce disse: "+ r.recogize.google(audio, language="pt-BR"))
except sr.UnkownValueError:
       print("Bia não pode entender o áudio!")
except sr.RequestError as e:
    print("Error ao chmar o Google Speech Recognition service; (e)".format(e))

