import pandas as pd

FILE_PATH = 'changjing.csv'

df = pd.read_csv(FILE_PATH)
# print(type(df.loc[0]))

se = df.loc[0]
arr = df.to_numpy()

# print(se)

# print(arr)
# print(len(arr))

# print(arr[0])
# print(df.to_numpy())
# print('-------')
# print(df.columns)
# title_arr = arr[0]
# print(type(title_arr))



def findIdxOfKey(key, arrar):
    idx = 0
    for x in arrar:
        if x == key:
            return idx
        idx += 1

indx = findIdxOfKey('送礼UID', se)
print(indx)
