import tkinter
import tkinter as tk
from PIL import Image, ImageTk
import random
import numpy as np
from tkinter import Tk, Label, Button, scrolledtext, filedialog, StringVar
from os import path
from tkinter.ttk import Radiobutton

def clicked():
    global file
    file = filedialog.askopenfilename(filetypes = (("Image files","*.bmp"),("all files","*.*")), initialdir= path.dirname(__file__))
    if file:
        lbl11.configure(text=file.split('/')[-1])
        file = file.split('/')[-1]
        lbl04 = Label(window, text='Пустой контейнер',font = ('Times New Roman', 14), fg='#000000',bg="#3d3d3d")
        lbl04.grid(sticky='W')
        lbl04.place(x=110,y=280)

        emp_con = Image.open(file)
        emp_con = emp_con.resize((300, 200))
        global tk_emp_con
        tk_emp_con = ImageTk.PhotoImage(emp_con)
        lbl05 = Label(window, image=tk_emp_con)
        lbl05.grid(sticky='W')
        lbl05.place(x=30,y=310)


def enable_raid():
    rad2_1.configure(state='enable')
    rad2_2.configure(state='enable')
    rad2_3.configure(state='enable')
    rad2_4.configure(state='enable')
    rad2_5.configure(state='enable')
    rad2_6.configure(state='enable')
    rad2_7.configure(state='enable')
    rad2_8.configure(state='enable')
def disable_raid():
    rad2_1.configure(state='disable')
    rad2_2.configure(state='disable')
    rad2_3.configure(state='disable')
    rad2_4.configure(state='disable')
    rad2_5.configure(state='disable')
    rad2_6.configure(state='disable')
    rad2_7.configure(state='disable')
    rad2_8.configure(state='disable')
def hiding():
    def ext_pix(image):
        pixels = list(image.getdata())
        print('Пиксели:', pixels[:10])
        for i in range(len(pixels)):
            pixels[i] = list(pixels[i])
            for j in range(len(pixels[i])):
                pixels[i][j] = bin(pixels[i][j])[2:].zfill(8)
        return pixels

    if var1.get() == '1':
        print('Метод LSB-R\n_Скрытие сообщения_')
        image = Image.open(file)
        width, height = image.size
        pixels = ext_pix(image)
        print('Пиксели в двоичном виде:', pixels[:10])

        secmes = scr.get("1.0", "end-1c")
        print('Сообщение:', secmes)
        global lenmes
        lenmes = len(secmes)
        binary_secmes = ''.join(format(ord(x), '08b') for x in secmes)
        print('Сообщение в двоичном виде:', binary_secmes)

        
        raid = int(var2.get())
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                r = list(pixels[i][j][-raid:])
                for k in range(len(r)):
                    if binary_secmes == '':
                        break
                    elif r[k] != binary_secmes[0]:
                        r[k] = binary_secmes[0]
                    binary_secmes = binary_secmes[1:]
                pixels[i][j] = pixels[i][j][:-raid] + ''.join(r)
        print('Пиксели с сообщением:', pixels[:10])

        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                pixels[i][j] = int(pixels[i][j], 2)
            pixels[i] = tuple(pixels[i])
        print('Пиксели в десятичном виде с сообщением:', pixels[:10])

        image_LSB_R = Image.new('RGB', (width, height))
        image_LSB_R.putdata(pixels)
        save_path = filedialog.asksaveasfilename(defaultextension=".bmp")
        if save_path:
            image_LSB_R.save(save_path)

        global image_for_ext
        image_for_ext = image_LSB_R

        lbl14 = Label(window, text='Заполненный контейнер',font = ('Times New Roman', 14), fg='#000000',bg="#3d3d3d")
        lbl14.place(x=390, y=280)

        image_LSB_R = image_LSB_R.resize((300, 200))
        global tk_image
        tk_image = ImageTk.PhotoImage(image_LSB_R)
        lbl15 = Label(window, image=tk_image)
        lbl15.place(x=340, y=310)

    elif var1.get() == '2':
        print('Метод LSB-M\n_Скрытие сообщения_')
        image = Image.open(file)
        width, height = image.size
        pixels = ext_pix(image)
        print('Пиксели в двоичном виде:', pixels[:10])

        secmes = scr.get("1.0", "end-1c")
        print('Сообщение:', secmes)
        #global lenmes
        lenmes = len(secmes)
        binary_secmes = ''.join(format(ord(x), '08b') for x in secmes)
        print('Сообщение в двоичном виде:', binary_secmes)

        raid = int(var2.get())
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                if binary_secmes == '':
                    break
                l = int(binary_secmes[:raid], 2)
                r = pixels[i][j]
                if l != int(r[-raid:], 2):
                    if raid != 1:
                        k1 = 0
                        while l != int(r[-raid:], 2):
                            r = bin(int(r, 2) + 1)[2:]
                            k1 += 1
                        r1 = r
                        r = pixels[i][j]
                        k2 = 0
                        while l != int(r[-raid:], 2) and not (bin(int(r, 2) - 1).startswith('-')):
                            r = bin(int(r, 2) - 1)[2:]
                            k2 += 1
                        r2 = r
                        R = [r1, r2]
                        if k1 > k2:
                            pixels[i][j] = r1
                        elif k1 < k2:
                            pixels[i][j] = r2
                        else:
                            pixels[i][j] = random.choice(R)
                    else:
                        pixels[i][j] = bin(int(pixels[i][j], 2) + random.choice([-1, 1]))[2:]
                binary_secmes = binary_secmes[raid:]

        print('Пиксели с сообщением:', pixels[:10])

        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                pixels[i][j] = int(pixels[i][j], 2)
            pixels[i] = tuple(pixels[i])
        print('Пиксели в десятичном виде с сообщением:', pixels[:10])

        image_LSB_M = Image.new('RGB', (width, height))
        image_LSB_M.putdata(pixels)
        save_path = filedialog.asksaveasfilename(defaultextension=".bmp")
        if save_path:
            image_LSB_M.save(save_path)

        #global image_for_ext
        image_for_ext = image_LSB_M

        lbl14 = Label(window, text='Заполненный контейнер',font = ('Times New Roman', 14), fg='#000000',bg="#3d3d3d")
        lbl14.place(x=390, y=280)

        image_LSB_L = image_LSB_M.resize((300, 200))
        #global tk_image
        tk_image = ImageTk.PhotoImage(image_LSB_L)
        lbl15 = Label(window, image=tk_image)
        lbl15.place(x=340, y=310)

    elif var1.get() == '3':
        print('Код Хемминга\n_Скрытие сообщения_')
        image = Image.open(file)
        width, height = image.size
        pixels = ext_pix(image)
        print('Пиксели в двоичном виде:', pixels[:10])

        secmes = scr.get("1.0", "end-1c")
        print('Сообщение:', secmes)
        # global lenmes
        lenmes = len(secmes)
        binary_secmes = ''.join(format(ord(x), '08b') for x in secmes)
        print('Сообщение в двоичном виде:', binary_secmes)

        global H
        H = np.array([list(format(i, '04b')) for i in range(1, 16)], dtype=int).T
        print('Проверочная матрица H:\n', H)

        pr = False
        for i in range(len(pixels)):
            c = np.array(list(pixels[i][0][-5:] + pixels[i][1][-5:] + pixels[i][2][-5:]))
            c = np.array(list(map(int, c)))
            m = np.array(list(binary_secmes[:4]))
            m = np.array(list(map(int, m)))
            binary_secmes = binary_secmes[4:]
            while len(binary_secmes) < 4:
                binary_secmes += '0'
                pr = True
            if pr:
                break

            s = (H @ c + m) % 2

            I = 8 * s[0] + 4 * s[1] + 2 * s[2] + s[3]
            if I == 0:
                continue

            c_mod = c
            c_mod[I - 1] = not c_mod[I - 1]
            c_mod = ''.join(str(x) for x in c_mod)

            pixels[i][0] = pixels[i][0][:-5] + c_mod[:5]
            c_mod = c_mod[5:]
            pixels[i][1] = pixels[i][1][:-5] + c_mod[:5]
            c_mod = c_mod[5:]
            pixels[i][2] = pixels[i][2][:-5] + c_mod[:5]
            c_mod = c_mod[5:]
        print('Пиксели в двоичном виде с сообщением:', pixels)

        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                pixels[i][j] = int(pixels[i][j], 2)
            pixels[i] = tuple(pixels[i])
        print('Пиксели в десятичном виде с сообщением:', pixels[:10])

        image_Hem = Image.new('RGB', (width, height))
        image_Hem.putdata(pixels)
        save_path = filedialog.asksaveasfilename(defaultextension=".bmp")
        if save_path:
            image_Hem.save(save_path)

        # global image_for_ext
        image_for_ext = image_Hem

        lbl14 = Label(window, text='Заполненный контейнер',font = ('Times New Roman', 14), fg='#000000',bg="#3d3d3d")
        lbl14.place(x=390, y=280)

        image_Hem = image_Hem.resize((300, 200))
        # global tk_image
        tk_image = ImageTk.PhotoImage(image_Hem)
        lbl15 = Label(window, image=tk_image)
        lbl15.place(x=340, y=310)

def extraction():
    def ext_pix(image):
        pixels = list(image.getdata())
        print('Пиксели:', pixels[:10])
        for i in range(len(pixels)):
            pixels[i] = list(pixels[i])
            for j in range(len(pixels[i])):
                pixels[i][j] = bin(pixels[i][j])[2:].zfill(8)
        return pixels

    if var1.get() == '1' or var1.get() == '2':
        raid = int(var2.get())
        print('\n_Извлечение сообщения_')
        image = image_for_ext
        pixels = ext_pix(image)
        print('Пиксели в двоичном виде:', pixels)
        secmes = ''
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                secmes += pixels[i][j][-raid:]
        print('Сообщение в двоичном виде: ', secmes)
        chunks = [secmes[i:i + 8] for i in range(0, len(secmes), 8)]
        mes = ''.join(chr(int(chunk, 2)) for chunk in chunks)
        print('Сообщение:', mes[:lenmes])

        lbl_mes = Label(window, text='Извлеченное сообщение', font = ('Times New Roman', 14), fg='#000000',bg="#3d3d3d")
        lbl_mes.place(x=720, y=280)

        scr_mes = scrolledtext.ScrolledText(window,fg='#29a61e',bg="black", width=40, height=12)
        scr_mes.insert(tkinter.INSERT, mes[:lenmes])
        scr_mes.place(x=660, y=310)

    elif var1.get() == '3':
        print('\n_Извлечение сообщения_')
        image = image_for_ext
        pixels = ext_pix(image)
        print('Пиксели в двоичном виде:', pixels)
        secmes_err = ''
        for i in range(len(pixels)):
            secmes_err += pixels[i][0][-5:] + pixels[i][1][-5:] + pixels[i][2][-5:]
        print('Сообщение в двоичном виде с ошибкой:', secmes_err)

        secmes = ''
        for i in range(0, len(secmes_err), 15):
            ser_err = (H @ np.array(list(int(x) for x in secmes_err[i: i + 15])).tolist()) % 2
            ser_err = ''.join(str(x) for x in ser_err)
            secmes += str(ser_err)
        print(secmes)
        chunks = [secmes[i:i + 8] for i in range(0, len(secmes), 8)]
        mes = ''.join(chr(int(chunk, 2)) for chunk in chunks)
        print('Сообщение:', mes[:lenmes])

        lbl_mes = Label(window, text='Извлеченное сообщение', font=('Times New Roman', 14))
        lbl_mes.place(x=680, y=235)

        scr_mes = scrolledtext.ScrolledText(window, width=40, height=12)
        scr_mes.insert(tkinter.INSERT, mes[:lenmes])
        scr_mes.place(x=680, y=282)

window = Tk()
window.minsize(width=1040, height=1)
window.title('LSB-R/M,')
window.configure(bg='#3d3d3d')
window.geometry('1000x600')

lbl00 = Label(window, text='Скрываемая информация', font = ('Times New Roman', 14), fg='#000000',bg="#3d3d3d")
lbl00.grid(column=0, row=0, pady=10, padx=400, sticky='W')

scr = scrolledtext.ScrolledText(window,font = ('Times New Roman', 14), fg='#29a61e',bg="black", width=60, height=8)
scr.grid(column=0, row=1, padx=10)
scr.focus()

lbl00 = Label(window, text='Контейнер', font = ('Times New Roman', 14), fg='#000000',bg="#3d3d3d")
lbl00.place(x=50,y=10)

btn11 = Button(window, text="Выбрать контейнер", command=clicked, fg='#29a61e',bg="#3d3d3d",activebackground="yellow")
btn11.place(x=40,y=50)

lbl11 = Label(window, text='', font=('Times New Roman', 9), fg='#000000',bg="#3d3d3d")
lbl11.place(x=100, y=100)

lbl02 = Label(window, text='Метод сокрытия', font = ('Times New Roman', 14), fg='#000000',bg="#3d3d3d")
lbl02.place(x=30, y=90)

var1 = StringVar()
rad1 = tk.Radiobutton(window, text='LSB-R',bg="#3d3d3d", fg="#29a61e",activebackground="#3d3d3d", activeforeground="black", value=1, variable=var1, command=enable_raid,)
rad2 = tk.Radiobutton(window, text='LSB-M',bg="#3d3d3d", fg="#29a61e",activebackground="#3d3d3d", activeforeground="black", value=2, variable=var1, command=enable_raid)
rad3 = tk.Radiobutton(window, text='Hamming',bg="#3d3d3d", fg="#29a61e",activebackground="#3d3d3d", activeforeground="black", value=3, variable=var1, command=disable_raid)
rad1.place(x=5, y=130)
rad2.place(x=70, y=130)
rad3.place(x=130, y=130)

lbl03 = Label(window, text='Рейд', font = ('Times New Roman', 14),  fg='#000000',bg="#3d3d3d")
lbl03.place(x=80, y=160)

var2 = StringVar()
rad2_1 = tk.Radiobutton(window, text='1',bg="#3d3d3d", fg="#29a61e", value=1, variable=var2)
rad2_2 = tk.Radiobutton(window, text='2',bg="#3d3d3d", fg="#29a61e", value=2, variable=var2)
rad2_3 = tk.Radiobutton(window, text='3',bg="#3d3d3d", fg="#29a61e", value=3, variable=var2)
rad2_4 = tk.Radiobutton(window, text='4',bg="#3d3d3d", fg="#29a61e", value=4, variable=var2)
rad2_5 = tk.Radiobutton(window, text='5',bg="#3d3d3d", fg="#29a61e", value=5, variable=var2)
rad2_6 = tk.Radiobutton(window, text='6',bg="#3d3d3d", fg="#29a61e", value=6, variable=var2)
rad2_7 = tk.Radiobutton(window, text='7',bg="#3d3d3d", fg="#29a61e", value=7, variable=var2)
rad2_8 = tk.Radiobutton(window, text='8',bg="#3d3d3d", fg="#29a61e", value=8, variable=var2)
rad2_1.place(x=5, y=180)
rad2_2.place(x=60, y=180)
rad2_3.place(x=115, y=180)
rad2_4.place(x=170, y=180)
rad2_5.place(x=5, y=200)
rad2_6.place(x=60, y=200)
rad2_7.place(x=115, y=200)
rad2_8.place(x=170, y=200)

btn03 = Button(window, text="Скрыть",fg='#29a61e',bg="#3d3d3d",activebackground="yellow", width=25, command=hiding)
btn03.place(x=225, y=240)

btn13 = Button(window, text="Извлечь",fg='#29a61e',bg="#3d3d3d",activebackground="yellow", width=25, command=extraction)
btn13.place(x=600, y=240)

window.mainloop()
