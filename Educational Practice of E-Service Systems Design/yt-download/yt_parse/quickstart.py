import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from yt_parse.worker import *

import shutil

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]


def main(link):
  shutil.rmtree("downloads")

  # google code after
  creds = None

  if os.path.exists("yt_parse/token.json"):
    creds = Credentials.from_authorized_user_file("yt_parse/token.json", SCOPES)

  if not creds or not creds.valid:

    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "yt_parse/credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)

    with open("yt_parse/token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("drive", "v3", credentials=creds)
    #google code before

    audio_f_path = download(link) #function download from worker.py

    file_metadata = {
      'name': os.path.basename(audio_f_path),#filename on drive
      'parents': ["1UU5D8xxXTr-ADMr6MxsW7SxnsRgXoRgJ"], #the folder test 1234 id
    }

    media = MediaFileUpload(audio_f_path, mimetype='audio/mpeg')

    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

  except HttpError as error:
    return

