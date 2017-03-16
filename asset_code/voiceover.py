import speech_recognition
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print ".....----.... Speak Now ....----...."
    audio = recognizer.listen(source)

try:
    print "audio : {0}".format(recognizer.recognize_google(audio))
		# or: return recognizer.recognize_sphinx(audio)
except speech_recognition.UnknownValueError:
	print("Could not understand audio")
except speech_recognition.RequestError as e:
	print("Recog Error; {0}".format(e))

