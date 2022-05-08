from tkinter import*
import webbrowser

avancement = 0

def avancement_add():
    global avancement
    avancement += 1
    label_avancement.config(text = avancement)
    frame.destroy()
    window.quit()

def quitter():
    window.destroy()

window = Tk()

window.title("UB")
window.geometry("1000x1000")
window.minsize(1000,1000)
#changer de logo
window.iconbitmap("")

bgd = '#FF2D00'
window.config(background=bgd)

#cree la frame
frame = Frame(window, bg = bgd)

#texte
label_title = Label(frame, text="Ultimate Bravery", font=("Courrier", 42), bg=bgd)
label_title.pack()

#second texte
label_subtitle = Label(frame, text="Le jeu du hasard et de la rage", font=("Courrier", 12), bg=bgd)
label_subtitle.pack()

#bouton
Pro = Button(frame, text="Jouer", font=("Courrier", 12), bg=bgd, bd=0, command=avancement_add, activebackground="#FF6666")
Quit = Button(frame, text="Quitter", font=("Courrier", 12), bg=bgd, bd=0, command=quitter, activebackground="#FF6666")

label_avancement = Label(frame, text=avancement, font=("Courrier", 12), bg=bgd)
label_avancement.pack()

"""#Entrée/demande
test = Entry(frame, text=avancement, font=("Courrier", 12), bg=bgd, bd=0)
test.pack()"""


Pro.pack(pady=100, fill=X)
Quit.pack(fill=X)
frame.pack(expand=YES)

window.mainloop()

#cree la frame
frame = Frame(window, bg = bgd)

#texte
label_title = Label(frame, text="Ultimate Bravery 2", font=("Courrier", 42), bg=bgd)
label_title.pack()

#second texte
label_subtitle = Label(frame, text="Le jeu du hasard et de la rage", font=("Courrier", 12), bg=bgd)
label_subtitle.pack()

#bouton
Pro = Button(frame, text="Jouer", font=("Courrier", 12), bg=bgd, bd=0, command=avancement_add, activebackground="#FF6666")
Quit = Button(frame, text="Quitter", font=("Courrier", 12), bg=bgd, bd=0, command=quitter, activebackground="#FF6666")

label_avancement = Label(frame, text=avancement, font=("Courrier", 12), bg=bgd)
label_avancement.pack()



Pro.pack(pady=100, fill=X)
Quit.pack(fill=X)
frame.pack(expand=YES)

window.mainloop()
