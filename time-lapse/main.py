from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'
print(SCOPES)

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    SCOPES = 'https://www.googleapis.com/auth/drive'
    credentials = 'credentials1.json'
    store = file.Storage(credentials)
    try:
        creds = store.get()
    except Exception:
        creds = None
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(credentials, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))
    return service

def upload(filename, new_name, drive_service):
    file_metadata = {'name': new_name}
    media = MediaFileUpload(filename)#,
                            # mimetype='image/jpeg')
    file = drive_service.files()        .create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file.get('id'))

#service = main()
#upload(service)