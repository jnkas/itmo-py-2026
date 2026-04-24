
from pathlib import Path
from datetime import datetime, date
import json

habits = []

DATA_PATH = Path(__file__).parent / "data.json"

# print(DATA_PATH)


# читает json и возвращает  list []
def read_data():
    if not DATA_PATH.exists():
        return []
    
    with DATA_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)
        return data

# сохраняет json и возвращает сообщение об успехе
def save_data(habits):
    with DATA_PATH.open("w", encoding="utf-8") as file:
        json.dump(habits, file, ensure_ascii=False, indent=4)
    
#Создает привычку. возвращет {id, title, crated_at, done}
def create_habit(title):
    return {
        "id": int(datetime.now().timestamp()% 10000),
        "title": title,
        "crated_at": date.today().isoformat(),
        "done": []
    }
    

def del_habit():
    pass
    #удаляет привычку

def statistics():
    pass
    # формирует статистику выдает {
    # "total":int, 
    # done_today:int, 
    # percent:float, 
    # left:int
    # }

def toggle_done():
    pass
    #переключает статус - выполнено сегодня или нет