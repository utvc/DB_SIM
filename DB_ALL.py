# -*- coding: UTF-8 -*-
import random
import sys

ZY = sys.argv[1]
ZJ = sys.argv[2]

dict_BW0 = {0: '饰品', 1: '护腕', 2: '手套', 3: '腰带', 4: '裤子', 5: '鞋子', 6: '戒指', 7: '主手', 8: '副手', 9: '双手武器'}
dict_BW1 = {0: '饰品', 1: '护腕', 2: '手套', 3: '腰带', 4: '裤子', 5: '鞋子', 6: '戒指', 7: '主手', 8: '副手'}
dict_BW2 = {0: '饰品', 1: '护腕', 2: '手套', 3: '腰带', 4: '裤子', 5: '鞋子', 6: '戒指', 7: '双手武器'}

dict_FS = {0: '闪避', 1: '吸血', 2: '挨打全能', 3: '触发精通', 4: '触发急速', 5: '暴击+暴击', 6: '渠道全能', 7: '渠道急速', 8: '渠道精通', 9: '渠道暴击', 10: '爆伤', 11: '无尽之星', 12: '触须', 13: '暮光炮', 14: '虚空回响', 15: '虚空仪式', 16: '真相', 17: '须臾洞察', 18: '龟裂创伤'}
dict_LV = {0: '1级', 1: '2级', 2: '3级'}
DB = '大米低保开出了：'
if ZJ in 'HF PH HY BS AS SS JL AY HM TK EM YS':
    random_BW = random.randint(0, 9)
    dict_BW = dict_BW0
elif ZJ in 'FY ZQ KT MR CS FC HJ TF NQ':
    random_BW = random.randint(0, 8)
    dict_BW = dict_BW1
elif ZJ in 'WQ KB CJ XX XE SJ SW SC JX ZW SH YX':
    random_BW = random.randint(0, 7)
    dict_BW = dict_BW2

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
    SP1 = random.randint(0, 8)
    if SP1 == 1:
        if ZY in 'FS MS SS':
            DB = DB + '而且是超线程护腕！'

if random_BW == 0:
    SP2 = random.randint(0, 8)
    if SP2 == 1:
        if ZJ in 'SJ SW SC ZQ KT MR CS HJ TF YX':
            DB = DB + '无敌！是点金手！'
        elif ZJ in 'FY WQ KB CJ XX BS XE':
            DB = DB + '无敌！是大红按钮，越按越有！'

if random_BW == 9:
    SP3 = random.randint(0, 8)
    if ZJ in 'YS HF ZW PH HY BS AS SS JL AY HM TK EM':
        if SP3 == 1:
            DB = DB + '无敌！是海风！'
        elif SP3 == 2:
            DB = DB + '无敌！是神经突触强化器！'

print(DB)
