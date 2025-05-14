import os, datetime as dt, pytz as tz
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/drive']

# folder = "1kGmciW9RG8USL8sBMpX3glfaHrE_F_Ov" # Main folder for 24-25 images
folder = "1r-Kjq9R0YMJXNLJERSEgAehbDsFYAmBK" # Folder for hood_test
local_folder = "temp_img_cache/"

def get_refreshed_credentials(SCOPES):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    
    elif not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server()

    with open('token.json', 'w') as token_file:
        token_file.write(creds.to_json())
            
    return creds

creds = get_refreshed_credentials(SCOPES)

for ip in sorted(os.listdir(local_folder)):
    full_path = local_folder + ip

    service = build('drive', 'v3', credentials=creds)

    curr_time = dt.datetime.now(tz.timezone("US/Pacific"))

    file_meta = {'name': f"{ip}_{str(curr_time)}.jpg", "parents": [folder]}

    media = MediaFileUpload(full_path)
    file = service.files().create(body=file_meta,
                                        media_body=media,
                                        fields='id').execute()
    
    os.remove(full_path)

print("Upload completed")
