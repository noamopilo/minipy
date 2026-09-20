import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

d = 0.02
btn = Button.left

start_key = KeyCode(char="a")
exit_key = KeyCode(char="b")

print("To start/pause autoclicker press 'a', to exit press 'b'.")

class AutoClicker(threading.Thread):
    def __init__(self, d, btn):
        super().__init__()
        self.d = d
        self.btn = btn
        self.clicking = False
        self.active = True
    
    def start_click(self):
        self.clicking = True
    
    def stop_click(self):
        self.clicking = False
    
    def exit(self):
        self.stop_click()
        self.active = False
    
    def run(self):
        while self.active:
            while self.clicking:
                mouse.click(self.btn)
                time.sleep(self.d)
            time.sleep(0.1)
    
mouse = Controller()
c = AutoClicker(d, btn)
c.start()

def on_press(k):
    if k == start_key:
        if c.clicking:
            c.stop_click()
            print("Clicker Stopped.")
        else:
            c.start_click()
            print("Clicker Started.")
    elif k == exit_key:
        c.exit()
        print("Exiting...")
        return False

with Listener(on_press=on_press, suppress=True) as listener:
    listener.join()