import speech_recognition as sr

path = "/Users/florianlan/Desktop/Florian/Graduate/1st Semester/ECE5725/final project/voice_wav"
# obtain audio from the microphone
r = sr.Recognizer()
harvard = sr.AudioFile(path+"/it is a test.wav")
with harvard as source:
    
    # noise reduction
    r.adjust_for_ambient_noise(source,duration=0.5)  
    audio = r.record(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio) + " with sphinx support")
    print("Google thinks you said " + r.recognize_google(audio) + " with google support")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))




