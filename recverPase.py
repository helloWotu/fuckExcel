import pandas as pd
import numpy as np

'''
作为送礼人分析收礼人分析，   土豪送给谁最多
'''

def getFirstSored(file_path):
    df = pd.read_csv(file_path)
    # for rows_i in range(1, df.)

    # 查看有多少行
    # print(df.shape[0])

    # 查看有多少列
    # print(df.shape[1])

    # print(df.loc[1][2])

    if df.shape[1] < 10:
        return []

    is_sender = True
    recver_id = df.loc[1][1]
    for row_i in range(2, df.shape[0]):
        this_recver_id = df.loc[row_i][1]
        if recver_id != this_recver_id:
            is_sender = False
            break

    if is_sender == False:
        return []


    rec_id_set = set()
    all_recver = []
    for row_i in range(1, df.shape[0]):
        # for col_i in range(0, df.shape[1]):
        #     nums = df.loc[row_i][col_i]
        send_id = df.loc[row_i][1]
        send_name = df.loc[row_i][2]
        rec_id = df.loc[row_i][3]
        rec_name = df.loc[row_i][4]
        rec_core = df.loc[row_i][8]
        recver = {
            'send_id': send_id,
            'send_name': send_name,
            'rec_id': rec_id,
            'rec_name': rec_name,
            'rec_core': rec_core
        }
        all_recver.append(recver)
        rec_id_set.add(rec_id)

    # 计算总金币
    sum_list = []
    for this_rec_id in rec_id_set:
        rec_core = 0
        rec_name = ''
        rec_id = ''
        send_id = ''
        send_name = ''
        # 遍历算出当前rec_id 所有的总金币
        for one_recv in all_recver:
            if one_recv['rec_id'] == this_rec_id:
                rec_core += int(one_recv['rec_core'])
                rec_name = one_recv['rec_name']
                rec_id = one_recv['rec_id']
                send_name = one_recv['send_name']
                send_id = one_recv['send_id']

        sum_rec = {
            '送礼人ID': send_id,
            '送礼人名字': send_name,
            '收礼人ID': rec_id,
            '收礼人名字': rec_name,
            '送礼总金额': rec_core
        }
        sum_list.append(sum_rec)
        sum_list = sorted(sum_list, key=lambda x: x['送礼总金额'], reverse=True)

    # print(sum_list)

    # df = pd.DataFrame(sum_list)
    # # 根据最高分数排序
    # df = df.sort_values(by=['送礼金额'], ascending=False)
    # df.to_csv('送礼统计.csv')
    return sum_list