import cowsay, pyttsx4

# this = input("What's this? ")
this = "This was CS50."

print(cowsay.get_output_string('cow', this))

engine = pyttsx4.init()
engine.say(this)
engine.runAndWait()