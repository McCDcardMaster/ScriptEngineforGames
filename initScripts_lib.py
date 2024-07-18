
print("""Script Engine for the PyCodeED Game Engine - SNAPSHOT

For writing scripts in the future, you can use the examples provided in the documentation:

      
``` Python
      
# Print Hello World Script

    
message_printed = False # - status check

      
def hello_world(event):   # <- script function
    global message_printed # <- Setting the main variable
    if not message_printed: # <- checking whether the message has already been shown, if not, output "Hello World"
        print("Hello world!") # <- print terminal message
        message_printed = True # <- Setting the flag to True means that the message was shown
      
      # Hello world message
```
      
# Print Hello World Given that
      
import pygame # - import PyGame Lib (py -m pip install pygame)

enter_pressed = False # - check status

def handle_event(event): # <- script function
    global enter_pressed # <- Setting the main variable
    if event.type == pygame.KEYDOWN: # <- Checking if the keyboard is in use
        if event.key == pygame.K_RETURN: #Checking if the Enter key is pressed
            if not enter_pressed: # <- Since at the beginning the status is False, this means that Enter was not pressed
                print("Hello World!") # <- print
                enter_pressed = True # <- showing that the action has been completed
    elif event.type == pygame.KEYUP: # <- Checking whether the key is released
        if event.key == pygame.K_RETURN:
            enter_pressed = False # - if it was Enter, return the False flag to complete execution and wait for the next press

```

# Play Sound Script
      
import pygame # - import PyGame Lib

sound_played = False # - Check status

def play_sound(event):   # <- script function
    global sound_played  # <- Setting the main variable
    if not sound_played:  # <- checking whether the sound was played, if not then play it
        try:
            pygame.mixer.init()
            sound = pygame.mixer.Sound('assets/sfx/your_sound.wav')
            sound.play()
            sound_played = True
        except Exception as e:
            print(f"Error: {e}")
                     
           # ^^^ 
        # trying to load sound and play it
    # if it is unsuccessful, display an error message in the console

```

# Draw red square at screen script

import pygame # - import PyGame Lib
from utils.gamewindow import size # <- set the parameters of the window we will access 

square = pygame.Surface((50, 50)) # <- call square
square.fill("Red") # <- Set the full color to the square (Red)

def redSquare(event): # <- Script function
    size.window_size.blit(square, (295, 220)) # <- draw a square on the coordinates, that is, in the center
    pygame.display.update() # <- screen update

```     
      
# Draw blue circle at screen script

import pygame # - import PyGame Lib
from utils.gamewindow import size # <- set the parameters of the window we will access

def bluecircle(event): # <- Script function
    pygame.draw.circle(size.window_size, 'Blue', (320, 220), 50) # <-draw a blue circle figure
    pygame.display.update() # <- screen update      

```

# Displaying the background image script

import pygame # <- import PyGame Lib
from utils.gamewindow import size # <- Load utils game window 

bg = pygame.image.load("assets/images/bg.png") # <- Load background image

def background_script(event): # <- Script function
    size.window_size.blit(bg, (0, 0)) # <- Draw background 

```\n""")