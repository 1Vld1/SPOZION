import socket
import threading
import datetime
import task_card as tc
import vosk

task1 = tc.TaskCard()
viewed_cards = []
not_viewd_cards = []
#tc.set_card(author='Начальник')
#alias = tc.convert_to_string()


# Удаляет карточку из списка просмотренных карточек, если она со статусом "ready"
def del_task_if_ready(task):
    if task.status == "ready":
        index = 0
        for elem in viewed_cards:
            flag = tc.compare_cards(task, elem)
            if not flag:
                del viewed_cards[index]
            index += 1


def boss_menu():
    action = 1
    while action != 0:
        action = int(input("\n***Меню начальника***\nЧто вы хотите сделать?\n0.Выйти\n1.Создать карточку\n" +
                           "2.Посмотреть новые задачи\n3.Посмотреть все задачи\n4.Обновить\n>"))
        if action == 1:  # Создание карточки
            newTask = tc.TaskCard()
            newTask.set_card(alias)
            sor.sendto(("card," + alias + newTask.convert_to_string()).encode('utf-8'), server)
        if action == 2:  # Просмотр новых карточек
            if len(not_viewd_cards) == 0:
                print("У вас нет новых не прочитанных задач!")
            else:
                index = 0
                for elem in not_viewd_cards:
                    elem.print()
                    viewed_cards.append(elem)
                    del not_viewd_cards[index]
                    index += 1
        if action == 3:  # Просмотр всех карточек
            for elem in viewed_cards:
                elem.print()
            if len(not_viewd_cards) == 0:
                print("У вас нет новых не прочитанных задач!")
            else:
                index = 0
                for elem in not_viewd_cards:
                    elem.print()
                    del not_viewd_cards[index]
                    viewed_cards.append(elem)
                    index += 1
        if action == 4:
            sor.sendto(("spam").encode('utf-8'), server)
            data = sor.recv(1024)
            data = data.decode('utf-8')
            if data == "success":
                data = ''
            elif data:  # Если карточка пришла
                newTask = tc.convert_string_to_card(data)  # Преобразование карточки из строки
                not_viewd_cards.append(newTask)
            if not data:  # если нет, создай дефолтную карточку
                newTask = tc.TaskCard()
        if action == 0:
            print("До скорых встреч!\n")
            break

        # Удаление выполненых карточек из списка просмотренных карточек
        for elem in viewed_cards:
            del_task_if_ready(elem)


def executor_menu(newTask):
    action = 1
    while action != 0:
        print("***Меню подчинённого***\n")
        answer = int(input("1.Просмотреть все задачи?\n2.Обновить\n3.Выйти\n>"))
        if answer == 1:
            if len(viewed_cards) == 0:
                print("У вас нет заданий!")
            for elem in viewed_cards:
                elem.print()
            if len(not_viewd_cards) != 0:
                print("Вам пришло новое задание!")
                newTask.print()
                print("Какой статус установить?\n1.read\n2.ready\n>")
                answer = int(input())
                if answer == 2:
                    newTask.set_status("ready")
                    del not_viewd_cards[len(not_viewd_cards) - 1]
                    viewed_cards.append(newTask)
                    sor.sendto(("card," + alias + newTask.convert_to_string()).encode('utf-8'), server)
                else:
                    newTask.set_status("read")
                    del not_viewd_cards[len(not_viewd_cards) - 1]
                    viewed_cards.append(newTask)
                    sor.sendto(("card," + alias + newTask.convert_to_string()).encode('utf-8'), server)
        if answer == 2:
            data = sor.recv(1024)
            data = data.decode('utf-8')
            if data == "success":
                data = ''
            elif data:
                newTask = tc.convert_string_to_card(data)  # Преобразование карточки из строки
                not_viewd_cards.append(newTask)
            if not data:
                newTask = tc.TaskCard()
        if answer == 3:
            print("До скорых встреч!\n")
            break


# Принятие запроса от сервера и отправка обратно
def read_sok():
    # Ожидание запроса от сервера
    data = sor.recv(1024)
    data = data.decode('utf-8')
    # кастыль с проверкой сообщения от сервера
    if data == "success":
        data = ''
    elif data: # Если карточка пришла
        newTask = tc.convert_string_to_card(data)  # Преобразование карточки из строки
        not_viewd_cards.append(newTask)
    if not data:  # если нет, создай дефолтную карточку
        newTask = tc.TaskCard()
    for gr in groups.split(','):  # проверка, к какой группе принадлежит текущий пользователь
        if gr == "chief":
            boss_menu()
        if gr == "executor":
            executor_menu(newTask)


obj = tc.TaskCard()
obj.set_card_by_voice('sheff')
obj.print()

server = '192.168.1.76', 65535 # Данные сервера
alias = "admin," # Вводим наш псевдоним
groups = 'chief,admin'
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0)) # Задаем сокет как клиент
sor.sendto(('autorize,'+ groups).encode('utf-8'), server)
# Уведомляем сервер о подключении
#potok = threading.Thread(target= read_sok)
#potok.start()



while 1 :
    read_sok()
    mensahe = input()
    sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)




