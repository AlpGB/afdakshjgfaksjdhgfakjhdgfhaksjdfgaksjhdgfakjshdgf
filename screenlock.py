import tkinter as tk
import time
import threading

def make_fullscreen(window):
    while True:
        try:
            window.attributes("-fullscreen", True)  
            window.update()  
            time.sleep(0.001)  
        except Exception:
            break

def open_fullscreen_window():
    window = tk.Tk()
    window.title("Fullscreen Window")

    window.attributes("-fullscreen", True)

    window.attributes("-topmost", True)

    fullscreen_thread = threading.Thread(target=make_fullscreen, args=(window,))
    fullscreen_thread.daemon = True
    fullscreen_thread.start()

    def on_close():
        window.quit()  
        open_fullscreen_window()  

    window.protocol("WM_DELETE_WINDOW", on_close)

    window.mainloop()

open_fullscreen_window()
