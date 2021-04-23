import dropbox
import os
from dropbox.files import WriteMode
class transferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def UploadFile(self,Filefrom,FileTo):
        Item1=dropbox.Dropbox(self.accessToken)
        for root,dirs,files in os.walk(Filefrom):
            for fileName in files:
                localPath=os.path.join(root,fileName)
                relatedPath=os.path.relpath(localPath,Filefrom)
                dropboxpath=os.path.join(FileTo,relatedPath)
                with open(localPath,'rb') as F:
                    Item1.files_upload(F.read(),dropboxpath,mode=WriteMode('overwrite'))
def main():
    accessToken='sl.AvfJTf-98RN3ejNm03DneYsfo44uxTdx6oKmr9OaWBQNfdnf2i64zkwtM86ghYIsFqMzDMFq20zcc3nrsLOSTGkSrgObmE2y0WLEcpHAxVVVG0l2RljSOxCo_Cg13f7wRGZpM_0'
    TD=transferData(accessToken)
    Filefrom=input("Enter the Name of Transfer File")
    FileTo=input("Destination Location")
    TD.UploadFile(Filefrom,FileTo)
    print('file has been moved')
main()
     