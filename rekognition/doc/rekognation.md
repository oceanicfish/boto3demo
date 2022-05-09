1. download a video (you can download any video from youtube via savefrom.net)
2. upload the video to your S3 bucket
3. create a IAM User and give the following permissions to him
 - AmazonSQSFullAccess
 - AmazonRekognitionFullAccess
 - AmazonS3FullAccess
 - AmazonSNSFullAccess
4. use the AccessKey and SecuredKey of the new user which created above (hard code it directly in the python code)
4. install Python 3.7 and Boto3 SDK by PIP