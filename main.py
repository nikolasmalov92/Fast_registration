import os
import random
import psutil
import time
from pywinauto import Application
import subprocess 
import sys

app = Application(backend='uia')

print('\n***** Добро пожаловать *****\n')


# Функция запуска утилиты 'SetLit.exe'
def running(cmd):
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    proc.communicate()


# Cмена литеры радиоустройства
def cmd_lit():
    command = '7'    
    time.sleep(2)
    cmd = 'SetLit.exe {} {} '.format(int(command), int(lit))    
    running(cmd)
    for remaining in range(3, 0, -1):
        sys.stdout.write('\r')
        sys.stdout.write('-- Идёт установка литеры {:2d} сек '.format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write(f'\r-- Литера выбрана\n')

coordinator = input('-- Введите тип/номер координатора(РР РИМ или МРР-РИМ): ')

lit = input('-- Введите литеру(Например 1): ')
cmd_lit()
print('-- Список радиоустройств: ')
type_device_list = ('\t1. Астра-3321-CMK ','\t2. Астра-6131-AK ', '\t3. Астра-5131-ИК ', '\t4. Астра-421-ИП ',
               '\t5. Астра-КТСУ ', '\t6. Астра-ДП ','\t7. Астра-3321-РПДУ ', '\t8. Астра–8-ИКА ', '\t9 Астра-361-ДУВ ', 
               '\t10. Астра-3221-КТС ', '\t11. Астра-3731-ИТ ')
for j in type_device_list:
    print(j)
t_device = input('-- Введите тип радиоустройства из списка: ')
time.sleep(1)
print('-- Уберите руки от клавиатуры/мыши')
time.sleep(1)
print('-- Сходите за кофе, дальше вашу работу выполнит БОТ-Семён\n')
time.sleep(5)


# open Pconf-pro
def RunApplication():   
    global_path = r'C:\Program Files (x86)\TEKO'       
    for root, dirs, files in os.walk(global_path):
        for file in files:
            if file.endswith("Pconf-Pro.exe"):
                print('-- Pconf-Pro найден')
                path_file = os.path.join(root,file)    
    new_path = path_file
    app.start(new_path)
    time.sleep(3)
    assertion_msg = '-- Pconf-Pro не запустился!'
    assert psutil.pid_exists(app.process), assertion_msg
    process = psutil.Process(app.process)
    print('-- Pconf-Pro запущен!')
    time.sleep(2)
    global main_windows_pconf
    main_windows_pconf = app.Dialog 
    


# Поиск окна программы Pconf-Pro
def open_app():
    title_window = ''
    name_app = 'Pconf-Pro'
    try: 
        new_sl = main_windows_pconf.texts()
        str1 = ''.join(new_sl)
        if str1 == title_window:
            print(f'-- Открылось окно "{name_app}"')            
    except:
        print(f'-- Окно "{title_window}" не открылось!')
    time.sleep(1)


# Поиск кнопки меню и нажатие на эту кнопку
def main_menu_button(title_menu_button):
    menu_btn = main_windows_pconf.descendants(control_type="MenuItem")
    temp = 0
    msg = '-- Не найдено значение'
    count = 0
    for child in menu_btn:
        count += 1
        new_child = child.texts()
        text_str = ''.join(new_child)            
        if title_menu_button == text_str:
            menu_btn[count - 1].click_input()             
            temp = 1
    if temp == 1:
        print(f'-- Нажата кнопка меню "{title_menu_button}"')    
    else:
        assert title_menu_button is False, msg
    time.sleep(1)


# Поиск кнопки подменю и нажатие на эту кнопку
def slave_menu_button(title_sub_menu_button):
    sub_menu_btn = main_windows_pconf.descendants(control_type="MenuItem")
    temp = 0
    msg = '-- Не найдено значение'
    count = 0
    for child in sub_menu_btn:
        count += 1
        new_child = child.texts()
        text_str = ''.join(new_child)            
        if title_sub_menu_button == text_str:
            sub_menu_btn[count - 1].click_input()            
            temp = 1
    if temp == 1:
        print(f'-- Нажата кнопка подменю "{title_sub_menu_button}"')           
    else:
        assert title_sub_menu_button is False, msg
    time.sleep(1)


# Поиск кнопки
def ElementButton(title_button):
    button = main_windows_pconf.descendants(control_type="Button")
    temp = 0
    msg = '-- Кнопка не найдена'
    count = 0
    for child in button:
        count += 1
        new_child = child.texts()
        text_str = ''.join(new_child)            
        if title_button == text_str:
            button[count - 1].click_input()             
            temp = 1
    if temp == 1:
        print(f'-- Нажата кнопка "{title_button}"')    
    else:
        assert title_button is False, msg
    time.sleep(1)


# Поиск и выбор виджета
def Widget(title_widget):
    widget_element = main_windows_pconf.descendants(control_type="CheckBox")
    count = 0
    temp = 0
    msg = '-- Виджет не найден'
    count = 0
    for child in widget_element:
        count += 1
        new_child = child.texts()
        text_str = ''.join(new_child)            
        if title_widget == text_str:
            widget_element[count - 1].click_input()             
            temp = 1
    if temp == 1:
        print(f'-- Выбран виджет: "{title_widget}"')    
    else:
        assert title_widget is False, msg
    time.sleep(2)


# Авторизация
def Authorization(title_passw):
    engineer_password = main_windows_pconf
    print(f'-- Происходит ввод пароля: "{title_passw}"')
    engineer_password.Edit.click_input()
    engineer_password.Edit.type_keys(title_passw)
    time.sleep(2)
    if int(title_passw) == 123456:
        engineer_password.Edit.type_keys('{ENTER}')
        print('-- Вход в систему произведён инженером ')
    else:
        assert title_passw is False, f'-- Пароль "{title_passw}" не верный! '
    time.sleep(3)


# Ожидание статус бара
def StateStatusBar(title_status_bar, timer):
    state_status = main_windows_pconf.descendants(control_type="Text")
    count = 0
    temp = 0
    msg = '-- Статус сообщения не найден '
    count = 0
    for child in state_status:
        count += 1
        new_child = child.texts()
        text_str = ''.join(new_child)            
        if title_status_bar == text_str:
            state_status[count - 1].click_input()             
            temp = 1
    if temp == 1:
        print(f'-- Статус: "{title_status_bar}"')    
        print(f'-- Ожидание переключение статуса: {title_status_bar}')
        time.sleep(int(timer))
    else:
        assert title_status_bar is False, msg
    time.sleep(2)


# В тулбаре ищем кнопку "Оборудование"
def step_impl_search_toolbar(title_toolbar):
    time.sleep(2)
    toolbar = app.Dialog.descendants(control_type="CheckBox")
    count = 0
    for child in toolbar:
        count += 1
        for text in child.texts():
            if text == title_toolbar:
                toolbar[count-1].click_input()
                print(f'-- Выбор вкладки {title_toolbar}')
    time.sleep(2)


# Поиск устройства в списке
def Element_treeitem_device(title_treeitem_device):  
    treeItem_item = main_windows_pconf.descendants(control_type="TreeItem")
    temp = 0
    msg = f'-- Устройство с таким наименованием {title_treeitem_device} не найдено'   
    count = 0
    for child in treeItem_item:
        count += 1
        new_child = child.texts()
        str1 = ''.join(new_child)        
        if title_treeitem_device in str1:
            t1 = str1                    
            treeItem_item[count - 1].click_input()   
            temp = 1
            break  
    if temp == 1:
        print(f'-- Выбрано устройство: "{t1}"')  
    else:
        assert title_treeitem_device is False, msg
time.sleep(2)


# Запуск регистрации радиостройство(рим односторонний)
def cmd_reg(number_ser):    
    if t_device == '1':
        type_device_6 = 0b10111000
    elif t_device =='2':
        type_device_6 = 0b10101000
    elif t_device =='3':
        type_device_6 = 0b11001000
    elif t_device =='4':
        type_device_6 = 0b11011000
    elif t_device =='5':
        type_device_6 = 0b10001100
    elif t_device =='6':
        type_device_6 = 0b10011100
    elif t_device =='7':
        type_device_6 = 0b00011000
    elif t_device =='8':
        type_device_6 = 0b00111000
    elif t_device =='9':
        type_device_6 = 0b01001000
    elif t_device =='10':
        type_device_6 = 0b01111000
    elif t_device =='11':
        type_device_6 = 0b101011000
    else:
        pass    
    time.sleep(2)
    length = 0b00001001
    sync_old = 0b10000110   
    k = number_ser + n     
    s_Num_5 = 0b11110010
    state_device_7 = 0b10000000
    byte_8 = 0b00000000
    crc_byte_9 = 0b00000000
    crc_byte_10 = 0b01010101        
    random_sync = random.randint(0b01101110, 0b11000111)
    increment_sync = random_sync + 1
    new_sync = increment_sync
    cmd = 'SetLit.exe {} {} {} {} {} {} {} {} {} {}'.format(length, new_sync, sync_old,
                                                                    k, s_Num_5, type_device_6, state_device_7,
                                                                    byte_8, crc_byte_9, crc_byte_10 )
    
    print("-- Регистрация радиоустройства: ", cmd)
    running(cmd)
    time.sleep(2)


# Множественная регистрация радиоустройств 
def fast_reg():
    print(f'-- Выбран координатор {coordinator}')
    global n
    n = 0
    while n < 191:                           
        Element_treeitem_device(f'{coordinator}')
        ElementButton('Добавить устройство в радиосеть')
        ElementButton('OK')
        cmd_reg(0b10011110)
        for remaining in range(3, 0, -1):
            sys.stdout.write('\r')
            sys.stdout.write('-- Идёт регистрация радиоустройств {:2d} сек\n'.format(remaining))
            sys.stdout.flush()
            time.sleep(1)
            n += 1
    sys.stdout.write('\r-- -- Зарегистрировано 192 извещателя\n')
    os.system('pause')
    time.sleep(1)
 

RunApplication()
main_menu_button('ППКОП')    
slave_menu_button('Подключиться к ППКОП...')
ElementButton('OK')
StateStatusBar('Чтение конфигурации из ППКОП.', 12)
Authorization(123456)
Widget('Оборудование')
fast_reg()

   

