from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '18NWe4Eu5JZ15LARWjrJintc7w30zGIIXfgJEFMSN-b8'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet5!A1:B5").execute()
values = result.get('values', [])

local_csv=pd.read_csv("C:\\Users\\Samsung\\OneDrive\\Desktop\\task_csv.csv")
csv_drive=[local_csv.columns.values.tolist()] + local_csv.values.tolist()

if bool(values==csv_drive):
    print('No Changes')
else:
    clear = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                    range="Sheet5").execute()
    update = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet5!A1",valueInputOption="USER_ENTERED",body={"values":csv_drive}).execute()
    result1 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet5!A1").execute()
    values1 = result1.get('values', [])
    print('Updated Successfully')
