import boto3
import json

s3 = boto3.resource('s3')


def lambda_handler(event, context):
   
   bucket = event['Records'][0]['s3']['bucket']['name']
   key = event['Records'][0]['s3']['object']['key']

   source_object = {'Bucket':bucket , 'Key': key}

   object_acl = s3.Object(bucket_name='bucket-name', key=key)

   response = object_acl.Acl().put(ACL='public-read')

   return {
       'statusCode': 200,
       'body': json.dumps('Hello from S3 events Lambda!')
   }
