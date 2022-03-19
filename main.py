from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys







recogniser = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate',160)

todo_list = ['Go Shopping', 'Clean Room', 'Record Video']


def createNewNote():
    global recogniser
    
    speaker.say("What do you want to write onto your note?")
    speaker.runAndWait()

    done = False
    
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recogniser.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recogniser.listen(mic)
                
                note = recogniser.recognize_google(audio)
                note = note.lower()
               
                speaker.say("Choose a filename!")
                speaker.runAndWait()
                recogniser.adjust_for_ambient_noise(mic, duration=0.2)
               
                filename = recogniser.recognize_google(audio)
                filename = filename.lower()
                
                
            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                speaker.runAndWait()
            
        except speech_recognition.UnknownValueError as e:
            print(e)
            recogniser = speech_recognition.Recognizer()
            speaker.say('I did not understand you! Please try again!')
            speaker.runAndWait()



def addNewTodo():
    global recogniser
    
    speaker.say("What todo do you want to add?")
    speaker.runAndWait()
    done = False
    
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                
                recogniser.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recogniser.listen(mic)

                item = recogniser.recognize_google(audio)
                item = item.lower()
                
                todo_list.append(item)
                done = True
                
                speaker.say(f"I added {item} to the to do list!")
                speaker.runAndWait()                

        except speech_recognition.UnknownValueError as e:
            print(e)
            recogniser = speech_recognition.Recognizer()
            speaker.say('I did not understand you! Please try again!')
            speaker.runAndWait()
            
            
def show_todos():
    speaker.say("The items on your to do list are:")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()
    
    
def hello():
    speaker.say("Hello! What can I do for you?")
    speaker.runAndWait()
    
def quit():
    pass
    
            
        
'''assistant = GenericAssistant('intents.json')
assistant.train_model()
'''



