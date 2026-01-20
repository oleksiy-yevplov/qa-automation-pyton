#1 варіант - імпорт цілого модуля
#спершу вбудовані модулі
import math
import json

#друга група - ті, які потрібно інсталювати (модулі з віртуал енв)
import pytest
import requests

#третя група - власні модулі
import imported_modules
result = imported_modules.sum_two_num(3, 5)
avg = imported_modules.average([1, 2, 3])
triangle = imported_modules.Triangle(10, 60)
print(result, avg, triangle.side, triangle.alpha, triangle.beta) 



#2 варіант - імпорт чогось конкретного
#спершу вбудовані модулі
from math import pi
from pathlib import Path

#друга група - ті, які потрібно інсталювати (модулі з віртуал енв)
from requests import get

#третя група - власні модулі
from imported_modules import sum_numbers, Triangle

res = sum_numbers("1,2,3")
tri = Triangle(5, 30)
print(res, tri.side, tri.alpha, tri.beta)


#3 варіант - імпорт сам не знаю чого
#спершу вбудовані модулі
from math import *
from random import *

#друга група - ті, які потрібно інсталювати (модулі з віртуал енв)
from pytest import *
from requests import *

#третя група - власні модулі
from imported_modules import *

res1 = sum_two_num(2, 4)
res2 = average([10, 20, 30])
table = multiplication_table(5)
tri = Triangle(7, 45)
print(res1, res2, table, tri.side, tri.alpha, tri.beta)


#4 варіант імпорт через псевдонім
#спершу вбудовані модулі
import datetime as dt
from math import sqrt as square_root

#друга група - ті, які потрібно інсталювати (модулі з віртуал енв)
import numpy as np
from requests import post as send_post

#третя група - власні модулі
import imported_modules as im

res = im.sum_two_num(1, 2)
avg = im.average([2, 4, 6])
print(res, avg, tri.side, tri.alpha, tri.beta)
