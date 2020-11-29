from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext

deadline = '22:30'
taskTextInput = 'Текст задания'
commentTextInput = 'Комментарий к заданию'
taskAuthor = 'Начальник'
taskType = ''
taskName = ''


def infoClicked():
    infoWindow = Tk()
    infoWindow.title('Информация о карточке')
    infoWindow.geometry('900x600')
    
    taskName = variable.get()
    secWinLbl = Label(infoWindow, text=taskName + ', выполнить до ' + deadline)
    secWinLbl.place(relx=.2, rely=0)
    taskWinLbl = Label(infoWindow, text='Задача:')
    taskWinLbl.place(relx=.2, rely=.05)
    commentWinLbl = Label(infoWindow, text='Комментарий к задаче:')
    commentWinLbl.place(relx=.2, rely=.4)
    taskAuthorLbl = Label(infoWindow, text='Задание выдал(-а): ' + taskAuthor)
    taskAuthorLbl.place(relx=.2, rely=.75)

    taskText = scrolledtext.ScrolledText(infoWindow, width=80, height=10)
    taskText.place(relx=.2, rely=.1)
    taskText.insert(INSERT, taskTextInput)
    commentText = scrolledtext.ScrolledText(infoWindow, width=80, height=10)
    commentText.place(relx=.2, rely=.45)
    commentText.insert(INSERT, commentTextInput)


def inputClicked():
    inputWindow = Tk()
    inputWindow.title('Ручное заполнение карточки')
    inputWindow.geometry('900x600')
    
    var = StringVar(inputWindow)
    typeList = ['Оповещение', 'Срочная задача', 'Постоянная задача']
    typeBox = Combobox(inputWindow, textvariable=var, values=typeList)
    typeBox.place(relx=.2, rely=.035)
    typeLbl = Label(inputWindow, text='Тип задачи')
    typeLbl.place(relx=.2, rely=.0)

    headerTxt=Entry(inputWindow, width=20)
    headerTxt.place(relx=.4, rely=.135)
    headerLbl = Label(inputWindow, text="Название задачи")
    headerLbl.place(relx=.2, rely=.135)

    descriptionTxt=Entry(inputWindow, width=50)
    descriptionTxt.place(relx=.4, rely=.2)
    descriptionLbl = Label(inputWindow, text="Описание задачи")
    descriptionLbl.place(relx=.2, rely=.2)

    commentTxt = Entry(inputWindow, width=50)
    commentTxt.place(relx=.4, rely=.265)
    commentLbl = Label(inputWindow, text="Комментарий к задаче")
    commentLbl.place(relx=.2, rely=.265)

    deadlineTxt = Entry(inputWindow, width=10)
    deadlineTxt.place(relx=.4, rely=.33)
    deadlineLbl = Label(inputWindow, text="Срок выполнения задачи, до")
    deadlineLbl.place(relx=.2, rely=.33)

    submitBtn = Button(inputWindow, text='Отправить карточку')
    submitBtn.place(relx=.5, rely=.5)


taskList = ['Задача 1', 'Задача 2', 'Задача 3']
mainWindow = Tk()
mainWindow.title('Создание карточки')
mainWindow.geometry('900x600')
mainWinLbl = Label(mainWindow, text='Активные задачи')
mainWinLbl.grid(column=0, row=0)

variable = StringVar(mainWindow)
mainCombo = Combobox(mainWindow, textvariable=variable, values=taskList)
mainCombo.current(1)
mainCombo.grid(column=0, row=1)

infoBtn = Button(mainWindow, text="Показать информацию \n по задаче", command=infoClicked)
infoBtn.place(relx=0, rely=.1)

inputBtn = Button(mainWindow, text="Создать задачу вручную", command=inputClicked)
inputBtn.place(relx=0, rely=.2)

mainWindow.mainloop()
