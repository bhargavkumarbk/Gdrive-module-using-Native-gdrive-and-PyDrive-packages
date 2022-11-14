from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_apis import create_service
from google.oauth2 import service_account

CLIENT_SECRET_FILE ='credentials.json'
CLIENT_SECRET_FILE = ['credentials.json','credentials1.json','credentials2.json','credentials3.json']

API_NAME='drive'
API_VERSION='v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
folder_id=['1EukowxCuR9pkJkq-Gi8XTQtLoPw6E9aA','1CUUKrRwDVW5vJLRuwIeH2qmd1ulCmb7n','1XFRW_H_qM27vPjiNp5gIJuS5pAk75nOe','19ZkfPesx_w1OvFwYRtmzdPHY1whEId32']
for CSF,FID in zip(CLIENT_SECRET_FILE,folder_id):
        
    service = create_service(CSF,API_NAME,API_VERSION,SCOPES)
    folder_id=FID
    upload_file_list = ['task_csv.csv','Google_Drive_logo.png']
    upload_file_type= ['text/csv','image/png']
    for upload_file,upload_type in zip(upload_file_list,upload_file_type):
        file_metadata={
                      'name':upload_file,
                      'parents': [folder_id]
                      }
        media = MediaFileUpload('C:/Users/bharg/{0}'.format(upload_file),mimetype=upload_type)
        service.files().create(
                                body=file_metadata,
                                media_body=media,
                                fields='id'
                              ).execute()
        print(file_metadata['name'],"uploaded successfully")
