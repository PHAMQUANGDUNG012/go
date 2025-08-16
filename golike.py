import os
import sys,re
import datetime
from datetime import datetime, timedelta
import json
import random
import platform
from time import sleep
try:
  import requests
except ImportError:
  os.system('pip install requests')
  import requests
try:
  from colorama import Back, Fore, Fore, Style, init
except ImportError:
  os.system('pip install colorama')
  from colorama import Back, Fore, Fore, Style, init
try:
  from bs4 import BeautifulSoup
except ImportError:
  os.system('pip3 install beautifulsoup4')
  from bs4 import BeautifulSoup







def pr3(text):
  lines = text.split('\n')
  for line in lines:
      sys.stdout.write(line+'\n')
      sys.stdout.flush()
      sleep(0.1)
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.01)
  print()

def time():
  current_time = datetime.now()

  time = current_time.strftime("%M:%S")
  return time

def cint(number):
  while True:
    try:
      numbers = int(input(number))
      return numbers
    except ValueError:
      print(f'{red}Vui lòng chỉ nhập số')
from datetime import date, datetime
time=datetime.now().strftime("%H:%M:%S")
from matplotlib.table import Table
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay = now.strftime("%d")
thang = now.strftime("%m")
nam = now.strftime("%Y")
red = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
trang = "\033[1;37m"
tim = "\033[1;35m"
lam = "\033[1;36m"
xduong = "\033[1;34m"
thanh = f'{red}[{trang}</>{red}] {trang}=>'
tentool="GOLIKE TIKTOK VIP"      
def banner():
  os.system("cls" if os.name == "nt" else "clear")
  print (f'''
{lam}██████╗   ██████╗  ██████╗  ████████╗ ██████╗  ██████╗ ██╗     
{trang}██ ╔═██╗ ██╔═══██╗ ██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
{lam}██████╔╝ ██║   ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
{trang}██╔═══╝  ██║▄▄ ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
{lam}██║      ╚██████╔╝ ██████╔╝    ██║   ╚██████╔╝╚██████╔╝███████╗
{trang}╚═╝       ╚══▀▀═╝  ╚═════╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{trang}-----------------------------------------------------------------
{thanh} {luc}Admin{trang} : {vang}Phạm Quang Dũng 
{thanh} {luc}Zalo{trang} : {red}https://zalo.me/0336502026
{thanh} {luc}Ngày Hôm Nay{trang} : {red}{ngay}/{thang}/{nam}
{thanh} {luc}Giờ Hoạt Động{trang} : {red}{time}
{thanh} {luc}Đang Sử Dụng{trang} : {vang}{tentool}
{trang}----------------------------------------------------------------- ''')
def bes4(url):
  html_source = requests.get(url).text
  soup = BeautifulSoup(html_source, 'html.parser')
  og_description = soup.find('meta', {'property': 'og:description'})
  if og_description:
      text =og_description['content']
      return text
  else:
      print("Không tìm thấy thẻ meta với thuộc tính property='og:description'")
def changetoken():
  if os.path.exists("golike.txt"):
    text=f'''{thanh} {luc}Nhập {red}[{vang}1{red}] {luc}ĐỂ ĐỔI TÀI KHOẢN MỚI
{thanh} {luc}Nhập {red}[{vang}2{red}] {luc}DÙNG TÀI KHOẢN CŨ '''
    pr3(text)
    print(f'{trang}-----------------------------------------------------------------')
    changetoken=cint(f'{thanh} {luc}NHẬP LỰA CHỌN : {trang}')
    if changetoken==1:
      file_name = 'golike.txt'
      if os.path.exists(file_name):
          os.remove(file_name)
    else:
      pass
def checkauth():
    import cloudscraper
    scraper = cloudscraper.create_scraper()

    while True:
        if not os.path.exists("golike.txt"):
            banner()
            auth = str(input(f'{thanh} {luc}NHẬP AUTHORIZATION {trang}: '))

        else:
            with open('golike.txt') as f:
                auth = f.read().strip()

        headers = {
            'Authorization': auth,
            't': 'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent': "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        }

        try:
            response = scraper.get('https://gateway.golike.net/api/tiktok-account', headers=headers)
        except Exception as e:
            print(f"{thanh} {red}Không thể kết nối tới API")
            continue

        if response.status_code == 200:
            if response.text.strip():
                try:
                    check = response.json()
                except json.JSONDecodeError:
                    print(f"{thanh} {red}Phản hồi không hợp lệ (không phải JSON):")
                    print(response.text)
                    continue
            else:
                print(f"{thanh} {red}Phản hồi rỗng. Có thể AUTH không đúng.")
                continue
        else:
            print(f"{thanh} {red}AUTH sai hoặc bị từ chối (status code: {response.status_code})")
            continue

        if check.get('status') == 200:
            name = check['data'][0]['username']
            hea = {
                'Authorization': auth,
                't': 'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                'User-Agent': headers['User-Agent']
            }

            try:
                report_response = scraper.get('https://gateway.golike.net/api/statistics/report', headers=hea)
                data = report_response.json()
            except Exception:
                print(f"{thanh} {red} Lỗi khi lấy thống kê.")
                continue

            total_pending_coin = sum(
                value['pending_coin'] for key, value in data.items()
                if isinstance(value, dict) and 'pending_coin' in value
            )
            xht = data.get('current_coin', 0)
            banner()
            pr(f'{thanh} {luc}TÊN TÀI KHOẢN : {trang}{name}')
            pr(f'{thanh} {luc}SỐ DƯ HIỆN TẠI : {vang}{xht}đ')
            pr(f'{thanh} {luc}CHỜ DUYỆT : {vang}{total_pending_coin}đ')

            nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
            print(f'{trang}-----------------------------------------------------------------')
            pr(f'{thanh} {luc}ACC CÓ TRONG TÀI KHOẢN')
            for i, nickname in enumerate(nicknames, start=1):
                globals()[f'{i}'] = nickname
                pr(f'{thanh} {luc}Nhập {red}[{vang}{i}{red}] {trang}: {nickname}')

            with open("golike.txt", "w") as f:
                f.write(auth)

            return auth, check
        else:
            pr(f'{thanh}{luc} AUTH KHÔNG HỢP LỆ. VUI LÒNG NHẬP LẠI.')



def get_id_from_nickname_number():
  while True :
    print(f'{trang}-----------------------------------------------------------------')
    user_input=input(f'{thanh} {luc}CHỌN ACC TIKTOK MUỐN CHẠY JOB :{trang} ')
    try:
      n = int(user_input)
      if 'data' in check and len(check['data']) >= n:
          idtiktok = check['data'][n-1]['id']
          if idtiktok :
              text=f"{thanh} {luc}ID CỦA NICKNAME SỐ {n} LÀ : {trang}{idtiktok}"
              banner()
              pr(text)
              print(f'{trang}-----------------------------------------------------------------')
              return idtiktok 
          else:
              text=f"{thanh}{luc}KHÔNG TÌM THẤY NICKNAME TƯƠNG ỨNG."
              pr(text)
      else:
          continue 
    except ValueError:
          pr(f"{thanh} {luc}VUI LÒNG CHỈ NHẬP SỐ.")
          continue 





def getjob():
    startmaxjob=1
    job_success=0
    hea={
'Authorization':	auth,
't':'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}
    while True:
      while True:
        try:
              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
              break
        except:
            print(f"{red}Có lỗi gì đó ,đang nhận lại nhiệm vụ...")
            sleep(2)
            pass
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        os.system(f'termux-open-url {link}')
        for k in range(delay,-1,-1):
            print(f'{thanh}:{red}[{luc}{job_success}{trang}/{red}{startmaxjob}] {luc}LẤY NHIỆM VỤ MỚI SAU {red}[{trang}{k}s{red}]',end='\r')
            sleep(1)
        print(f'{thanh}{luc}Đang kiểm tra hành động...',end='\r')
        headers = {
            'authorization': auth,
        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                      }
      
        json_data = {
            'ads_id': id,
            'account_id': idtiktok ,
            'async': True,
            'data': None,
                      }
        while True:
            try:
                g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                break
            except:
                print(f'{red}Có lỗi gì đó, đang thử lại...',end="\r")
                sleep(2)
                pass
        if g['status']==200:
            job_success+=1
            dem+=1
            print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}]{red}[{trang}{job_success}{red}/{startmaxjob}]{lam}FOLLOW|+{vang}{g["data"]["prices"]}')
            startmaxjob+=1
            jobloi=0
            if startmaxjob == maxjob+1:
                print(f'{thanh} {luc}ĐÃ ĐẠT MAX JOB. ')
                return

        else:
            print(f'{luc}Đang kiểm tra lại hành động...',end="\r")
            sleep(2)
            while True:
                try:
                    g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                    break
                except:
                    print(f'{red}Đang nhận lại phần thưởng...',end="\r")
                    sleep(2)
            if g['status']==200:
                job_success+=1
                print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}]{red}[{trang}{job_success}{red}/{startmaxjob}]{lam}FOLLOW|+{vang}{g["data"]["prices"]}')
                startmaxjob+=1
                jobloi=0
                if startmaxjob == maxjob+1:
                    print(f'{thanh} {luc}ĐÃ ĐẠT MAX JOB. ')
                    return
            else:
                print(f'{red}Đang bỏ qua nhiệm vụ...',end='\r')
                headers = {
                    'authorization': auth,
                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                            }
                
                json_data = {
                    'description': 'Báo cáo hoàn thành thất bại',
                    'users_advertising_id': id,
                    'type': 'ads',
                    'provider': 'tiktok',
                    'fb_id': idtiktok ,
                    'error_type': 3,
                              }
                
                requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)
            
              
                headers = {
                    'authorization': auth,
                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                          }
                
                json_data = {
                    'ads_id': id,
                    'object_id': object_id,
                    'account_id': idtiktok ,
                    'type': 'follow',
                              }
                skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)
                startmaxjob+=1
                jobloi+=1
                if startmaxjob == maxjob+1:
                    print(f'{thanh} {luc}ĐÃ ĐẠT MAX JOB')
                    return
                elif jobloi==15:
                    select=input(f'{red}Lỗi nhiều ,Bạn có muốn đổi nick?(y/n):')
                    if select.lower() == 'n':
                        pass
                    else:
                        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
                        for i, nickname in enumerate(nicknames, start=1):
                            globals()[f'{i}'] = nickname
                        print(f'{trang}-----------------------------------------------------------------')
                        text=f'{thanh}  {luc} CHỌN ACC CHẠY NHIỆM VỤ '
                        pr(text)
                        # In giá trị của các biến
                        for i, nickname in enumerate(nicknames, start=1):
                            text=f'{red}[{luc}{i}{red}]: {globals()[f"{i}"]}'
                            pr(text)
                        idtiktok = get_id_from_nickname_number()
                        jobloi=0

      except:
          print(f'{red}Đang nhận lại nhiệm vụ...',end='\r')
          sleep(2)

  

def getjob_follow():
    startmaxjob=1
    job_success=0
    jobloi=0
    hea={
'Authorization':auth,
't':'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}
    while True:
      while True:
        try:
              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
              break
        except:
            print(f"{red}Có lỗi gì đó ,đang nhận lại nhiệm vụ...")
            sleep(2)
            pass
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        if 'video' in link:
            print(f"{red}ĐANG LỌC JOB LIKE           ",end='\r')
            headers = {
                'authorization': auth,
                't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                        }
            
            json_data = {
                'description': 'Tôi không muốn làm Job này',
                'users_advertising_id': id,
                'type': 'ads',
                'provider': 'tiktok',
                'fb_id': idtiktok,
                'error_type': 0,
                        }

            response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)

            
            json_data = {
                'ads_id': id,
                'object_id': object_id,
                'account_id': idtiktok,
                'type': 'like',
                        }
            response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)
        else:  
            os.system(f'termux-open-url {link}')
            for k in range(delay,-1,-1):
                print(f'{thanh}:{red}[{luc}{job_success}{trang}/{red}{startmaxjob}] {luc}LẤY NHIỆM VỤ MỚI SAU {red}[{trang}{k}s{red}]',end='\r')
                sleep(1)
            print(f'{luc}Đang kiểm tra hành động...',end='\r')
            headers = {
                'authorization': auth,
            't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                         }
          
            json_data = {
                'ads_id': id,
                'account_id': idtiktok ,
                'async': True,
                'data': None,
                         }
            while True:
                try:
                    g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                    break
                except:
                    print(f'{red}Có lỗi gì đó, đang thử lại...',end="\r")
                    sleep(2)
                    pass
            if g['status']==200:
                job_success+=1
                print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}]{red}[{trang}{job_success}{red}/{startmaxjob}]{lam}FOLLOW|+{vang}{g["data"]["prices"]}')
                startmaxjob+=1
                jobloi=0
                if startmaxjob == maxjob+1:
                    print(f'{thanh} {luc}ĐÃ ĐẠT MAX JOB. ')
                    return

            else:
                print(f'{luc}Đang kiểm tra lại hành động...',end="\r")
                sleep(2)
                while True:
                    try:
                        g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                        break
                    except:
                        print(f'{red}Đang nhận lại phần thưởng...',end="\r")
                        sleep(2)
                if g['status']==200:
                    job_success+=1
                    print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}]{red}[{trang}{job_success}{red}/{startmaxjob}]{lam}FOLLOW|+{vang}{g["data"]["prices"]}')
                    startmaxjob+=1
                    jobloi=0
                    if startmaxjob == maxjob+1:
                        print(f'{thanh} {luc}ĐÃ ĐẠT MAX JOB. ')
                        return
                else:
                    print(f'{red}Đang bỏ qua nhiệm vụ...',end='\r')
                    headers = {
                        'authorization': auth,
                        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                                }
                    
                    json_data = {
                        'description': 'Báo cáo hoàn thành thất bại',
                        'users_advertising_id': id,
                        'type': 'ads',
                        'provider': 'tiktok',
                        'fb_id': idtiktok ,
                        'error_type': 3,
                                 }
                    
                    requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)
                
                  
                    headers = {
                        'authorization': auth,
                        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                             }
                    
                    json_data = {
                        'ads_id': id,
                        'object_id': object_id,
                        'account_id': idtiktok ,
                        'type': 'follow',
                                 }
                    skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)
                    startmaxjob+=1
                    jobloi+=1
                    if startmaxjob == maxjob+1:
                        print(f'{thanh} {luc}ĐÃ ĐẠT ĐỦ JOB ')
                        return
                    elif jobloi==15:
                        select=input(f'{thanh} {red}Lỗi nhiều , Bạn có muốn đổi nick?(y/n):')
                        if select.lower() == 'n':
                            pass
                        else:
                            nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
                            for i, nickname in enumerate(nicknames, start=1):
                                globals()[f'{i}'] = nickname
                            print(f'{trang}-----------------------------------------------------------------')
                            text=f'{thanh} {luc}CHỌN ACC CHẠY NHIỆM VỤ '
                            pr(text)
                            # In giá trị của các biến
                            for i, nickname in enumerate(nicknames, start=1):
                                text=f'{red}[{luc}{i}{red}]: {globals()[f"{i}"]}'
                                pr(text)
                            idtiktok = get_id_from_nickname_number()
                            jobloi=0

      except:
          print(f'{red}Đang nhận lại nhiệm vụ...',end='\r')
          sleep(2)
while True:
  banner()
  changetoken() 
  auth,check =checkauth()
  if not os.path.exists("setting.txt"):
      idtiktok =get_id_from_nickname_number()
      print(f'''{thanh} {luc}Nhập {red}[{vang}1{red}] {luc}LỌC NHIỆM VỤ TYM
{thanh} {luc}Nhập {red}[{vang}2{red}] {luc}KHÔNG LỌC NHIỆM VỤ TYM ''')
      print(f'{trang}-----------------------------------------------------------------')
      select_job=cint(f'{thanh} {luc}NHẬP LỰA CHỌN :{trang}')
      delay =cint(f'{thanh} {luc}NHẬP DELAY : {trang}')
      maxjob= cint(f'{thanh} {luc}NHẬP MAX JOB : {trang}')
      setting={
        "loaijob":select_job,
        "delay":delay,
        "maxjob":maxjob
      }
      file = open("setting.txt", "a")  # Append mode
      file.write(json.dumps(setting))
      file.close()
      print(f'{trang}-----------------------------------------------------------------')
      sleep(1)
      if select_job==1:
        getjob_follow()
      else:
        getjob()   
          
                
  else: 
        idtiktok = get_id_from_nickname_number()
        select_setting=input(f'{thanh} {luc}BẠN CÓ MUỐN DÙNG SETTING CŨ [CÓ (y) | KHÔNG (n)]{trang}:' )
        if select_setting.lower() == 'n':
            os.remove('setting.txt')
            idtiktok =get_id_from_nickname_number()
            print(f'''{thanh} {luc}Nhập {red}[{vang}1{red}] {luc}CÓ
{thanh} {luc}Nhập {red}[{vang}2{red}] {luc}KHÔNG''')
            select_job=cint(f'{thanh} {luc}NHẬP LỰA CHỌN :{trang}')
            delay =cint(f'{thanh} {luc}NHẬP DELAY : {trang}')
            maxjob= cint(f'{thanh} {luc}NHẬP MAX JOB : {trang}')
            setting={
              "loaijob":select_job,
              "delay":delay,
              "maxjob":maxjob
            }
            file = open("setting.txt", "a")  # Append mode
            file.write(json.dumps(setting))
            file.close()

            print(f'{trang}-----------------------------------------------------------------')
            sleep(1)
            if select_job==1:
              getjob_follow()
            else:
              getjob()   
                
                      
        else:
          try:
              with open("setting.txt", "r") as file:
                data_txt=file.read()
                data_json = json.loads(data_txt)
                select_job = int(data_json.get('loaijob'))
                delay = int(data_json.get('delay'))
                maxjob= int(data_json.get('maxjob'))
                print(f'{trang}-----------------------------------------------------------------')
                sleep(1)
                if select_job==1:
                  getjob_follow()
                else:
                  getjob()
          except json.JSONDecodeError:
              print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại định dạng JSON trong tệp.")
          
