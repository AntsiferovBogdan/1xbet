from tkinter import Button, END, Entry, Label, Tk, W
import re

root = Tk()
root.title('Название программы')

Label(root, text='Введите число').grid(row=3, sticky=W)


EntryA = Entry(root, width=10, font='Arial 14')  # создаем поля для "червяков"
Worm12 = Entry(root, width=38, font='Arial 14')
Worm15 = Entry(root, width=38, font='Arial 14')
Worm13 = Entry(root, width=38, font='Arial 14')
Worm10 = Entry(root, width=38, font='Arial 14')
Worm10_1 = Entry(root, width=38, font='Arial 14')

allert = Entry(root, width=10, font='Arial 14')   # и предупреждений

EntryA.grid(row=3, column=1, sticky=W)  # и размещаем на сетке
Worm12.grid(row=5, column=1)
Worm15.grid(row=6, column=1)
Worm13.grid(row=7, column=1)
Worm10.grid(row=8, column=1, padx=10, pady=0)
Worm10_1.grid(row=9, column=1, pady=0)
allert.grid(row=6, column=0)

space = Label(root, text="", bg="white", fg="white")  # необходимо для разрыва
space.grid(row=13, column=5)                          # между таблицами 2 и 3

x = Label(root, bg="white", fg="white")  # число, вылетевшее из червяка №3
x.grid(row=7, column=0)
x.config(width=1)

_1 = Label(root, text=" 3 6 \n2 5", bg="green", relief="groove")  # таблица от заказчика
_2 = Label(root, text=" 6 9 \n5 8", bg="green", relief="groove")
_3 = Label(root, text=" 9 12 \n8 11", bg="green", relief="groove")
_4 = Label(root, text=" 12 15 \n11 14", bg="green", relief="groove")
_5 = Label(root, text=" 15 18 \n14 17", bg="green", relief="groove")
_6 = Label(root, text=" 18 21 \n17 20", bg="green", relief="groove")
_7 = Label(root, text=" 21 24 \n20 23", bg="green", relief="groove")
_8 = Label(root, text=" 24 27 \n23 26", bg="green", relief="groove")
_9 = Label(root, text=" 27 30 \n26 29", bg="green", relief="groove")
_10 = Label(root, text=" 30 33 \n29 32", bg="green", relief="groove")
_11 = Label(root, text=" 33 36 \n32 35", bg="green", relief="groove")
_12 = Label(root, text=" 2 5 \n1 4", bg="green", relief="groove")
_13 = Label(root, text=" 5 8 \n4 7", bg="green", relief="groove")
_14 = Label(root, text=" 8 11 \n7 10", bg="green", relief="groove")
_15 = Label(root, text=" 11 14 \n10 13", bg="green", relief="groove")
_16 = Label(root, text=" 14 17 \n13 16", bg="green", relief="groove")
_17 = Label(root, text=" 17 20 \n16 19", bg="green", relief="groove")
_18 = Label(root, text=" 20 23 \n19 22", bg="green", relief="groove")
_19 = Label(root, text=" 23 26 \n22 25", bg="green", relief="groove")
_20 = Label(root, text=" 26 29 \n25 28", bg="green", relief="groove")
_21 = Label(root, text=" 29 32 \n28 31", bg="green", relief="groove")
_22 = Label(root, text=" 32 35 \n31 34", bg="green", relief="groove")

twins = []  # создаем таблицы 2 и 3
twins2 = []
c = 8
c_2 = 14
d = 4
for i in range(1, 37):
    square = Label(root, text=str(i), bg="green", height=1, font='Arial 14',
                   relief="groove", highlightcolor="black")
    square_2 = Label(root, text=str(i), bg="green", height=1, font='Arial 14',
                     relief="groove", highlightcolor="black")
    twins.append(square)
    twins2.append(square_2)
    square.config(width=4)
    square.grid(row=c, column=d)  # и размещаем их на сетке
    square_2.config(width=4)
    square_2.grid(row=c_2, column=d)
    if d == 15:
        d = 4
        c += 1
        c_2 += 1
    else:
        d += 1

square_list = [_1, _2, _3, _4, _5, _6, _7, _8, _9,  # также размещаем таблицу 1
               _10, _11, _12, _13, _14, _15, _16,   # на сетке
               _17, _18, _19, _20, _21, _22]

a = 5
b = 4
for i in square_list:
    i.grid(row=a, column=b)
    i.config(width=4, font="Arial 14")
    if b == 14:
        b = 4
        a += 1
    else:
        b += 1


def add(event):
    a = EntryA.get()  # получаем информацию из Ввода
    a = str(a)
    if a.isdigit() and 0 < int(a) < 37:  # проверяем ее
        allert.delete(0, END)
    else:
        allert.delete(0, END)
        allert.insert(0, "Ошибка!")
        EntryA.delete(0, END)
        return

    worm12 = Worm12.get()
    worm15 = Worm15.get()
    worm13 = Worm13.get()
    worm10 = Worm10.get()
    worm10_1 = Worm10_1.get()

    list_1 = worm12.split("|")  # операции для дальнейшего подсчета элементов
    list_2 = worm15.split("|")
    list_3 = worm13.split("|")
    list_4 = worm10.split("|")
    list_5 = worm10_1.split("|")

    seps_1 = re.findall(r"[|]", worm12)
    seps_2 = re.findall(r"[|]", worm15)
    seps_3 = re.findall(r"[|]", worm13)
    seps_4 = re.findall(r"[|]", worm10)
    seps_5 = re.findall(r"[|]", worm10_1)

    result = "|" + a

    if len(seps_1) < 12:  # проверяем, куда вставлять число
        Worm12.insert(0, result)
    else:
        if len(seps_2) >= 15:
            if len(seps_3) >= 13:
                if len(seps_4) >= 10:
                    if len(seps_5) >= 10:
                        x["text"] = str(list_5[-1])
                        Worm10_1.delete(len(worm10_1) - len(list_5[-1])-1, END)
                    Worm10.delete(len(worm10) - len(list_4[-1])-1, END)
                    Worm10_1.insert(0, "|" + list_4[-1])
                Worm13.delete(len(worm13) - len(list_3[-1])-1, END)
                Worm10.insert(0, "|" + list_3[-1])
            Worm15.delete(len(worm15) - len(list_2[-1])-1, END)
            Worm13.insert(0, "|" + list_2[-1])
        Worm12.delete(len(worm12) - len(list_1[-1])-1, END)
        Worm15.insert(0, "|" + list_1[-1])
        Worm12.insert(0, result)
    EntryA.delete(0, END)
    for i in square_list:  # и последующее окрашивание введенного числа
        nums = i["text"].split(" ")
        caret = nums[3].split("\n")
        nums[3] = caret[1]
        if a in nums:
            i["bg"] = "red"

    for i in twins:
        nums = i["text"]
        if a == nums:
            i["bg"] = "red"

    for i in twins2:
        nums = i["text"]
        if a == nums:
            i["bg"] = "red"

    worm12 = Worm12.get()
    worm15 = Worm15.get()
    worm13 = Worm13.get()
    worm10 = Worm10.get()
    worm10_1 = Worm10_1.get()

    list_1 = worm12.split("|")
    if list_1[0] == "":
        del list_1[0]
    list_2 = worm15.split("|")
    if list_2[0] == "":
        del list_2[0]
    list_3 = worm13.split("|")
    if list_3[0] == "":
        del list_3[0]
    list_4 = worm10.split("|")
    if list_4[0] == "":
        del list_4[0]
    list_5 = worm10_1.split("|")
    if list_5[0] == "":
        del list_5[0]
    full_list_1 = list_1 + list_2 + list_3
    full_list_2 = list_1 + list_2 + list_3 + list_4
    full_list_3 = list_1 + list_2 + list_3 + list_4 + list_5

    try:  # затем проверяем числа, которые "уехали" из 1 или 2 червяка
        if list_4[0].isdigit():
            check_13 = []
            for j in full_list_1:
                j = int(j)
                check_13.append(j)
            if int(list_4[0]) in check_13:
                print("дальше")
            else:
                for i in square_list:
                    nums = i["text"].split(" ")
                    caret = nums[3].split("\n")
                    nums[3] = caret[1]
                    del nums[0]
                    if list_4[0] in nums:
                        for num in nums:
                            if num in full_list_1:
                                i["bg"] = "red"
                                break
                            else:
                                i["bg"] = "green"
    except IndexError:
        pass

    try:
        if list_5[0].isdigit():
            check_4 = []
            for j in full_list_2:
                j = int(j)
                check_4.append(j)
            if int(list_5[0]) in check_4:
                print("дальше2")
            else:
                for t in twins:
                    num = int(t["text"])
                    if int(list_5[0]) == num:
                        t["bg"] = "green"
    except IndexError:
        pass

    try:
        if int(x["text"]) != 0:
            check_5 = []
            for j in full_list_3:
                j = int(j)
                check_5.append(j)
            if int(x["text"]) in check_5:
                print("дальше3")
            else:
                for t in twins2:
                    num = int(t["text"])
                    if int(x["text"]) == num:
                        t["bg"] = "green"
    except (NameError, ValueError):
        pass


root.bind("<Return>", add)  # ввод числа по нажатию на Enter


def delete():  # в данной функции все ананлогично функции add, но наоборот
    worm12 = Worm12.get()
    worm15 = Worm15.get()
    worm13 = Worm13.get()
    worm10 = Worm10.get()
    worm10_1 = Worm10_1.get()

    list_1 = worm12.split("|")
    if list_1[0] == "":
        del list_1[0]
    list_2 = worm15.split("|")
    if list_2[0] == "":
        del list_2[0]
    list_3 = worm13.split("|")
    if list_3[0] == "":
        del list_3[0]
    list_4 = worm10.split("|")
    if list_4[0] == "":
        del list_4[0]
    list_5 = worm10_1.split("|")
    if list_5[0] == "":
        del list_5[0]

    seps_1 = re.findall(r"[|]", worm12)
    seps_3 = re.findall(r"[|]", worm13)
    seps_4 = re.findall(r"[|]", worm10)
    seps_5 = re.findall(r"[|]", worm10_1)

    global y
    y = list_1[0]
    if len(seps_1) < 12:
        Worm12.delete(0, len(list_1[0])+1)
    else:
        if len(seps_3) >= 1:
            if len(seps_4) >= 1:
                if len(seps_5) >= 1:
                    if x["text"] != "":
                        Worm10_1.insert(len(worm10_1), "|"+x["text"])
                    Worm10.insert(len(worm10), "|"+list_5[0])
                    Worm10_1.delete(0, len(list_5[0])+1)
                Worm13.insert(len(worm13), "|"+list_4[0])
                Worm10.delete(0, len(list_4[0])+1)
            Worm15.insert(len(worm15), "|"+list_3[0])
            Worm13.delete(0, len(list_3[0])+1)
        Worm12.delete(0, len(list_1[0])+1)
        Worm12.insert(len(worm12), "|"+list_2[0])
        Worm15.delete(0, len(list_2[0])+1)

    worm12 = Worm12.get()
    worm15 = Worm15.get()
    worm13 = Worm13.get()
    worm10 = Worm10.get()
    worm10_1 = Worm10_1.get()

    list_1 = worm12.split("|")
    list_2 = worm15.split("|")
    list_3 = worm13.split("|")
    list_4 = worm10.split("|")
    list_5 = worm10_1.split("|")

    list_1 = worm12.split("|")
    if list_1[0] == "":
        del list_1[0]
    list_2 = worm15.split("|")
    if list_2[0] == "":
        del list_2[0]
    list_3 = worm13.split("|")
    if list_3[0] == "":
        del list_3[0]
    list_4 = worm10.split("|")
    if list_4[0] == "":
        del list_4[0]
    list_5 = worm10_1.split("|")
    if list_5[0] == "":
        del list_5[0]

    full_list_1 = list_1 + list_2 + list_3
    full_list_2 = list_1 + list_2 + list_3 + list_4
    full_list_3 = list_1 + list_2 + list_3 + list_4 + list_5

    for i in square_list:
        nums = i["text"].split(" ")
        caret = nums[3].split("\n")
        nums[3] = caret[1]
        del nums[0]
        if y in full_list_1:
            print("все четко")
        elif y in nums:
            for num in nums:
                if num in full_list_1:
                    i["bg"] = "red"
                else:
                    i["bg"] = "green"
        try:
            if list_3[-1] in nums:
                i["bg"] = "red"
        except (NameError, IndexError):
            pass

    for t in twins:
        num = int(t["text"])
        if y in full_list_2:
            print("все четко 2")
        elif int(y) == num:
            t["bg"] = "green"
        try:
            if int(list_4[-1]) == num:
                t["bg"] = "red"
        except (NameError, IndexError):
            pass

    for t in twins2:
        num = int(t["text"])
        if y in full_list_3:
            print("все четко 3")
        elif int(y) == num:
            t["bg"] = "green"
        try:
            if int(list_5[-1]) == num:
                t["bg"] = "red"
        except (NameError, IndexError):
            pass


but = Button(root, text='Добавить', command=add)  # размещение главных кнопок
but.grid(row=4, column=0, sticky=W)

but2 = Button(root, text='Удалить', command=delete)
but2.grid(row=5, column=0, sticky=W)

root.mainloop()

y = 0
