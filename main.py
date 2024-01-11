
from csv import DictReader, DictWriter
from os.path import exists
class LenNumberError:
    def __init__(self, txt):
        self.txt = txt
        
        
def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    is_valid_number = False
    while not is_valid_number:
        try: 
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number))!= 11:
                print("Невалидная длина")
            else:
                
                is_valid_number = True
        except ValueError:
            print("Невалидный номер")
            continue
        except:
            print
            continue
    return[first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя','Фамилия','Телефон'])
        f_writer.writeheader()
def create_file(file_name_copy):
    with open(file_name_copy, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя','Фамилия','Телефон'])
        f_writer.writeheader()
        
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
    
def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el['телефон'] == str(user_data[2]):
            print("Такой пользователь уже существует")
            return
    obj = {'имя': user_data[0], 'фамилия': user_data[1], 'телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def copy_data(file_name, file_name_copy, line_number):
    line_number = int(input("введите строчку, которую хотите копировать: "))     ### строчка для копирования
    res = read_file(file_name)
    with open(file_name_copy, 'a', encoding='utf-8', newline='') as copy_data:
        f_writer = DictWriter(copy_data, fieldnames=['имя', 'фамилия', 'телефон'])
        if line_number <= len(res):
            f_writer.writerow(res[line_number - 1])

  
file_name = 'phone.csv'
file_name_copy = 'phone2.csv'

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print("Файл не создан. Создайте его.")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            
            if not exists(file_name_copy):
                create_file(file_name_copy)
            copy_data(file_name, file_name_copy,1)
            
           
            
           
           
           
            
            
main()
