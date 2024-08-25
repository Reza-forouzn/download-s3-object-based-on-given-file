# import xlrd
import pandas as pd
import boto3
# f = xlrd.open_workbook("/mnt/data/Work/Kian/kyc/dataset2-image-id.xlsx")
# f = pd.ExcelFile("/mnt/data/Work/Kian/kyc/dataset2-image-id.xlsx")
# print (type(f))
# fline = f.readlines()
# for line in fline:
#     print (line)

# dfs = pd.read_excel(file_name, sheet_name=None)

f = pd.read_excel("/mnt/data/Work/Kian/kyc/test.xlsx")
# print (f)
# print (type(f))
# print (f.iloc[0])
# print (f.iat[0,0])
# print (f.iat[1,0])

# for i in range (0,len(f)):
#     print (f.iat[i,0])

# c = 0
# for rows in f:
#     print (f.values)
#     c += 1
# print (c)

for i in range (0,len(f)):
    # print (f.values[i])
    # print (type(f.values[i]))
    # print (str(f.values[i]))
    # print (type(str(f.values[i])))
    # c += 1
    st = str(f.values[i])
    st = st.replace("']","")
    st = st.replace("['","")

    # print (st)
# print (c)
