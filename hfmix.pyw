from tkinter import *
from sound_panel import *
import pygame.mixer

app = Tk()

app.title("Head First Mix")

mixer = pygame.mixer
mixer.init()

panel = SoundPanel(app, mixer, "50459_M_RED_Nephlimizer.wav")
panel.pack()
panel = SoundPanel(app, mixer, "49119_M_RED_HardBouncer.wav")
panel.pack()

def shutdown():
    track.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
