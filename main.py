import pyttsx3
import speech_recognition as sr
audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say('ola, eu sou a Quita')
maquina.say('Como Posso te ajudar?')
maquina.runAndWait()

try:
    with sr.MIcrophone() as source:
        print('Ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, lenguafge='pt-BR')
        comando = comando.lower()
        if 'quita' in comando:
            print(comando)
except:
    print('Microfone não está Funcionando')