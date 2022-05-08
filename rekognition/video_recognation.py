import boto3
from matplotlib import pyplot as plt
from PIL import Image
import random
import os

filename = "video/portugal_vs_spain_2018.mp4"
# img = Image.open(filename)

bucket = "rekognition-resource"
region = "us-east-1"

access_key = ""
secret_key = ""
session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)
s3 = session.client("s3")

rekognition = session.client("rekognition")

responseLableDetection = rekognition.start_label_detection(Video={
  'S3Object': {
    'Bucket': bucket,
    'Name': filename
  }
})
jobIdLableDetection = responseLableDetection['JobId']
print("[" + filename + "] label detection JobId = " + jobIdLableDetection)
print("[DEBUG] response:")
print(responseLableDetection)

responseCelebrityRecognition = rekognition.start_celebrity_recognition(Video={
  'S3Object': {
    'Bucket': bucket,
    'Name': filename
  }
})
jobIdCelebrityRecognition = responseCelebrityRecognition['JobId']
print("[" + filename + "] celebrity detection JobId = " + jobIdCelebrityRecognition)

responseFaceDetection = rekognition.start_face_detection(Video={
  'S3Object': {
    'Bucket': bucket,
    'Name': filename
  }
})
jobIdFaceDetection = responseFaceDetection['JobId']
print("[" + filename + "] face detection JobId = " + jobIdFaceDetection)

# responseTextDetection = rekognition.start_text_detection(Video={
#   'S3Object': {
#     'Bucket': bucket,
#     'Name': filename
#   }
# })
# jobIdTextDetection = responseTextDetection['JobId']
# print("[" + filename + "] text detection JobId = " + jobIdTextDetection)

# responsePersonTracking = rekognition.start_person_tracking(Video={
#   'S3Object': {
#     'Bucket': bucket,
#     'Name': filename
#   }
# })
# jobIdPersonTracking = responsePersonTracking['JobId']
# print("[" + filename + "] person tracking JobId = " + jobIdPersonTracking)

# responseContentModeration = rekognition.start_content_moderation(Video={
#   'S3Object': {
#     'Bucket': bucket,
#     'Name': filename
#   }
# })
# jobIdContentModeration = responseContentModeration['JobId']
# print("[" + filename + "] content moderation JobId = " + jobIdContentModeration)

# NEED SEGMENT TYPES
# response = rekognition.start_segment_detection(Video={
#   'S3Object': {
#     'Bucket': bucket,
#     'Name': filename
#   }
# })
# jobId = response['JobId']
# print("[" + filename + "] segment detection JobId = " + jobId)

# results = rekognition.get_celebrity_recognition(JobId=jobId)
# print(results)
