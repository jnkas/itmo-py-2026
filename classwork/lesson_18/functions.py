
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

def add_habit(title):
    habits = read_data()
    for hb in habits:
        if hb["title"] == title:
            return False
    new_habit = create_habit(title)
    habits.append(new_habit)
    save_data(habits)
    return True


# add_habit("чистить зубы 2 раза в день")    

#удаляет привычку
def del_habit(id):
    habits = read_data()
    count = 0
    for hb in habits:
        if hb["id"] == id:
            break
        count +=1
    
    habits.pop(count)
    save_data(habits)
    

def statistics():
    habits = read_data()
    done_today_total = 0
    today = date.today().isoformat()
    for hb in habits:
        done = hb["done"]
        if today in done:
            done_today_total += 1
    
    percent = round((done_today_total / len(habits)) * 100, 1)

    left = len(habits) - done_today_total

    return {
        "total": len(habits),
        "done_today": done_today_total,
        "percent": percent,
        "left": left
    }

    # формирует статистику выдает {
    # "total":int, 
    # done_today:int, 
    # percent:float, 
    # left:int
    # }

def toggle_done(id):
    habits = read_data()
    today = date.today().isoformat()
    for hb in habits:
        if hb["id"] == id:
            done = hb["done"]
            print(done)
            if today in done:
                done.remove(today)
            else:
                done.append(today)
            break 
    save_data(habits)
    #переключает статус - выполнено сегодня или нет 