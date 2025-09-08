from datetime import datetime
import tkinter as jarvis
import os
import platform
# import psutil
# external libs - can't load to test b/c school laptop blocks pip.
# from Pillow import Image as img
# from Pillow import ImageTk as imgtk

# load the image please
img_path = "cool_spot.png"
# using cool spot as a test img
# open the image
# og_img = img.open(img_path)

# totally not taken from gemini
# source: trust me bro :3
def resize_img(og_phi, new_width, new_height):
    # make the new
    new_img = jarvis.PhotoImage(width=new_width, height=new_height)
    # placeholder bg is now a nice shade of orange.
    for y in range(new_height):
        for x in range (new_width):
            new_img.put("#fa6605", (x, y))
    return new_img

def upd_img(event):
    # global current image label and original photo image
    global cur_img_lb, og_phi
    new_width = event.width
    new_height = event.height
    # new resized photo img
    resz_phi = resize_img(og_phi, new_width, new_height)
    cur_img_lb.config(image=resz_phi)
    # prevention of garbage collection
    cur_img_lb.image = resz_phi

# requires psutil
# mem = psutil.virtual_memory

pingas = datetime.now()
print(pingas)
ui = jarvis.Tk()
ui.title("Cool spot tells you System Information by nrkceg2")
ui.geometry('920x640')

# create tkimage
# thank you tk 8.6+
ui_img = jarvis.PhotoImage(file=img_path)

# set og photo image to ui_img b/c lazy
og_phi = ui_img


# stringvars.

# Placeholder text if needed.
plhld = "Placeholder! Please replace on release!"

# Time
bingus = jarvis.StringVar()
bingus.set(pingas)

# OS Name
sysname = platform.system()
sysnm = jarvis.StringVar()
sysnm.set((sysname, os.name))

# OS Hostname
syshs = jarvis.StringVar()
syshs.set(platform.node())

# System Memory (sysme is total ram, sysam is available ram)
sysme = jarvis.StringVar()
# definitions for sysme and sysam unable to be tested b/c psutil cannot be installed
# on the school laptop.
# sysme.set(mem.total)
sysme.set(plhld)
sysam = jarvis.StringVar()
# sysam.set(mem.available)
sysam.set(plhld)

# System OS Version
sysos = jarvis.StringVar()
sysver = platform.version()
sysver_win32 = platform.win32_ver()
sysos.set(sysver)

# System architecture
sysar = jarvis.StringVar()
sysar.set(platform.machine())
sysardetailed = jarvis.StringVar()
sysardetailed.set(platform.architecture())

# System Processor
syspr = jarvis.StringVar()
syspr.set(platform.processor())

# System Processor core count(?)
syscr = jarvis.StringVar()
syscr.set(os.cpu_count())

# combined core and processor info.
sysprc = jarvis.StringVar()
sysprc.set((platform.processor(), os.cpu_count(), "Cores."))

# Python version + build info
syspy = jarvis.StringVar()
syspy.set((platform.python_version(), "(", platform.python_implementation(), ")"))
syspyb =jarvis.StringVar()
syspyb.set(platform.python_build())

# User logon
sysur = jarvis.StringVar()
sysur.set(os.getlogin())

# Full Platform
syspl = jarvis.StringVar()
syspl.set(platform.platform())

# window creation
# if this doesn't work im going to implode maybe
# as of like, 5-10 minutes after this was written, cool spot is finally
# displayed. still no text though, I ought to fix that soon.
# update from potential first release: text be displaying
cnt_bg = jarvis.Label(ui, image = (ui_img))

# contents of table
cnt_bg.place(x=0, y=0, relwidth=1, relheight=1)
cnt0 = jarvis.Label(ui, textvariable = bingus, font=("Hobo Std", 14))
cnt0l = jarvis.Label(ui, textvariable = sysur, font=("Hobo Std", 14))

cnt1l = jarvis.Label(ui, text = "Computer Name:", font=("Hobo Std", 14))
cnt1 = jarvis.Label(ui, textvariable = syshs, font=("Hobo Std", 14))

cnt2l = jarvis.Label(ui, text = "Operating System:", font=("Hobo Std", 14))
cnt2 = jarvis.Label(ui, textvariable = sysnm, font=("Hobo Std", 14))

cnt3l = jarvis.Label(ui, text = "Operating System Version:", font=("Hobo Std", 14))
cnt3 = jarvis.Label(ui, textvariable = sysos, font=("Hobo Std", 14))

cnt4l = jarvis.Label(ui, text = "Detailed architecture:", font=("Hobo Std", 14))
cnt4 = jarvis.Label(ui, textvariable = sysardetailed, font=("Hobo Std", 14))

cnt5l = jarvis.Label(ui, text = "Processor:", font=("Hobo Std", 14))
cnt5 = jarvis.Label(ui, textvariable = sysprc, font=("Hobo Std", 14))

cnt6l = jarvis.Label(ui, text = "Python version:", font=("Hobo Std", 14))
cnt6 = jarvis.Label(ui, textvariable = syspy, font=("Hobo Std", 14))

cnt7l = jarvis.Label(ui, text = "Python build details:", font=("Hobo Std", 14))
cnt7 = jarvis.Label(ui, textvariable = syspyb, font=("Hobo Std", 14))

cnt8l = jarvis.Label(ui, text = "Full platform:", font=("Hobo Std", 14))
cnt8 = jarvis.Label(ui, textvariable = syspl, font=("Hobo Std", 14))

# table settings
cnt0.grid(row=0, column=0)
cnt0l.grid(row=0, column=1)

cnt1l.grid(row=1, column=0)
cnt1.grid(row=1, column=1)

cnt2l.grid(row=2, column=0)
cnt2.grid(row=2, column=1)

cnt3l.grid(row=3, column=0)
cnt3.grid(row=3, column=1)

cnt4l.grid(row=4, column=0)
cnt4.grid(row=4, column=1)

cnt5l.grid(row=5, column=0)
cnt5.grid(row=5, column=1)

cnt6l.grid(row=6, column=0)
cnt6.grid(row=6, column=1)

cnt7l.grid(row=7, column=0)
cnt7.grid(row=7, column=1)

cnt8l.grid(row=8, column=0)
cnt8.grid(row=8, column=1)

# run the ui.
# update pingas on window draw (hopefully)
ui.mainloop()
pingas = datetime.now()
