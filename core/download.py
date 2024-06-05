import os
import boto3
from dotenv import load_dotenv
from schemas.voice import Voice

load_dotenv()

def download_wav(voice: Voice):
    try:
        dataset_path = f'dataset/{voice.user_id}.wav'

        bucket = boto3.resource('s3').Bucket(os.getenv('AWS_BUCKET'))
        bucket.download_file(f'user_voice/{voice.wav}.wav', dataset_path)

        return dataset_path

    except Exception as e:
        print(e)
