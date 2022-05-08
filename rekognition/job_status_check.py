import boto3

region = "us-east-1"
access_key = "AKIAURJP6PMX34NESR5O"
secret_key = "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"
session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)

rekognition = session.client("rekognition")

# Labels Detection #
labelDetectionJobId = '168248d1aa3f5b564dd5d199aa6aba4460be640a8ee9f4b933748c15f06ae790'
print("checking the job status of Job " + labelDetectionJobId)
labelDetectionResults = rekognition.get_label_detection(JobId=labelDetectionJobId)
print("Labels Detection: " + labelDetectionResults['JobStatus'])

# Celebrity Recognition #
celebrityDetectionJobId = 'c63ec673d1a6cfaac1e3ab5ba1aeeb633eb2bc4f3d0dca66a2dde258fe1482c8'
print("checking the job status of Job " + celebrityDetectionJobId)
celebrityDetectionResults = rekognition.get_celebrity_recognition(JobId=celebrityDetectionJobId)
print("Celebrity Recognition: " + celebrityDetectionResults['JobStatus'])

# Face Dectection #
faceDetectionJobId = '32288169fce60bffe99b729189798347b8300470c68e04a01881b323184af2cd'
print("checking the job status of Job " + faceDetectionJobId)
faceDetectionResults = rekognition.get_face_detection(JobId=faceDetectionJobId)
print("Face Dectection: " + faceDetectionResults['JobStatus'])

# Text Dectection #
textDetectionJobId = 'cf51e879433b90b13a2b9de231a9d9e2da30e1fa822c7b767a8ed536ed36a49e'
print("checking the job status of Job " + textDetectionJobId)
textDetectionResults = rekognition.get_text_detection(JobId=textDetectionJobId)
print("Text Dectection: " + textDetectionResults['JobStatus'])

# Person Tracking #
personTrackingJobId = 'f7a2cc06582628a54bdfd0478b1093526c76b251ea4068024378ca0b0b784437'
print("checking the job status of Job " + personTrackingJobId)
personTrackingResults = rekognition.get_person_tracking(JobId=personTrackingJobId)
print("Person Tracking: " + personTrackingResults['JobStatus'])

# Content Moderation #
contentModerationJobId = '4cc64ed51b31700177da1191f9eb2e51db9e25d23cdee206169625925368aa37'
print("checking the job status of Job " + contentModerationJobId)
contentModerationResults = rekognition.get_content_moderation(JobId=contentModerationJobId)
print("Content Moderation: " + contentModerationResults['JobStatus'])