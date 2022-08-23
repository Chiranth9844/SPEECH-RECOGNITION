#we are using speech_recognition and pyAudio modules
import  speech_recognition  as  sr
import  webbrowser  as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with  sr.Microphone()  as  source:
    print()
    print('speak now')
    audio = r3.listen(source)

if  'search'  in r2.recognize_google(audio):
    #print("here text can be seen "+r2.recognize_google(audio))
    r2 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    with  sr.Microphone()  as source:
        print('search your query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except  sr.UnknownValueError:
            print('error')
        except  sr.RequestError  as e:
            print('failed'.format(e))

elif  'video' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with  sr.Microphone() as source:
        print('search for a video')
        audio = r2.listen(source)

        try:
            get = r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)

        except sr.UnknownValueError:
            print('could not understand')
        except sr.RequestError as e:
            print('failed to get results'.format(e))

elif  'web' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://bit-bangalore.edu.in/'

    try:
        wb.get().open_new(url)

    except sr.UnknownValueError:
        print('could not understand')
    except sr.RequestError as e:
        print('failed to get results'.format(e))

elif  'v' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://vtu.ac.in/'

    try:
        wb.get().open_new(url)

    except sr.UnknownValueError:
        print('could not understand')
    except sr.RequestError as e:
        print('failed to get results'.format(e))

elif  'geek' in r1.recognize_google(audio):
    r1 = sr.Recognizer()

    try:
        wb.get().open_new(url)

    except sr.UnknownValueError:
        print('could not understand')
    except sr.RequestError as e:
        print('failed to get results'.format(e))

else:
    print("couldn't recognize the speech")
