import random
from datetime import datetime

random_hour = random.randint(0,23)
random_minute = random.randint(0,59)
random_sec = random.randint(0,59)

date = datetime.now()
print(f"Приглашаю вас на собрание сегодня {date} в {} ")