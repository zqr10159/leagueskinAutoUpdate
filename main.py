import os
import zipfile
import subprocess
import requests
import re
import wget

url = 'http://leagueskin.net/p/download-mod-skin-2020-chn'
f = requests.get(url)
fuck = f.text
# print(fuck)
# regix = r'http://dl\d.modskinpro\.com/.*\d'
regix = r'http://\w+\.modskinlolvn\.com/MODSKIN_\d+.\d+.zip'

urlt = re.findall(regix, fuck)[0]
for x in range(len(urlt)):
    if urlt[x] == '_':
        version = urlt[x+1:-4]

# print(version)
# print(urlt)
o = 'fuck.zip'
old = os.path.exists(r'C:\Fraps\LOLPRO %s.exe' %version)
# print(old)
if not old:
    wget.download(urlt, out = o)
    with zipfile.ZipFile(o, "r") as zFile:
        for fileM in zFile.namelist():
            zFile.extract(fileM)
    os.remove(o)
    print('检测到新版本，已为您下载最新版本%s！正在为您打开league skin' % version)
    subprocess.Popen(r'C:\Fraps\LOLPRO %s.exe' %version)
else:
    print('您目前已经是最新版本%s了！无需更新！正在为您打开league skin'% version)
    subprocess.Popen(r'C:\Fraps\LOLPRO %s.exe' %version)
