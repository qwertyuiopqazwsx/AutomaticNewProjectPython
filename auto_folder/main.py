import os
import time
import threading
from modules. class_errors import AutomaticError

MY_DIRECTORY = f"C:\\Users\\ogurec\\Desktop\\Artyom\\IT"

class Check:
    """Класс, предназначенный для работы с пользователем. Используется для выбора пользователем нужного каталога."""
    def __init__(self) -> None:
        self.directory = MY_DIRECTORY
        self.check_directory = True
        self.start_animations = False
        self.exit = True
        while self.exit:
            while self.check_directory:
                os.system("cls")
                self.catalog = os.listdir(path=f'{self.directory}')
                self.catalog = [i for i in self.catalog  if os.path.isdir(self.directory+"\\"+i)] + ['Вернуться назад', 'Остаться здесь']
                print('\nВыберите папку | Select a folder:', ''.join([f'\n{i+1}. {folder}' for i, folder in enumerate(self.catalog)]))
                activity = self.get_user_select_catalog(lenght=len(self.catalog))
                if activity == False:
                    self.check_directory = False
                elif activity == True:
                    self.del_user_directory()
            self.create_files()
        

    def create_files(self):
        os.system("cls")
        tasks = ['Создать каталог', 'main.py, start.bat', 'Выбрать другой каталог']
        print('\nВыберите что создать:', ''.join([f'\n{i+1}. {task}' for i, task in enumerate(tasks)]))
        user_select_files = self.get_user_select_files(len(tasks))

        #anim = threading.Thread(target=self.animations, args=())

        if user_select_files == 1:
            os.system('cls')
            name_new_catalog = str(input('\nВведите имя нового каталога: '))
            self.start_animations = True
            #anim.start()
            self.directory = f'{self.directory}\\{name_new_catalog}'
            os.mkdir(path=f'{self.directory}')
            self.start_animations = False

        elif user_select_files == 2:
            self.start_animations = True
            #anim.start()
            
            os.chdir(f'{self.directory}')
            with open('main.txt', 'w') as f:
                f.write(f'#import\n\nclass Name:\n\tdef __init__(self) -> None:\n\t\t...')
            os.rename("main.txt", "main.py")

            with open('start.txt', 'w') as f:
                f.write(f'python main.py\nPAUSE')
            os.rename("start.txt", "start.bat")

            self.start_animations = False
            
        elif user_select_files == 3:
            self.check_directory = True
            return

        os.system('cls')

        print('\nВаши файлы созданы!')
        print('Выберите, что делать далее?\n1. Выйти из программы\n2. Создать новые файлы')
        ahead = int(input('\n'))
        if ahead not in range(1, 3):
            raise AutomaticError("Введите корректный номер каталога! | Yoy need correct input number catalog")
        
        if ahead == 1:
            self.exit = False
        elif ahead == 2:
            return


    def get_user_select_files(self, lenght):
        user_select = int(input('\n'))
        if user_select not in range(lenght+1):
            raise AutomaticError("Введите корректный номер каталога! | Yoy need correct input number catalog")
        return user_select
        

    def del_user_directory(self):
        change_directory = self.directory.split('\\')[:-1]
        self.directory = '\\'.join(change_directory)

    def get_user_select_catalog(self, lenght: int) -> bool:
        user_select = int(input('\n'))
        if user_select not in range(lenght+1):
            raise AutomaticError("Введите корректный номер каталога! | Yoy need correct input number catalog")
        if lenght-user_select == 1 or lenght-user_select == 0:
            return lenght-user_select
        self.directory = self.directory + f'\\{self.catalog[user_select-1]}'

    def animations(self):
        while self.start_animations:
            for i in range(1, 4):
                os.system("cls")
                print(f"\nСоздаю файлы {'.'*i}")
                time.sleep(0.1)

check = Check()
#print(check)




