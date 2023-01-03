import tkinter as tk
import alkoholfunksjoner as af


window = tk.Tk()

window.title('Alkoholkalkulator')

window.geometry('300x200')


label = tk.Label(text='Velg volum, alkoholprosent og pris...')
label1 = tk.Label(text='OBS: Skriv volumet i liter!')
label2 = tk.Label(text='Resultat: ')


label.pack()
label1.pack()


def alkv():
    global label2
    label2.pack_forget()
    volum = textbox1.get()
    prosent = textbox2.get()
    pris = textbox3.get()
    label2 = tk.Label(text='Resultat: ' + str(af.alkohol_volum(float(volum), float(prosent))))
    label2.pack()
    # print(volum)
    # print(prosent)
    # print(pris)

'''
def totv():
    global label2
    label2.pack_forget()
    volum = textbox1.get()
    prosent = textbox2.get()
    pris = textbox3.get()
    label2 = tk.Label(text='Resultat: ' + str(af.total_volum(float(alko), float(prosent))))
    label2.pack()
'''

def alkpkr():
    global label2
    label2.pack_forget()
    volum = textbox1.get()
    prosent = textbox2.get()
    pris = textbox3.get()
    label2 = tk.Label(text='Resultat: ' + str(round(af.alkohol_per_krone(float(af.alkohol_volum(float(volum), float(prosent))), pris), 2)) + 'ml/kr')
    label2.pack()

textbox1 = tk.Entry(window)
textbox2 = tk.Entry(window)
textbox3 = tk.Entry(window)


button = tk.Button(text="Total Alkohol", command=alkv)
button2 = tk.Button(text="Pris per alkohol", command=alkpkr)


textbox1.pack()
textbox2.pack()
textbox3.pack()
button.pack()
button2.pack()
label2.pack()


window.mainloop()
