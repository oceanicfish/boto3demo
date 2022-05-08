import boto3
from matplotlib import pyplot as plt
from PIL import Image
import random
import os

filename = "rekognition/images/pl00001.jpg"
img = Image.open(filename)

bucket = "rekognition-resource"
region = "us-east-1"

access_key = ""
secret_key = ""
session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)
s3 = session.client("s3")

with open(filename, "rb") as f:
  s3.put_object(Bucket=bucket, Key=filename, Body=f)

rekognition = session.client("rekognition")

results = rekognition.detect_labels(Image={
  "S3Object": {
    "Bucket": bucket,
    "Name": filename
  }
})

print("Detected labels for " + filename)
print(results)

plt.imshow(img)
plt.show()