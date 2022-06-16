import pandas as pd
import numpy as np

'''
作为送礼人分析收礼人分析，   土豪送给谁最多
'''
file_idx = 0

def getFirstSored(file_path):


    print('file_path:%s index:%d\n' % (file_path, file_idx))
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
        rec_id = df.loc[row_i][4]
        rec_name = df.loc[row_i][5]
        rec_core = df.loc[row_i][10]
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


    # df = pd.DataFrame(sum_list)
    # # 根据最高分数排序
    # df = df.sort_values(by=['送礼金额'], ascending=False)
    # df.to_csv('送礼统计.csv')
    return sum_list


'''
作为送礼人分析收礼人情况，   土豪送给哪个场景 最多，各个场景的具体情况
'''

def getTuHaoSendScene(file_path):
    global file_idx
    file_idx += 1
    print('file_path:%s index:%d\n' % (file_path, file_idx))

    df = pd.read_csv(file_path)

    first_title = df.loc[0][0]
    if first_title != 'ID':
        return

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
    title_se = df.loc[0]
    for row_i in range(1, df.shape[0]):
        # 送礼人id
        send_id = findValus(df, row_i, "送礼UID", title_se)

        # 送礼人name
        send_name = findValus(df, row_i, "送礼人", title_se)

        # 送礼场景id
        # rec_sence_id = findValus(df, row_i, "对应ID", title_se)

        # 送礼场景name
        rec_sence_name = findValus(df, row_i, "场景", title_se)

        # 送礼场景金币
        rec_core = findValus(df, row_i, "金币", title_se)
        recver = {
            'send_id': send_id,
            'send_name': send_name,
            'rec_sence_name': rec_sence_name,
            'rec_core': rec_core
        }
        all_recver.append(recver)
        rec_id_set.add(rec_sence_name)

    # 计算总金币
    sum_list = []
    for this_rec_name in rec_id_set:
        rec_core = 0
        rec_sence_name = ''
        send_id = ''
        send_name = ''
        # 遍历算出当前rec_id 所有的总金币
        for one_recv in all_recver:
            if one_recv['rec_sence_name'] == this_rec_name:
                rec_core += int(one_recv['rec_core'])
                rec_sence_name = one_recv['rec_sence_name']
                send_name = one_recv['send_name']
                send_id = one_recv['send_id']

        sum_rec = {
            '送礼人ID': send_id,
            '送礼人名字': send_name,
            '场景名字': rec_sence_name,
            '送礼总金额': rec_core
        }
        sum_list.append(sum_rec)

    # print(sum_list)

    # df = pd.DataFrame(sum_list)
    # # 根据最高分数排序
    # df = df.sort_values(by=['送礼金额'], ascending=False)
    # df.to_csv('送礼统计.csv')
    sum_list = sorted(sum_list, key=lambda x: x['送礼总金额'], reverse=True)

    first_item = sum_list[0]
    tuhao_uid = first_item['送礼人ID']
    tuhao_name = first_item['送礼人名字']
    most_sence_name = first_item['场景名字']
    sence_ktv_core = 0
    sence_zhibo_core = 0
    sence_zuoping_core = 0
    sence_sixing_core = 0
    sence_qinmi_core = 0
    sence_other_core = 0
    sence_other_name = ''

    for dic_item in sum_list:
        if dic_item['场景名字'] == 'KTV':
            sence_ktv_core = dic_item['送礼总金额']
        elif dic_item['场景名字'] == '直播':
            sence_zhibo_core = dic_item['送礼总金额']
        elif dic_item['场景名字'] == '作品':
            sence_zuoping_core = dic_item['送礼总金额']
        elif dic_item['场景名字'] == '私信':
            sence_sixing_core = dic_item['送礼总金额']
        elif dic_item['场景名字'] == '亲密关系':
            sence_qinmi_core = dic_item['送礼总金额']
        else:
            sence_other_name = dic_item['场景名字']
            sence_other_core = dic_item['送礼总金额']

    column_names = ['土豪uid', '土豪送礼最多的场景', '场景A（KTV）', '场景B（直播）', '场景C（作品）', '场景D（私信）', '场景E（亲密关系）', '其他场景']
    column_data = {
        column_names[0]: tuhao_uid,
        column_names[1]: most_sence_name,
        column_names[2]: sence_ktv_core,
        column_names[3]: sence_zhibo_core,
        column_names[4]: sence_zuoping_core,
        column_names[5]: sence_sixing_core,
        column_names[6]: sence_qinmi_core,
        column_names[7]: sence_other_core
    }

    return column_data


def findIdxOfKey(key, arrar):
    idx = 0
    for x in arrar:
        if x == key:
            return idx
        idx += 1

def findValus(df, row_i, key, arrar):
    find_idx = findIdxOfKey(key, arrar)
    value = df.loc[row_i][find_idx]
    return value


# file_path = '/Users/tuzhaoyang/Desktop/blecrash/充值TOP100用户/gift_history_20220616031730.csv'
# column_data = getTuHaoSendScene(file_path)
# print(column_data)
#
# data_list = [column_data,column_data]
#
# df_save = pd.DataFrame(data_list)
# save_path = '/Users/tuzhaoyang/Desktop/blecrash' + '/export.csv'
# df_save.to_csv(save_path, encoding='utf_8_sig')
