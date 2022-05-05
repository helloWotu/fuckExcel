import pandas as pd
import numpy as np
from operator import  itemgetter, attrgetter


def getFirstSored(file_path):
    df = pd.read_csv(file_path)
    # for rows_i in range(1, df.)

    # 查看有多少行
    # print(df.shape[0])

    # 查看有多少列
    # print(df.shape[1])

    # print(df.loc[1][2])
    rec_id_set = set()
    all_recver = []
    for row_i in range(1, df.shape[0]):
        # for col_i in range(0, df.shape[1]):
        #     nums = df.loc[row_i][col_i]
        rec_id = df.loc[row_i][3]
        rec_name = df.loc[row_i][4]
        rec_core = df.loc[row_i][8]
        recver = {
            'rec_id': rec_id,
            'rec_name': rec_name,
            'rec_core': rec_core
        }
        all_recver.append(recver)
        rec_id_set.add(rec_id)

    # 计算总金币
    sum_list = []
    for rec_id in rec_id_set:
        rec_name = ''
        rec_core = 0
        for recver in all_recver:
            if recver['rec_id'] == rec_id:
                rec_core += int(recver['rec_core'])
                rec_name = recver['rec_name']

        sum_rec = {
            '送礼人ID': rec_id,
            '送礼人名字': rec_name,
            '送礼金额': rec_core
        }
        sum_list.append(sum_rec)
        sum_list = sorted(sum_list, key=lambda x: x['送礼金额'], reverse=True)

    # print(sum_list)

    # df = pd.DataFrame(sum_list)
    # # 根据最高分数排序
    # df = df.sort_values(by=['送礼金额'], ascending=False)
    # df.to_csv('送礼统计.csv')
    return sum_list[0]