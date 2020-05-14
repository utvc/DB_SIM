# -*- coding: UTF-8 -*-
import random

dict_BW = {0: '饰品', 1: '护腕', 2: '手套', 3: '腰带', 4: '裤子', 5: '鞋子', 6: '戒指', 7: '主手', 8: '副手', 9: '双手武器'}
dict_FS = {0: '闪避', 1: '吸血', 2: '挨打全能', 3: '触发精通', 4: '触发急速', 5: '暴击+暴击', 6: '渠道全能', 7: '渠道急速', 8: '渠道精通', 9: '渠道暴击', 10: '爆伤', 11: '无尽之星', 12: '触须', 13: '暮光炮', 14: '虚空回响', 15: '虚空仪式', 16: '真相', 17: '须臾洞察', 18: '龟裂创伤'}
dict_LV = {0: '1级', 1: '2级', 2: '3级'}
DB = '大米低保开出了：'

random_BW = random.randint(0, 9)
if random_BW == 0:
    DB = DB + dict_BW[random_BW] + '！'
elif 0 < random_BW <= 9:
    random_LV = random.randint(0, 2)
    if random_LV == 0:
        random_FS = random.randint(0, 18)
        DB = DB + dict_LV[random_LV] + '/' + dict_FS[random_FS] + '/' + dict_BW[random_BW] + '！'
    elif random_LV == 1:
        random_FS = random.randint(0, 16)
        DB = DB + dict_LV[random_LV] + '/' + dict_FS[random_FS] + '/' + dict_BW[random_BW] + '！'
    else:
        random_FS = random.randint(0, 15)
        DB = DB + dict_LV[random_LV] + '/' + dict_FS[random_FS] + '/' + dict_BW[random_BW] + '！'

if random_BW == 1:
    random.randint(0,20)
    if random.randint == 1:
        DB = DB + '而且是超线程护腕！'

print(DB)
