import pandas as pd
import boto3

f = pd.read_excel("/path/to/excel/file/consisting/file/names")


ak = input("please enter s3 Access Key: ")
sk = input("please enter s3 Secret Key: ")
bk = input("Please enter s3 Bucket name: ")
endpoint = input("Please enter s3 Endpoint URL: ")
s3 = boto3.client('s3',endpoint_url=endpoint,aws_access_key_id=ak,aws_secret_access_key=sk)

try:
    for i in range (0,len(f)):
        st = str(f.values[i])
        st = st.replace("']","")
        st = st.replace("['","")
        s3.download_file(bk,st,"/path/to/download/destination/%s" % (st))
except Exception as e:
    print (e)
