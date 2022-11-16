import speech_recognition as sr
import os

PATH = "/Users/florianlan/Desktop/Florian/Graduate/1st Semester/ECE5725/final project/voice_wav/"
# the file we need to recognize

# file format
FORMAT = AUDIO_FILE[-3:]  # only wav format is supported

# Preset AudioFile
PROMPT = "./prompt.wav"
FIRE = "./fire.wav"
SHUTDOWN = './shutdown.wav'


def getResults(audio_file):


    # obtain audio from the microphone
    r = sr.Recognizer()
    harvard = sr.AudioFile(PATH+audio_file)
    with harvard as source:
        # noise reduction
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.record(source)

    # recognize speech using Sphinx
    try:
        sphinx_res = r.recognize_sphinx(audio)
        google_res = r.recognize_google(audio)
        print("Sphinx thinks you said " + sphinx_res + " with sphinx support")
        print("Google thinks you said " + google_res + " with google support")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    return google_res

def voiceControl():
    # 1. start to record audio and save it
    
    print("Please input your voice command")
    os.system('aplay'+PROMPT)
    # name of each record
    count = 0
    name = count + '.wav'
    os.system('sudo arecord -D “plughw:3,0” -d 5 wav'+name)
    print("Done")

    cmd = getResults(name)
    
    if cmd == 'fire':
        os.system("aplay"+FIRE)
        #TODO call Fire code here
        os.system("sudo python3 &")

    elif cmd == 'shutdown':
        os.system("aplay"+SHUTDOWN)
        #TODO call Shutdown code here



