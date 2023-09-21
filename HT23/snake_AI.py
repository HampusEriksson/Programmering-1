import random
import time
import keyboard  # Make sure to install the "keyboard" module using pip if you haven't already

# List of keys to choose from
keys = ['w', 'a', 's', 'd']

while True:
    # Generate a random keypress
    key = random.choice(keys)
    # Simulate the keypress
    keyboard.press(key)
    
    # Wait for 1 second
    
    # Release the key
    keyboard.release(key)