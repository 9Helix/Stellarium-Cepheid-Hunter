import os
import pyautogui as pag
import time
from PIL import ImageGrab as scr
from datetime import datetime
from datetime import date
import subprocess
import logging
import keyboard
from jdcal import *

logging.basicConfig(filename='example.log', level=logging.DEBUG)

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

if keyboard.is_pressed('q'):
    pag.press('ctrl','c')

file_cep=input('Delta Cep file: ')
file_pol=input('Polaris file: ')
file_x=input('X Cyg file: ')
file_su=input('SU Cyg file: ')

up_cep=0.221131
up_pol=0.136034
up_x=0.097010
up_su=0.270130

pad_cep=0.663394
pad_pol=0.136034
pad_x=0.194021
pad_su=0.810390

min_cep=3.48
min_pol=1.86
min_x=5.85
min_su=6.44

per_cep=5.36634
per_pol=3.9696
per_x=16.39
per_su=3.85

#os.startfile('C:\Program Files\Stellarium\stellarium.exe')

time.sleep(4)
pag.hotkey('k')
stel_vrijeme=datetime.now().strftime('%Y-%m-%d %H-%M-%S')
ctime1=os.path.getmtime('D:\Dokumenti\ASTRONOMIJA\Cefeide\CEFEIDE\Delta Cep\Delta Cep {}.jpg'.format(file_cep))
ctime1=datetime.utcfromtimestamp(ctime1).strftime('%Y-%m-%d %H:%M:%S')
corr=int(ctime1[ctime1.find(' '):ctime1.find(' ')+3])+2
corr=' '+str(corr)
ctime1=ctime1.replace(ctime1[ctime1.find(' '):ctime1.find(' ')+3],str(corr))
ctime1_yr=ctime1[:4]
ctime1_mo=ctime1[5:7]
ctime1_da=ctime1[8:10]
ctime1_hr=ctime1[11:13]
ctime1_mi=ctime1[14:16]
ctime1_se=ctime1[17:19]
if ctime1_mo[0]=='0':
   ctime1_mo=ctime1_mo.replace('0','')
god_sad=stel_vrijeme[:4]
if god_sad[0]=='0':
   god_sad=god_sad.replace('0','')
mj_sad=stel_vrijeme[5:7]
if mj_sad[0]=='0':
   mj_sad=mj_sad.replace('0','')
dan_sad=stel_vrijeme[8:10]
if dan_sad[0]=='0':
   dan_sad=dan_sad.replace('0','')
jd_prošlost=int(gcal2jd(ctime1_yr,ctime1_mo,ctime1_da)[1])
print(jd_prošlost)

pag.press('f5')
pag.click(x=709,y=565)
pag.click(x=715,y=618)
pag.moveTo(715,618)
pag.dragTo(855,618,2,button='left')
pag.write(str(jd_prošlost),interval=1.00)
pag.moveTo(784,617)
pag.dragTo(855,618,0.50,button='left')
pag.write(str(7),interval=0.50)
pag.press('f5')

    
"""
pag.hotkey('f3')
pag.typewrite('Delta Cep')
pag.hotkey('enter')
time.sleep(1)
now_cep=datetime.now()
vrijeme_cep=now_cep.strftime('%m-%d-%Y %H-%M-%S')
folder='images/'
filename=' Delta Cep.png'
output_cep=folder+vrijeme_cep+filename
im=scr.grab(bbox=(7,305,329,320))
im.save(output_cep)

pag.hotkey('f3')
pag.typewrite('Polaris')
pag.hotkey('enter')
time.sleep(1)
now_pol=datetime.now()
vrijeme_pol=now_pol.strftime('%m-%d-%Y %H-%M-%S')
folder='images/'
filename=' Polaris.png'
output_pol=folder+vrijeme_pol+filename
im1=scr.grab(bbox=(8,331,328,344))
im1.save(output_pol)

pag.hotkey('f3')
pag.typewrite('X Cyg')
pag.hotkey('enter')
time.sleep(1)
now_x=datetime.now()
vrijeme_x=now_x.strftime('%m-%d-%Y %H-%M-%S')
folder='images/'
filename=' X Cyg.png'
output_x=folder+vrijeme_x+filename
im2=scr.grab(bbox=(7,322,328,336))
im2.save(output_x)

pag.hotkey('f3')
pag.typewrite('SU Cyg')
pag.hotkey('enter')
time.sleep(1)
now_su=datetime.now()
vrijeme_su=now_su.strftime('%m-%d-%Y %H-%M-%S')
folder='images/'
filename=' SU Cyg.png'
output_su=folder+vrijeme_su+filename
im3=scr.grab(bbox=(7,322,328,336))
im3.save(output_su)

x=ocr_core(output_cep)
x=x.split('\n',1)
x=x[0]
x=x.replace('Next maximum light: ','')
x=x.replace(' UTC','')
print('Delta Cep')
print(x)
yr_cep=x[:4]
mo_cep=x[x.find('-')+1:x.replace('-','X',1).find('-')]
if mo_cep.find('0')==0:
    mo_cep=mo_cep[1:]
da_cep=x[x.find('-',6)+1:10]
if da_cep.find('0')==0:
    da_cep=da_cep[1:]
hr_cep=x[x.find(' ')+1:x.find(':')]
if hr_cep.find('0')==0:
    hr_cep=hr_cep[1:]
mi_cep=x[x.find(':')+1:x.find(':',x.find(':')+1,len(x))]
se_cep=x[17:]
if se_cep.find('0')==0:
    se_cep=se_cep[1:]
if mi_cep.find('0')==0:
    mi_cep=mi_cep[1:]
if int(hr_cep)>=14 or (int(hr_cep)==14 and int(mi_cep)>=0):
    jd_cep=(int(hr_cep)+1.98+(int(mi_cep)/60+(int(se_cep)+1)/3600)-14)/24
    x=date(int(yr_cep),int(mo_cep),int(da_cep)).toordinal()+1721425+jd_cep
else:
    jd_cep=(14-(int(hr_cep)+1.98+(int(mi_cep)/60)+(int(se_cep)+1)/3600))/24
    x=date(int(yr_cep),int(mo_cep),int(da_cep)).toordinal()+1721425-jd_cep
x=round(x,6)
#print(yr_cep,mo_cep,da_cep,hr_cep,mi_cep,se_cep)
print(x)
print()

y=ocr_core(output_pol)
y=y.split('\n',1)
y=y[0]
y=y.replace('Next maximum light: ','')
y=y.replace(' UTC','')
print('Polaris')
print(y)
yr_pol=y[:4]
mo_pol=y[y.find('-')+1:y.replace('-','X',1).find('-')]
if mo_pol.find('0')==0:
    mo_pol=mo_pol[1:]
da_pol=y[y.find('-',6)+1:10]
if da_pol.find('0')==0:
    da_pol=da_pol[1:]
hr_pol=y[y.find(' ')+1:y.find(':')]
if hr_pol.find('0')==0:
    hr_pol=hr_pol[1:]
mi_pol=y[y.find(':')+1:y.find(':',y.find(':')+1,len(y))]
if mi_pol.find('0')==0:
    mi_pol=mi_pol[1:]
se_pol=y[17:]
if se_pol.find('0')==0:
    se_pol=se_pol[1:]
if int(hr_pol)>=14 or (int(hr_pol)==14 and int(mi_pol)>=0):
    jd_pol=(int(hr_pol)+1.98+(int(mi_pol)/60)+(int(se_pol)+1)/3600-14)/24
    y=date(int(yr_pol),int(mo_pol),int(da_pol)).toordinal()+1721425+jd_pol
else:
    jd_pol=(14-(int(hr_pol)+1.98+(int(mi_pol)/60)+(int(se_pol)+1)/3600))/24
    y=date(int(yr_pol),int(mo_pol),int(da_pol)).toordinal()+1721425-jd_pol
y=round(y,6)
#print(yr_pol,mo_pol,da_pol,hr_pol,mi_pol,se_pol)
print(y)
print()

z=ocr_core(output_x)
z=z.split('\n',1)
z=z[0]
z=z.replace('Next maximum light: ','')
z=z.replace(' UTC','')
print('X Cyg')
print(z)
yr_x=z[:4]
mo_x=z[z.find('-')+1:z.replace('-','X',1).find('-')]
if mo_x.find('0')==0:
    mo_x=mo_x[1:]
da_x=z[z.find('-',6)+1:10]
if da_x.find('0')==0:
    da_x=da_x[1:]
hr_x=z[z.find(' ')+1:z.find(':')]
if hr_x.find('0')==0:
    hr_x=hr_x[1:]
mi_x=z[z.find(':')+1:z.find(':',z.find(':')+1,len(z))]
if mi_x.find('0')==0:
    mi_x=mi_x[1:]
se_x=z[17:]
if se_x.find('0')==0:
    se_x=se_x[1:]
if int(hr_x)>=14 or (int(hr_x)==14 and int(mi_x)>=0):
    jd_x=(int(hr_x)+1.98+(int(mi_x)/60)+(int(se_x)+1)/3600-14)/24
    z=date(int(yr_x),int(mo_x),int(da_x)).toordinal()+1721425+jd_x
else:
    jd_x=(14-(int(hr_x)+1.98+(int(mi_x)/60)+(int(se_x)+1)/3600))/24
    z=date(int(yr_x),int(mo_x),int(da_x)).toordinal()+1721425-jd_x
z=round(z,6)
#print(yr_x,mo_x,da_x,hr_x,mi_x,se_x)
print(z)
print()

q=ocr_core(output_su)
q=q.split('\n',1)
q=q[0]
q=q.replace('Next maximum light: ','')
q=q.replace(' UTC','')
print('SU Cyg')
print(q)
yr_su=q[:4]
mo_su=q[q.find('-')+1:q.replace('-','X',1).find('-')]
if mo_su.find('0')==0:
    mo_su=mo_su[1:]
da_su=q[q.find('-',6)+1:10]
if da_su.find('0')==0:
    da_su=da_su[1:]
hr_su=q[q.find(' ')+1:q.find(':')]
if hr_su.find('0')==0:
    hr_su=hr_su[1:]
mi_su=q[q.find(':')+1:q.find(':',q.find(':')+1,len(q))]
if mi_su.find('0')==0:
    mi_su=mi_su[1:]
se_su=q[17:]
if se_su.find('0')==0:
    se_su=se_su[1:]
if int(hr_su)>=14 or (int(hr_su)==14 and int(mi_su)>=0):
    jd_su=(int(hr_su)+1.98+(int(mi_su)/60)+(int(se_su)+1)/3600-14)/24
    q=date(int(yr_su),int(mo_su),int(da_su)).toordinal()+1721425+jd_su
else:
    jd_su=(14-(int(hr_su)+1.98+(int(mi_su)/60)+(int(se_su)+1)/3600))/24
    q=date(int(yr_su),int(mo_su),int(da_su)).toordinal()+1721425-jd_su
q=round(q,6)
#print(yr_su,mo_su,da_su,hr_su,mi_su,se_su)
print(q)
print()


ctime1=os.path.getmtime('D:\Dokumenti\ASTRONOMIJA\Cefeide\CEFEIDE\Delta Cep\Delta Cep {}.jpg'.format(file_cep))
ctime1=datetime.utcfromtimestamp(ctime1).strftime('%Y-%m-%d %H:%M:%S')
corr=int(ctime1[ctime1.find(' '):ctime1.find(' ')+3])+2
corr=' '+str(corr)
ctime1=ctime1.replace(ctime1[ctime1.find(' '):ctime1.find(' ')+3],str(corr))
ctime1_yr=ctime1[:4]
ctime1_mo=ctime1[5:7]
ctime1_da=ctime1[8:10]
ctime1_hr=ctime1[11:13]
ctime1_mi=ctime1[14:16]
ctime1_se=ctime1[17:19]
if ctime1_mo.find('0')==0:
    ctime1_mo=ctime1_mo[1:]
if ctime1_da.find('0')==0:
    ctime1_da=ctime1_da[1:]
if ctime1_hr.find('0')==0:
    ctime1_hr=ctime1_hr[1:]
if ctime1_mi.find('0')==0:
    ctime1_mi=ctime1_mi[1:]
if ctime1_se.find('0')==0:
    ctime1_se=ctime1_se[1:]

if float(ctime1_hr)>=14 or (float(ctime1_hr)==14 and float(ctime1_hr)>=0):
    ctime1_jd=(int(ctime1_hr)+(int(ctime1_mi)/60)+(int(ctime1_se)+1)/3600-14)/24
    ctime1=date(int(ctime1_yr),int(ctime1_mo),int(ctime1_da)).toordinal()+1721425+ctime1_jd
else:
    ctime1_jd=(14-(int(hr_pol)+(int(mi_pol)/60)+(int(se_pol)+1)/3600))/24
    ctime1=date(int(yr_pol),int(mo_pol),int(da_pol)).toordinal()+1721425-ctime1_jd
print(ctime1)
if float(x)-float(ctime1)<=(0.25*per_cep):
    delta_cep=4.37-(pad_cep*(float(ctime1)-(float(x)-0.25*per_cep)))
    delta_cep=round(delta_cep,2)
    print('Delta Cep: {}'.format(delta_cep))

else:
    delta_cep=(up_cep*(float(ctime1)-(float(x)-per_cep)))+3.48
    delta_cep=round(delta_cep,2)
    print('Delta Cep: {}'.format(delta_cep))


ctime2=os.path.getmtime('D:\Dokumenti\ASTRONOMIJA\Cefeide\CEFEIDE\Polaris\Polaris {}.jpg'.format(file_pol))
ctime2=datetime.utcfromtimestamp(ctime2).strftime('%Y-%m-%d %H:%M:%S')
corr2=int(ctime2[ctime2.find(' '):ctime2.find(' ')+3])+2
corr2=' '+str(corr2)
ctime2=ctime2.replace(ctime2[ctime2.find(' '):ctime2.find(' ')+3],str(corr2))
ctime2_yr=ctime2[:4]
ctime2_mo=ctime2[5:7]
ctime2_da=ctime2[8:10]
ctime2_hr=ctime2[11:13]
ctime2_mi=ctime2[14:16]
ctime2_se=ctime2[17:19]
if ctime2_mo.find('0')==0:
    ctime2_mo=ctime2_mo[1:]
if ctime2_da.find('0')==0:
    ctime2_da=ctime2_da[1:]
if ctime2_hr.find('0')==0:
    ctime2_hr=ctime2_hr[1:]
if ctime2_mi.find('0')==0:
    ctime2_mi=ctime2_mi[1:]
if ctime2_se.find('0')==0:
    ctime2_se=ctime2_se[1:]

if float(ctime2_hr)>=14 or (float(ctime2_hr)==14 and float(ctime2_hr)>=0):
    ctime2_jd=(int(ctime2_hr)+(int(ctime2_mi)/60)+(int(ctime2_se)+1)/3600-14)/24
    ctime2=date(int(ctime2_yr),int(ctime2_mo),int(ctime2_da)).toordinal()+1721425+ctime2_jd
else:
    ctime2_jd=(14-(int(hr_pol)+(int(mi_pol)/60)+(int(se_pol)+1)/3600))/24
    ctime2=date(int(yr_pol),int(mo_pol),int(da_pol)).toordinal()+1721425-ctime2_jd
print(ctime2)
if float(y)-float(ctime2)<=0.5*per_pol:
    polaris=2.13-(pad_pol*(float(ctime2)-(float(y)-0.5*per_pol)))
    polaris=round(polaris,2)
    print('Polaris: {}'.format(polaris))
else:
    polaris=(up_pol*(float(ctime2)-(float(y)-per_pol)))+1.86
    polaris=round(polaris,2)
    print('Polaris: {}'.format(polaris))

    
ctime3=os.path.getmtime('D:\Dokumenti\ASTRONOMIJA\Cefeide\CEFEIDE\X Cyg\X Cyg {}.jpg'.format(file_x))
ctime3=datetime.utcfromtimestamp(ctime3).strftime('%Y-%m-%d %H:%M:%S')
corr3=int(ctime3[ctime3.find(' '):ctime3.find(' ')+3])+2
corr3=' '+str(corr3)
ctime3=ctime3.replace(ctime3[ctime3.find(' '):ctime3.find(' ')+3],str(corr3))
ctime3_yr=ctime3[:4]
ctime3_mo=ctime3[5:7]
ctime3_da=ctime3[8:10]
ctime3_hr=ctime3[11:13]
ctime3_mi=ctime3[14:16]
ctime3_se=ctime3[17:19]
if ctime3_mo.find('0')==0:
    ctime3_mo=ctime3_mo[1:]
if ctime3_da.find('0')==0:
    ctime3_da=ctime3_da[1:]
if ctime3_hr.find('0')==0:
    ctime3_hr=ctime3_hr[1:]
if ctime3_mi.find('0')==0:
    ctime3_mi=ctime3_mi[1:]
if ctime3_se.find('0')==0:
    ctime3_se=ctime3_se[1:]

if float(ctime3_hr)>=14 or (float(ctime3_hr)==14 and float(ctime3_hr)>=0):
    ctime3_jd=(int(ctime3_hr)+(int(ctime3_mi)/60)+(int(ctime3_se)+1)/3600-14)/24
    ctime3=date(int(ctime3_yr),int(ctime3_mo),int(ctime3_da)).toordinal()+1721425+ctime3_jd
else:
    ctime3_jd=(14-(int(hr_x)+(int(mi_x)/60)+(int(se_x)+1)/3600))/24
    ctime3=date(int(yr_x),int(mo_x),int(da_x)).toordinal()+1721425-ctime3_jd
print(ctime3)
if float(z)-float(ctime3)<=(0.25*per_x):
    x_cyg=6.91-(pad_x*(float(ctime3)-(float(z)-(0.3125*per_x)))) #ako ne, vrati na 0.25*per_x
    x_cyg=round(x_cyg,2)
    print('X Cyg: {}'.format(x_cyg))
else:
    x_cyg=(up_x*(float(ctime3)-(float(z)-per_x)))+5.85
    x_cyg=round(x_cyg,2)
    print('X Cyg: {}'.format(x_cyg))


ctime4=os.path.getmtime('D:\Dokumenti\ASTRONOMIJA\Cefeide\CEFEIDE\SU Cyg\SU Cyg {}.jpg'.format(file_su))
ctime4=datetime.utcfromtimestamp(ctime4).strftime('%Y-%m-%d %H:%M:%S')
corr4=int(ctime4[ctime4.find(' '):ctime4.find(' ')+3])+2
corr4=' '+str(corr4)
ctime4=ctime4.replace(ctime4[ctime4.find(' '):ctime4.find(' ')+3],str(corr4))
ctime4_yr=ctime4[:4]
ctime4_mo=ctime4[5:7]
ctime4_da=ctime4[8:10]
ctime4_hr=ctime4[11:13]
ctime4_mi=ctime4[14:16]
ctime4_se=ctime4[17:19]
if ctime4_mo.find('0')==0:
    ctime4_mo=ctime4_mo[1:]
if ctime4_da.find('0')==0:
    ctime4_da=ctime4_da[1:]
if ctime4_hr.find('0')==0:
    ctime4_hr=ctime4_hr[1:]
if ctime4_mi.find('0')==0:
    ctime4_mi=ctime4_mi[1:]
if ctime4_se.find('0')==0:
    ctime4_se=ctime4_se[1:]

if float(ctime4_hr)>=14 or (float(ctime4_hr)==14 and float(ctime4_hr)>=0):
    ctime4_jd=(int(ctime4_hr)+(int(ctime4_mi)/60)+(int(ctime4_se)+1)/3600-14)/24
    ctime4=date(int(ctime4_yr),int(ctime4_mo),int(ctime4_da)).toordinal()+1721425+ctime4_jd
else:
    ctime4_jd=(14-(int(hr_su)+(int(mi_su)/60)+(int(se_su)+1)/3600))/24
    ctime4=date(int(yr_su),int(mo_su),int(da_su)).toordinal()+1721425-ctime4_jd
print(ctime4)
if float(q)-float(ctime4)<=(0.25*per_su):
    su_cyg=7.22-(pad_su*(float(ctime4)-(float(q)-(0.25* per_su))))
    su_cyg=round(su_cyg,2)
    print('SU Cyg: {}'.format(su_cyg))
else:
    su_cyg=(up_su*(float(ctime4)-(float(q)-per_su)))+6.44
    su_cyg=round(su_cyg,2)
    print('SU Cyg: {}'.format(su_cyg))

#print(x,ctime1,up_cep,pad_cep,y,ctime2,up_pol,pad_pol,z,ctime3,up_x,pad_x,q,ctime4,up_su,pad_su)
#f=open('Predviđene magnitude Cefeida.txt','a')
f=open('test.txt','a')
now=datetime.now()
vrijeme=now.strftime('%d.%m.%Y. %H:%M:%S')
f.write('\n'+'\n'+'{}'.format((ctime1+ctime2+ctime3+ctime4)/4)+'\n'+'\n'+'Delta Cep: {} - {}'.format(delta_cep,ctime1)+'\n'+'Polaris: {} - {}'.format(polaris,ctime2)+'\n'+'X Cyg: {} - {}'.format(x_cyg,ctime3)+'\n'+'SU Cyg: {} - {}'.format(su_cyg,ctime4)+'\n')
f.close()
import webbrowser
#webbrowser.open('Predviđene magnitude Cefeida.txt')
os.remove('{}'.format(output_cep))
os.remove('{}'.format(output_pol))
os.remove('{}'.format(output_x))
os.remove('{}'.format(output_su))
pag.hotkey('k')
#os.system('TASKKILL /F /IM stellarium.exe')
"""



