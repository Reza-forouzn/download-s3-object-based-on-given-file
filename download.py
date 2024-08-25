import pandas as pd
import boto3

f = pd.read_excel("/mnt/data/Work/Kian/kyc/test.xlsx")

# ak = "U58MA5TFBMEWQ8MW3IJI"
# sk = "1ozVl4yTtTBgmm7xtD8wiZUWRwGcsQROYdg7NRFv"
# bk = "kyc-image-external"
# endpoint = "https://s3.kiandigital.com"
ak = input("please enter s3 Access Key: ")
sk = input("please enter s3 Secret Key: ")
bk = input("Please enter s3 Bucket name: ")
endpoint = input("Please enter s3 Endpoint url: ")
s3 = boto3.client('s3',endpoint_url=endpoint,aws_access_key_id=ak,aws_secret_access_key=sk)

try:
    for i in range (0,len(f)):
        st = str(f.values[i])
        st = st.replace("']","")
        st = st.replace("['","")
        s3.download_file(bk,st,"/mnt/data/Work/Kian/kyc/images/%s" % (st))
except Exception as e:
    print (e)
