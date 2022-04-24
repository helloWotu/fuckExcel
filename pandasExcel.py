
import pandas as pd
dirpath = r'/Users/tuzhaoyang/Desktop/日志下载/'

# nba_path = dirpath + 'nba.csv'
# df = pd.read_csv(nba_path)
# # print(df.to_string())
# print(df)


# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]

# 字典
dict = {'name': nme, 'site': st, 'age': ag}

df = pd.DataFrame(dict)
site_path = dirpath + 'site.csv'
df.to_csv(site_path)

