import pyjokes
import pyttsx3

print("Printing Jokes")
joke = pyjokes.get_joke()
print(joke)

engine = pyttsx3.init()
engine.say("Hi Sanju, Everytime Consistency Beats Motivation, Don't Lose Your Hope, Shree Krishna is With You")
engine.runAndWait()

# This is a Modeule Program