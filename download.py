import pandas as pd
# import boto
# import boto.s3.connection
import boto3

f = pd.read_excel("/mnt/data/Work/Kian/kyc/test.xlsx")

ak = "U58MA5TFBMEWQ8MW3IJI"
sk = "1ozVl4yTtTBgmm7xtD8wiZUWRwGcsQROYdg7NRFv"
bk = "kyc-image-external"
endpoint = "https://s3.kiandigital.com"
# stt = "e139e62b-795c-4299-80b4-9ebe1ed8c6b4"

s3 = boto3.client('s3',endpoint_url=endpoint,aws_access_key_id=ak,aws_secret_access_key=sk)
# s3.download_file(bk,stt,"/mnt/data/Work/Kian/kyc/images/%s" % (stt))

# e139e62b-795c-4299-80b4-9ebe1ed8c6b4
# obr = s3.list_objects_v2(Bucket=bk)
# print (obr)
# response = s3.list_buckets()
# for bucket in response['Buckets']:
#     print("{name}\t{created}".format(
#                 name = bucket['Name'],
#                 created = bucket['CreationDate']
# ))
# conn = boto.connect_s3(
#         aws_access_key_id = ak,
#         aws_secret_access_key = sk,
#         host = 's3-hwuatk8s.kian.digital',
#         #is_secure=False,               # uncomment if you are not using ssl
#         calling_format = boto.s3.connection.OrdinaryCallingFormat(),)

for i in range (0,len(f)):
    st = str(f.values[i])
    st = st.replace("']","")
    st = st.replace("['","")
    s3.download_file(bk,st,"/mnt/data/Work/Kian/kyc/images/%s" % (st))

