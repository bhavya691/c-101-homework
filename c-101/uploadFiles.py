import os
import dropbox
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for fName in files:
                local_path = os.path.join(root, fName)
                relative_path = os.path.relpath(local_path, file_from)
                dbx_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dbx_path, mode=WriteMode('overwrite'))


def main():
    access_token = '2vubDnYO4soAAAAAAAAAAY20eXVPYI9zADoM1p45Nr107Wo5S-PqKH89LyciQons'
    transferData = TransferData(access_token)
    file_from = input('Enter the file name to be uploaded: \t')
    file_to = input('Enter the path to upload: \t')
    transferData.uploadFile(file_from, file_to)
    print('done')


if __name__ == '__main__':
    main()
