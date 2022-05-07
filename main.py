# 递归获取.csv文件存入到list1
import os
import pandas as pd
import recverPase
import senderPase

paths = os.getcwd()
columns = ['送礼人ID', '送礼人名字', '收礼人ID', '收礼人名字', '送礼总金额']

# 将所有文件的路径放入到listcsv列表中
def list_dir(file_dir):
    list_csv = []
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

# 解决科学计数造成的uid丢真问题
def long_num_str(data):
    data = str(data)+'\t'
    return data


def save_to_csv(df,path):
    for column in columns:
        df[column] = df[column].map(long_num_str)
    df.to_csv(path, encoding='utf_8_sig')

if __name__ == '__main__':

    # ret = recverPase.getFirstSored('gift_history_20220424024233.csv')
    # print(ret)

    list_csv = list_dir(file_dir=paths)
    sender_list = []
    recver_list = []
    for filePath in list_csv:
        # 土豪送给谁最多
        ret_recver = recverPase.getFirstSored(filePath)

        # 谁送给土豪最多
        ret_sender = senderPase.getFirstSored(filePath)
        if len(ret_sender) > 0:
            sender_list.append(ret_sender[0])

        if len(ret_recver) > 0:
            recver_list.append(ret_recver[0])

    if len(sender_list) > 0:
        # 存谁送给土豪最多的表
        df_send = pd.DataFrame(sender_list)
        sender_path = paths + '/收礼人（谁送给土豪最多）.csv'
        save_to_csv(df=df_send, path=sender_path)

    if len(recver_list) > 0:
        # 存土豪送给谁最多的表
        recver_path = paths + '/送礼人（土豪送给谁最多）.csv'
        df_rec = pd.DataFrame(recver_list)
        save_to_csv(df=df_rec, path=recver_path)
