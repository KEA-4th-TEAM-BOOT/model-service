import os
import glob
import boto3
from dotenv import load_dotenv

load_dotenv()

def path_finder(path):
    return glob.glob(path)

def s3_connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3"
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3

def upload_model(user_id: int, model_path: str, index_file: str):
    index = path_finder(index_file)
    model_link = f'model/{user_id}/{user_id}.pth'
    index_link = f'model/{user_id}/{os.path.basename(index[0])}'

    s3 = s3_connection()
    try:
        s3.upload_file(model_path, os.getenv('AWS_BUCKET'), model_link)
        s3.upload_file(index[0], os.getenv('AWS_BUCKET'), index_link)
        return model_link, index_link
    except Exception as e:
        print(e)
