# NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
# rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
# aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

from pynput.keyboard import Key, Controller
import keyboard
from time import sleep

kv = Controller()

# keyboard.press('win+r')
# keyboard.release('win+r')

# kv.press(Key.enter)
# kv.release(Key.enter)
sleep(3)
keyboard.write('ssh bandit12@bandit.labs.overthewire.org -p 2220')
kv.press(Key.enter)
kv.release(Key.enter)
sleep(3)
keyboard.write('JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv')
kv.press(Key.enter)
kv.release(Key.enter)

# # def on_press(key):

#     print('tecla: ',key)

#     keys = str(key)
    
#     try:
        
#         if keys == 'Key.alt_l':
#             print("Saliendo del programa...")
#             listener.stop()

#     except Exception:
#         pass

# with keyboard.Listener(on_press=on_press) as listener:
    # listener.join()
