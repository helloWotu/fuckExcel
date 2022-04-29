# 递归获取.csv文件存入到list1
import os
import json
import pandas as pd

paths = os.getcwd()
# paths = r'C:\Users\tuzy\Documents\WeChat Files\tzyyyzyyq\FileStorage\File\2022-04'
# paths = r'C:\Users\tuzy\Documents\WeChat Files\tzyyyzyyq\FileStorage\File\2022-04\新建文件夹\新建文件夹\充值TOP10送谁最多？'
# paths = r'C:\Users\tuzy\Documents\WeChat Files\tzyyyzyyq\FileStorage\File\2022-04\新建文件夹\新建文件夹\充值TOP10送谁最多？\有问题的'

# 将所有文件的路径放入到listcsv列表中
def list_dir(file_dir):
    # list_csv = []
    dir_list = os.listdir(file_dir)
    for cur_file in dir_list:
        path = os.path.join(file_dir, cur_file)
        # 判断是文件夹还是文件
        if os.path.isfile(path):
            # print("{0} : is file!".format(cur_file))
            dir_files = os.path.join(file_dir, cur_file)
        # 判断是否存在.csv文件，如果存在则获取路径信息写入到list_csv列表中
        if os.path.splitext(path)[1] == '.csv':
            csv_file = os.path.join(file_dir, cur_file)
            # print(os.path.join(file_dir, cur_file))
            # print(csv_file)
            list_csv.append(csv_file)

        if os.path.splitext(path)[1] == '.json':
            json_file = os.path.join(file_dir, cur_file)
            os.remove(json_file)

        if os.path.isdir(path):
            # print("{0} : is dir".format(cur_file))
            # print(os.path.join(file_dir, cur_file))
            list_dir(path)
    return list_csv

def findSenderOrRever(jsonDic):
    if len(jsonDic) < 3:
        return
    firstItem = dict(jsonDic[0])
    if '1' not in firstItem.keys():
        return

    isSender = True
    sender_uid = jsonDic[3]['1']
    for dic in jsonDic:
        if dic['1'] == '送礼UID':
            continue
        if sender_uid != dic['1']:
            isSender = False
            break
    if isSender == True:
        return 'isSender'

    isRecver = True
    recver_uid = jsonDic[3]['3']
    for dic in jsonDic:
        if dic['1'] == '送礼UID':
            continue
        if recver_uid != dic['3']:
            isRecver = False
            break

    if isRecver == True:
        return 'isRecver'


def csvTojsonDic(filePath):

    df = pd.read_csv(filePath)
    json_path = paths + '\\temp.json'
    df.to_json(json_path, orient='records', force_ascii=False)

    with open(json_path, 'r', encoding='utf-8') as f:
        dictJson = json.loads(f.read())
        return dictJson


def findHighterSocre(dicts, mp, issender):
    if issender == 'isSender':
        # 送礼人的逻辑
        for dic in dicts:
            if dic['1'] == '送礼UID':
                continue
            mp[dic['3']] = 0

        for dic in dicts:
            if dic['1'] == '送礼UID':
                continue
            rever_uid = dic['3']
            sore = int(dic['8'])
            last_sore = mp[rever_uid]
            mp[rever_uid] = sore + last_sore

    if issender == 'isRecver':
        # 收礼人的逻辑
        for dic in dicts:
            if dic['1'] == '送礼UID':
                continue
            mp[dic['1']] = 0

        for dic in dicts:
            if dic['1'] == '送礼UID':
                continue
            sender_uid = dic['1']
            sore = int(dic['8'])
            last_sore = mp[sender_uid]
            mp[sender_uid] = sore + last_sore



sender_list = []
recver_list = []


def findNeedInfos(dicts, mp, issender):
    if issender == 'isSender':
        # 送礼人的逻辑
        for dic in dicts:
            if dic['3'] == mp[0][0]:
                rever_uid = dic['3']
                rever_name = dic['4']
                rever_sore = mp[0][1]
                sender_uid = dic['1']
                sender_name = dic['2']
                sender_list.append([rever_uid, rever_name, rever_sore, sender_uid, sender_name])
                print(
                    f'送礼人>>>>>>>>找到最高充值的了！\n 送礼人uid：{sender_uid} ,送礼人name is：{sender_name},\n 收礼人uid is:{rever_uid}, name is :{rever_name},\n 累计送出金额是：{rever_sore}')
                print('----------------------------------------------------------------------------')
                print()
                print()
                break

    if issender == 'isRecver':
        # 收礼人的逻辑
        for dic in dicts:
            if dic['1'] == mp[0][0]:
                rever_uid = dic['3']
                rever_name = dic['4']
                sender_uid = dic['1']
                sender_name = dic['2']
                rever_sore = mp[0][1]
                recver_list.append([rever_uid, rever_name, rever_sore, sender_uid, sender_name])

                print(
                    f'收礼人<<<<<<<<<<找到最高充值的了！\n 送礼人uid：{sender_uid} ,送礼人name is：{sender_name},\n 收礼人uid is:{rever_uid}, name is :{rever_name},\n 累计送出金额是：{rever_sore}')
                print('----------------------------------------------------------------------------')
                print()
                print()
                break

# 解决科学计数造成的uid丢真问题
def long_num_str(data):
    data = str(data)+'\t'
    return data

if __name__ == '__main__':
    list_csv = []
    list_dir(file_dir=paths)

    for filePath in list_csv:
        mp = {}
        jsonDict = csvTojsonDic(filePath)
        issender = findSenderOrRever(jsonDict)
        # print(rest)
        findHighterSocre(jsonDict, mp, issender)
        mp = sorted(mp.items(), key=lambda x: x[1], reverse=True)
        findNeedInfos(jsonDict, mp, issender)

        columns = ['收礼人uid', '收礼人名字', '收礼总金额', '送礼人uid', '送礼人名字']
        df = pd.DataFrame(sender_list, columns=columns)
        df['收礼人uid'] = df['收礼人uid'].map(long_num_str)
        df['送礼人uid'] = df['送礼人uid'].map(long_num_str)
        sender_path = paths + '/送礼人（土豪送给谁最多）.csv'
        df.to_csv(sender_path)

        df_rec = pd.DataFrame(recver_list, columns=columns)
        df_rec['收礼人uid'] = df['收礼人uid'].map(long_num_str)
        df_rec['送礼人uid'] = df['送礼人uid'].map(long_num_str)
        recver_path = paths + '/收礼人（谁送给土豪最多）.csv'
        df.to_csv(recver_path)

        # print(df)

    # print(list_csv)