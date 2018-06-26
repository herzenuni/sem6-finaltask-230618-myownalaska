from tkinter import *
import functools
import pytest

def to_mess():
    mess.configure(text=change(int(box.get()),radio.get()))
    print(stole_oct(change)(int(box.get())))

def change(arg, radio):
    if radio == 'name':
        x = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
        if arg > 9 or arg < 0:
            text = 'Диапозон чисел от 0 до 9!  Sorry! '
        else:
            text=x[arg]
    if radio == 'bin':
        if arg < 0:
            text=('-'+bin(arg)[3:])
        else:
            text = bin(arg)[2:]
    if radio == 'oct':
        if arg < 0:
            text = ('-' + oct(arg)[3:])
        else:
            text = oct(arg)[2:]
    if radio == 'hex':
        if arg < 0:
            text=('-'+hex(arg)[3:])
        else:
            text = hex(arg)[2:]
    return text

def stole_oct(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(args[0], 'oct')
    return inner

root = Tk()
root.geometry("500x250")
root.title("DECO")
Helvetica = "-family {Helvetica} -size 14 -weight bold " \
            "-slant roman -underline 0 -overstrike 0"
radio = StringVar()
radio.set('name')
box = Spinbox(root, from_=0, to=9, width=45, font=Helvetica)
box.place(relx=0.12, rely=0.18, relheight=0.08, relwidth=0.09)

digit = Radiobutton(root, text='''Цифра''', font=Helvetica, variable=radio, value='name')
digit.place(relx=0.1, rely=0.3, relheight=0.16, relwidth=0.25)

bin_int = Radiobutton(root, text='''BIN''', font=Helvetica, variable=radio, value='bin')
bin_int.place(relx=0.077, rely=0.45, relheight=0.16, relwidth=0.15)

oct_int = Radiobutton(root, text='''OCT''', font=Helvetica, variable=radio, value='oct')
oct_int.place(relx=0.081, rely=0.6, relheight=0.16, relwidth=0.15)

hex_int = Radiobutton(root, text='''HEX''', font=Helvetica, variable=radio, value='hex')
hex_int.place(relx=0.081, rely=0.75, relheight=0.16, relwidth=0.15)

mess = Message(root, width=290, text='''Название''', font=Helvetica)
mess.place(relx=0.38, rely=0.04, relheight=0.55, relwidth=0.58)

transform = Button(root, text='''Преобразовать''', font=Helvetica, command=to_mess)
transform.place(relx=0.6, rely=0.67, height=40, width=139)


root.mainloop()

@pytest.mark.parametrize("a,b,expected", [
    (-7, 'name', 'Диапозон чисел от 0 до 9!  Sorry! '),
  (7, 'name', 'Семь'),
    (33, 'name', 'Диапозон чисел от 0 до 9!  Sorry! '),
    (-3, 'bin', '-11'),
  (5, 'bin', '101'),
    (-16, 'oct', '-20'),
    (9, 'oct', '11'),
    (-15, 'hex', '-f'),
  (0, 'hex', '0'),
    (11, 'hex', 'b')
])
def testik(a, b, expected):
    assert change(a, b) == expected