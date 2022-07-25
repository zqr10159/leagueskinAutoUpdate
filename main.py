import os
import zipfile
import subprocess
import requests
import re
import wget


class leagueskinAutoUpdate():
    def __init__(self):
        self.downloadFile = 'leagueskin.zip'
        self.downloadFolder = 'C:\leagueskin\\'

    def getVersion(self):
        url = 'http://leagueskin.net/p/download-mod-skin-2020-chn'
        f = requests.get(url)
        req = f.text

        url = r'http://\w+\.modskinlolvn\.com/MODSKIN_\d+.\d+.zip'

        urlt = re.findall(url, req)[0]
        for x in range(len(urlt)):
            if urlt[x] == '_':
                version = urlt[x + 1:-4]
        list = [version,urlt]
        return list

    def execute(self):
        version = self.getVersion()[0]
        urlt = self.getVersion()[1]
        # print(self.rootFolder+self.downloadFile)
        if self.checkVersion(version):
            print('检测到新版本，正在为您下载最新版本%s！下载完成后自动为您打开league skin' % version)
            self.download(urlt)
            with zipfile.ZipFile(self.downloadFolder+self.downloadFile, "r") as zFile:
                for fileM in zFile.namelist():
                    zFile.extract(fileM,self.downloadFolder)
            os.remove(self.downloadFolder+self.downloadFile)
            # print(r'C:\Fraps\LOLPRO %s.exe' % version)
            subprocess.Popen(self.downloadFolder+'LOLPRO %s.exe' % version)
        else:
            print('您目前已经是最新版本%s了！无需更新！正在为您打开league skin' % version)
            subprocess.Popen(self.downloadFolder+'LOLPRO %s.exe' % version)

    def download(self, urlt):
        if os.path.exists(self.downloadFolder):
            wget.download(urlt, out=self.downloadFolder+self.downloadFile)
        else:
            os.mkdir(self.downloadFolder)
            wget.download(urlt, out=self.downloadFolder + self.downloadFile)

    def checkVersion(self, version):
        old = os.path.exists(self.downloadFolder+'LOLPRO %s.exe' % version)
        if not old:
            return True
        else:
            return False

if __name__ == '__main__':
    leagueskinAutoUpdate().execute()