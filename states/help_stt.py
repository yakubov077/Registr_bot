from aiogram.fsm.state import State, StatesGroup

class Help(StatesGroup):
    help = State()

from aiogram.fsm.state import State, StatesGroup

class Registor(StatesGroup):
    ism = State() 
    familiya = State() 
    tel = State()