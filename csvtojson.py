import json
import pandas as pd

dir_paths = r'C:\Users\tuzy\Documents\WeChat Files\tzyyyzyyq\FileStorage\File\2022-04\新建文件夹\新建文件夹\充值TOP10送谁最多？\有问题的\\'
file_name = r'gift_history_20220429130433'
mp = {}

def csvTojsonDic():
    file_path = dir_paths + file_name + '.csv'
    df = pd.read_csv(file_path)
    json_path = dir_paths + file_name + '.json'
    df.to_json(json_path, orient='records', force_ascii=False)

    with open(json_path, 'r', encoding='utf-8') as f:
        dictJson = json.loads(f.read())
        return dictJson


    # f = open(filePath, "r", encoding='utf-8')  #
    # ls = []
    # for line in f:
    #     line = line.replace("\n", "")
    #     ls.append(line.split(","))
    #
    # f.close()
    # for i in range(1, len(ls)):
    #     ls[i] = dict(zip(ls[0], ls[i]))
    # json_string = json.dumps(ls[1:], sort_keys=True, indent=4, ensure_ascii=False)
    # dictJson = json.loads(json_string)
    # # print(len(dictJson))
    # return dictJson
    # print(len(json_string))

def findHighterSocre(dicts):
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


def findNeedInfos(dicts):
    for dic in dicts:
        if dic['3'] == mp[0][0]:
            rever_uid = dic['3']
            rever_name = dic['4']
            rever_sore = mp[0][1]
            sender_uid = dic['1']
            sender_name = dic['2']
            print(
                f'找到最高充值的了！\n 送礼人uid：{sender_uid} ,送礼人name is：{sender_name},\n 收礼人uid is:{rever_uid}, name is :{rever_name},\n 累计送出金额是：{rever_sore}')
            break


jsonDict = csvTojsonDic()
findHighterSocre(jsonDict)
mp = sorted(mp.items(), key=lambda x: x[1], reverse=True)
findNeedInfos(jsonDict)




