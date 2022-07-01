import pyautogui
from time import sleep

class MouseMover():
    def __init__(self):
        self.interval = 5
        self.position = pyautogui.position()

    def run(self):
        current_direction = 1
        while True:
            try:
                if not self.has_mouse_moved():
                    pyautogui.moveRel(0, 1 * current_direction)
                    current_direction = current_direction * (-1)

                    #send a key input
                    pyautogui.press("ctrl")

                self.position = pyautogui.position()
            except pyautogui.FailSafeException:
                pass 
            sleep(self.interval)
    
    def has_mouse_moved(self):
        current_position = pyautogui.position()
        if self.position == current_position:
            return False
        return True
