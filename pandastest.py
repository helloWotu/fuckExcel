import pandas as pd

# mydataset = {
#     'sites': ['goole','baidu','wiki'],
#     'numbers': [1, 2, 3]
# }
#
# myvar = pd.DataFrame(mydataset)
#
# print(myvar)

# a = [1, 2, 3]
# myvar = pd.Series(a)
# print(myvar)
#
# print('----')
# print(myvar[2])
# print(type(myvar[1]))
# print(type(2))

# site = {
#     'a', 'ali',
#     'b', 'baidu',
#     'c', 'chifan'
# }

# sites = ['goole','baidu','wiki']

# sites = {
#     1: 'ali',
#     2: 'baidu',
#     3: 'chifan'
# }
# myvar = pd.Series(sites, index= [1, 2, 3])
# print(myvar)


# sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
#
# myvar = pd.Series(sites, index = [1, 3], name="RUNOOB-Series-TEST" )
#
# print(myvar)

#  dataFrame

# 二维数组
# data = [
#     ['gg', 10],
#     ['bb', 12],
#     ['wiki', 18]
# ]
#
# df = pd.DataFrame(data, columns=['name', 'age'])
# print(df)


data = {
    'Site':['Google', 'Runoob', 'Wiki'],
    'Age':[10, 12, 13]
}
df = pd.DataFrame(data, index= ["day1", "day2", "day3"])
print(df)

print('----')
lineData = df.loc['day1']
print(lineData)
print(lineData['Age'])
