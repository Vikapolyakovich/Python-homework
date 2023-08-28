from alhoritm import *
from work_w_file import *

import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

while True:
    clear()
    print_instructions()
    choose(input("Введите команду: "))
    input("Введите enter чтобы продолжить")