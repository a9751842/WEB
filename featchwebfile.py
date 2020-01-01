import datetime
import urllib.request

class featchwebfile:
    def __init__(self):
        self.file_folder = r'C:\test'
        self.Year = datetime.datetime.now().strftime('%Y')
        self.Month = datetime.datetime.now().strftime('%m')
        self.Day = datetime.datetime.now().strftime('%d')

    def Setup(self):
        self.url  = 'https://www.tpex.org.tw/storage/bond_zone/tradeinfo/cb/'+self.Year+'/'+self.Year+self.Month+'/'+'CBdrs001.'+self.Year+self.Month+self.Day+'-C.xls'
        self.file_name =self.file_folder+'\\'+self.Year+self.Month+self.Day+'.xls'

    def Pull(self):
        urllib.request.urlretrieve(self.url, self.file_name)

if __name__ == '__main__':
    featchwebfile = featchwebfile()
    featchwebfile.Setup()
    featchwebfile.Pull()
