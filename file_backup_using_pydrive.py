#local csv file to google drive folder using pydrive module
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)
upload_file_list = ['C:/Users/bharg/task_csv.csv']
for upload_file in upload_file_list:
    title=upload_file.split("/")[-1]
    gfile = drive.CreateFile({'parents': [{'id': '1EukowxCuR9pkJkq-Gi8XTQtLoPw6E9aA'}],'title':title})
    # Read file and set it as the content of this instance.
    gfile.SetContentFile(upload_file)
    gfile.Upload() # Upload the file.
    print(title,"uploaded successfully")
