import boto3
import pandas as pd
from docpi_app.connection import access_key_id, secret_access_key, region_name
def upload_file_to_s3(file_path, bucket_name, object_name):
    # Create an S3 client 
    # s3 = s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, region_name= region_name)
    s3 = s3 = boto3.client('s3')
    

    # Upload the file to S3
    s3.upload_file(file_path, bucket_name, object_name)
    
def read_csv_from_s3(bucket_name, object_name):
    # Create an S3 client
    # s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, region_name= region_name)
    s3 = boto3.client('s3')


    # Generate a pre-signed URL for the S3 object
    url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_name})

    # Read the CSV file using pandas
    df = pd.read_csv(url)

    return df