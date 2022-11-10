from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_apis import create_service
from google.oauth2 import service_account

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME='drive'
API_VERSION='v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = create_service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
folder_id='1EukowxCuR9pkJkq-Gi8XTQtLoPw6E9aA'
upload_file_list = ['task_csv.csv','Google_Drive_logo.png']
upload_file_type= ['text/csv','image/png']
for upload_file,upload_type in zip(upload_file_list,upload_file_type):
    file_metadata={
                  'name':upload_file,
                  'parents': [folder_id]
                  }
    media = MediaFileUpload('C:/Users/Samsung/OneDrive/Desktop/{0}'.format(upload_file),mimetype=upload_type)
    service.files().create(
                            body=file_metadata,
                            media_body=media,
                            fields='id'
                          ).execute()
    print(file_metadata['name'],"uploaded successfully")
