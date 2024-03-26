import pyttsx4

# Initialize the pyttsx4 engine
engine = pyttsx4.init()

# Set properties (optional)
engine.setProperty('rate', 160)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Say something
text = "Hello, I'm pyttsx4. Nice to meet you!"
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
