
import os
import pandas as pd
import time

# Folder_Path = os.getcwd()
Folder_Path = r'/Users/tuzhaoyang/Desktop/新建文件夹/'
SaveFile_Name = r'all.csv'              #合并后要保存的文件名

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
            if 'all' in csv_file:
                os.remove(csv_file)
            else:
                list_csv.append(csv_file)

        if os.path.isdir(path):
            # print("{0} : is dir".format(cur_file))
            # print(os.path.join(file_dir, cur_file))
            list_dir(path)
    return list_csv


def readExcelData(filepath):
   df = pd.read_csv(filepath)


if __name__ == '__main__':
    file_list = list_dir(Folder_Path)
    # 读取第一个CSV文件并包含表头
    df = pd.read_csv(file_list[0])  # 编码默认UTF-8，若乱码自行更改

    save_path = Folder_Path  + SaveFile_Name
    # 将读取的第一个CSV文件写入合并后的文件保存
    df.to_csv(save_path, encoding="utf_8_sig", index=False, header=True)

    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
    for i in range(1, len(file_list)):
        df = pd.read_csv(file_list[i])
        df.to_csv(save_path, encoding="utf_8_sig", index=False, header=False, mode='a+')
    print('文件写入完毕，开始计算平均值------')

    all_df = pd.read_csv(save_path)
    print(all_df)
    print('-------')

    print(all_df.shape[0])
    print(all_df.shape[1])

    all_df.loc['row_sum'] = all_df.apply(lambda x: x.sum())
    all_df.loc['avg'] = all_df.mean()
    print(all_df)
    all_df.to_csv(save_path, encoding="utf_8_sig")

