
import datetime

def logger(type_code, username, message, code, file):
    fd = open("test.log", 'at', encoding='utf-8')
    time = datetime.datetime.now()
    text = f"{type_code}: {code} : {time} : [{username}] {message} : {file} \n"
    fd.write(text)
    fd.close()
    

logger(type_code="WARNING",
        username="Иван",
       code=500,
       file=__file__,
       message="Произошла ошибка доступа"
    )