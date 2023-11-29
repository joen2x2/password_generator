import tkinter
import random

number_of_symbols = 8 #записывается в показатель width;можно указать желаемое кол-во символов

#Скачать с карточки ----------------------------------------------------------#
def generate(number_of_symbols=6):
    import random
    symbols = []
    for i in range(number_of_symbols):
        num = random.randint(1, 3)
        if num == 1:
            symbols.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        elif num == 2:
            symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        elif num == 3:
            symbols.append(random.choice('0123456789'))
    password = ''.join(str(symb) for symb in symbols)
    text.delete('1.0', tkinter.END)
    text.insert('1.0', password)
#----------------------------------------------------------------------------#
    
window = tkinter.Tk()#TK() создает окно.
window.config(bg="black")#фон основного окна
window.geometry("800x600")#размер окна
window.title("Password Generator")#имя в окне

text = tkinter.Text(
    font=("arial", 40, "bold"), #семейство шрифта,размер px,выделение
    height=1, #высота текстового поля не больше 1 символа
    width=number_of_symbols + 1, #ширина подстраивается под длину пароля
    bg="blue",# фон поля ввода
    fg="white",#цвет текста
    borderwidth=10#толщина границы
)#создать текстовое поле
text.pack(expand=1)#отобразить текстовое поле;expand-распологает поле по центру

#Видео 2 Создание кнопки генерации пароля -----------------------------------#
tkinter.Button(
    text="Generate",
    font=("arial", 40, "bold"),
    bg="green",
    fg="white",
    borderwidth=0,
    #command=generate генерирует пароль из 6 символов(по умолчанию)
    #command=generate(number_of_symbols) #неправильно,фун-я вызывается при отрисовке окна
    command=lambda: generate(number_of_symbols)#ссылка на функцию,а не результат ее работы
    ).pack(expand=1)


window.mainloop() #не дает окну закрываться,зацикливает прорисовку окна


