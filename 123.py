import  pandas as pd


re = pd.read_csv(r'C:\Users\tuzy\Downloads\5066549353802410_sender.csv', index_col=0)
print(re.head())

print(re.shape)
# 读收礼UID列
pf = re['3'].values
print(pf)

print('-------------------------')

recer_list = list(set(pf[1:]))
# print(len(recer_list))

mp = {}
for uid in recer_list:
    mp[uid] = 0


# 遍历excel每一行
# for i in range(1, re.shape[0]+1):
#    读取每一行数据
    line_data = re.iloc[1184]
    recver_uid = line_data[2]
    print(recver_uid)
    sorce = mp[recver_uid] + int(line_data[7])
    mp[recver_uid] = sorce




    # if i == 2:
    #         break

print('===========================')
print(mp)


