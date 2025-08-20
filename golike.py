import json
#đã có chỉnh sửa
import os,time
import cloudscraper
import requests
import socket
import subprocess
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from colorama import Fore, init
import sys
from datetime import date, datetime
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
thanh = f'{red}[{trang}</>{red}] {trang}=> '
tentool="GOLIKE TIKTOK VIP"
def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        print("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")

kiem_tra_mang()
scraper = cloudscraper.create_scraper()

from colorama import Fore

banner = f"""
{lam}██████╗   ██████╗  ██████╗  ████████╗ ██████╗  ██████╗ ██╗     
{trang}██ ╔═██╗ ██╔═══██╗ ██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
{lam}██████╔╝ ██║   ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
{trang}██╔═══╝  ██║▄▄ ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
{lam}██║      ╚██████╔╝ ██████╔╝    ██║   ╚██████╔╝╚██████╔╝███████╗
{trang}╚═╝       ╚══▀▀═╝  ╚═════╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{trang}-----------------------------------------------------------------
{thanh}{luc}Admin{trang} : {vang}Phạm Quang Dũng 
{thanh}{luc}Zalo{trang} : {red}https://zalo.me/0336502026
{thanh}{luc}Ngày Hôm Nay{trang} : {red}{ngay}/{thang}/{nam}
{thanh}{luc}Đang Sử Dụng{trang} : {vang}{tentool}
{trang}-----------------------------------------------------------------"""
os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
#Nhập auth
try:
  Authorization = open("Authorization.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
author = Authorization.read()
if author == "":
  author = input("\033[1;32mNHẬP AUTHORIZATION : \033[1;33m")
  Authorization = open("Authorization.txt","w")
  Authorization.write(author)
else:
  print(f"{thanh}{luc}Nhập {red}[{vang}1{red}] {luc}Để Dùng Tài Khoản Cũ")
  print(f"{thanh}{luc}Nhập {red}[{vang}2{red}] {luc}Để Dùng Tài Khoản Mới")
  select = input(f"{thanh}{luc}Lựa Chọn Của Bạn Là : {trang}")
  kiem_tra_mang()
if select == "1":
    if not author :
        print(f"{red}lỗi hãy nhập lại\n")
        sys.exit(1)
elif select == "2":
    os.system('cls' if os.name== 'nt' else 'clear')
    print(banner)
    author = input(f"{thanh}{luc}NHẬP AUTHORIZATION GOLIKE: ").strip()
    try:
        with open("Authorization.txt", "w") as Auth:
            Auth.write(author)
    except:
        print("Hãy tạo file Authorization.txt \n")
        sys.exit(1)
else:
    print(f"{thanh}Lựa chọn không hợp lệ! Vui lòng chọn 1 hoặc 2.")
    sys.exit(1)
os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
print(f"{thanh}{luc}DANH SÁCH ACC TRONG TÀI KHOẢN")
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': 'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}
scraper = cloudscraper.create_scraper()
def chonacc():
    json_data = {}
    response = scraper.get(
        'https://gateway.golike.net/api/tiktok-account',
        headers=headers,
        json=json_data
    ).json()
    return response
def nhannv(account_id):
    try:
        params = {
            'account_id': account_id,
            'data': 'null',
        }
        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',
            headers=headers,
            params=params,
            json={}
        )
        return response.json()
    except Exception as e:
        print()
        return {}
def hoanthanh(ads_id, account_id):
    try:
        json_data = {
            'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None,
        }
        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=6
        )
        return response.json()
    except Exception as e:
        print()
        return {}
def baoloi(ads_id, object_id, account_id, loai):
    try:
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'tiktok',
            'fb_id': account_id,
            'error_type': 6,
        }
        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)
        json_data2 = {
            'ads_id': ads_id,
            'object_id': object_id,
            'account_id': account_id,
            'type': loai,
        }
        scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
            headers=headers,
            json=json_data2,
        )
    except Exception as e:
        print()
# Gọi chọn tài khoản một lần và xử lý lỗi nếu có
chontktiktok = chonacc()
def dsacc():
  if chontktiktok.get("status") != 200:  
    print("\033[1;31mAuthorization hoăc T sai   ")
    quit()
  for i in range(len(chontktiktok["data"])):
    print(f'{thanh}{luc}Nhập {red}[{vang}{i+1}{red}] {trang}{chontktiktok["data"][i]["nickname"]} ')
dsacc() 
print(f"{trang}-----------------------------------------------------------------")
while True:
  try:
    luachon = int(input(f"{thanh}{luc}Chọn tài khoản TIKTOK : {trang}"))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input(f"{thanh}{luc}Không Có Trong Danh Sách , Nhập Lại : {trang}"))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print(f"{thanh}{red}Sai Định Dạng") 
while True:
  try:
    delay = int(input(f"{thanh}{luc}Delay :{trang} "))
    break
  except:
    print(f"{thanh}{red}Sai Định Dạng  ")
while True:
  try: 
    doiacc = int(input(f"{thanh}{luc}Lỗi Bao Nhiêu Lần Đổi Acc :{trang} "))
    break
  except:
    print(f"{thanh}{luc}Nhập Vào 1 Số  ")
os.system("cls" if os.name == "nt" else "clear")
print(banner)  
print(f"{thanh} {luc}Nhập {red}[{vang}1{red}] {luc}Để Chạy Followers")
print(f"{thanh} {luc}Nhập {red}[{vang}2{red}] {luc}Để chạy Like")
print(f"{thanh} {luc}Nhập {red}[{vang}3{red}] {luc}Follow và Like")
while True:
    try:
        loai_nhiem_vu = int(input(f"{thanh}{luc}Chọn loại nhiệm vụ : {trang}"))
        if loai_nhiem_vu in [1, 2, 3]:
            break
        else:
            print(f"{thanh}{luc}Vui lòng chọn số từ 1 đến 3")
    except:
        print(f"{thanh}{luc}Vui lòng nhập số.")  
x_like, y_like, x_follow, y_follow = None, None, None, None
os.system("cls" if os.name == "nt" else "clear")
print(banner)
print(f"{thanh}{luc}Nhập {red}[{vang}1{red}] {luc}Chạy ADB tự động")
print(f"{thanh}{luc}Nhập {red}[{vang}2{red}] {luc}Không Chạy ADB tự động ")
adbyn = input(f"{thanh}{luc}Nhập lựa chọn : {trang}")
if adbyn == "1":
    def setup_adb():
      config_file = "adb_config.txt"
      like_coords_file = "toa_do_tim.txt"
      follow_coords_file = "toa_do_follow.txt"
    # Nhập IP và port ADB
      print(f"{Fore.MAGENTA}═══════════════════════════════════")
      
      ip = input(f"{thanh}{luc}Nhập IP của thiết bị {red}({trang}192.168.1.2{red}) : {trang}")
      adb_port = input(f"{thanh}{luc}Nhập port của thiết bị {red}({trang}39327{red}) : {trang}")
      # Kiểm tra và đọc tọa độ từ file nếu tồn tại
      x_like, y_like, x_follow, y_follow = None, None, None, None    
      if os.path.exists(like_coords_file):
           with open(like_coords_file, "r") as f:
              coords = f.read().split("|")
              if len(coords) == 2:
                   x_like, y_like = coords
                   print(f"{thanh}{luc}Đã tìm thấy tọa độ nút tim : {trang}X ={vang}{x_like} {trang}Y ={vang}{y_like}")    
      if os.path.exists(follow_coords_file):
          with open(follow_coords_file, "r") as f:
               coords = f.read().split("|")
               if len(coords) == 2:
                   x_follow, y_follow = coords
                   print(f"{thanh}{luc}Đã tìm thấy tọa độ nút follow :{trang} X = {vang}{x_follow} {trang}Y = {vang}{y_follow}")
      if not os.path.exists(config_file):
           pair_code = input(f"{thanh}{luc}Nhập mã ghép nối 6 số {red}({trang}322763{red}) {trang}: ")
           pair_port = input(f"{thanh}{luc}Nhập port ghép nối {red}({trang}44832{red}) {trang}: ")
           with open(config_file, "w") as f:
               f.write(f"{pair_code}|{pair_port}")
      else:
          with open(config_file, "r") as f:
               pair_code, pair_port = [s.strip() for s in f.read().split("|")]  
      print(f"\n {thanh}{tim}Đang ghép nối với thiết bị")
      os.system(f"adb pair {ip}:{pair_port} {pair_code}")
      time.sleep(2)  
      print(f"{thanh}{luc}Đang kết nối ADB\033[0m")
      os.system(f"adb connect {ip}:{adb_port}")
      time.sleep(2)  
      devices = os.popen("adb devices").read()
      if ip not in devices:
        print(f"{thanh}{red}Kết nối thất bại")
        exit()    
       # Yêu cầu nhập tọa độ nếu chưa có
      print("\033[1;35m╔═════════════════════════════════╗")
      print("\033[1;35m║     \033[1;33m  NHẬP TỌA ĐỘ NÚT         \033[1;35m║")
      print("\033[1;35m╚═════════════════════════════════╝")    
      if loai_nhiem_vu in [1, 3] and (x_follow is None or y_follow is None):
           x_follow = input("\033[1;32mNhập tọa độ X của nút follow: \033[1;33m")
           y_follow = input("\033[1;32mNhập tọa độ Y của nút follow: \033[1;33m")
           with open(follow_coords_file, "w") as f:
               f.write(f"{x_follow}|{y_follow}")    
      if loai_nhiem_vu in [2, 3] and (x_like is None or y_like is None):
           x_like = input("\033[1;32mNhập tọa độ X của nút tim: \033[1;33m")
           y_like = input("\033[1;32mNhập tọa độ Y của nút tim: \033[1;33m")
           with open(like_coords_file, "w") as f:
              f.write(f"{x_like}|{y_like}")
      return x_like, y_like, x_follow, y_follow
# Khi gọi hàm setup_adb()
    x_like, y_like, x_follow, y_follow = setup_adb()
elif adbyn == "2":
    pass
# Thêm phần chọn loại nhiệm vụ sau khi chọn tài khoản và trước khi bắt đầu làm nhiệm vụ   
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        print(f"\033[1;31m  Acc Tiktok {dsaccloi} gặp vấn đề ")
        print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        dsacc()
        while True:
            try:
                print(f"{Fore.WHITE}════════════════════════════════════════════════════")
                luachon = int(input(f"{thanh}{luc}Chọn tài khoản mới {trang}: "))
                while luachon > len((chontktiktok)["data"]):
                    luachon = int(input(f"{thanh}{luc}Acc Này Không Trong Danh Sách, Hãy Nhập Lại : \033[1;33m"))
                account_id = chontktiktok["data"][luachon - 1]["id"]
                checkdoiacc = 0
                os.system('cls' if os.name== 'nt' else 'clear')
                for h in banner:
                    print(h,end = "")
                break  
            except:
                print("\033[1;31mSai Định Dạng !!!")
    print(f'{luc}Đang Tìm Nhiệm Vụ        ', end="\r")
    max_retries = 3
    retry_count = 0
    nhanjob = None
    while retry_count < max_retries:
        try:
            nhanjob = nhannv(account_id)
            if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                break
            else:
                retry_count += 1
                time.sleep(2)
        except Exception as e:
            retry_count += 1
            time.sleep(1)
    if not nhanjob or retry_count >= max_retries:
        continue
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    job_type = nhanjob["data"]["type"]
    # Kiểm tra loại nhiệm vụ
    if (loai_nhiem_vu == 1 and job_type != "follow") or \
       (loai_nhiem_vu == 2 and job_type != "like") or \
       (job_type not in ["follow", "like"]):
        baoloi(ads_id, object_id, account_id, job_type)
        continue
    # Mở link và kiểm tra lỗi
    try:
        if adbyn == "1":
            os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}" > /dev/null 2>&1')
        else:
            #os.system(f"termux-open-url {link}")
            subprocess.run(["termux-open-url", link])        
        for remaining in range(3, 0, -1):
            time.sleep(1)
        print("\r" + " " * 30 + "\r", end="")
    except Exception as e:
        baoloi(ads_id, object_id, account_id, job_type)
        continue
    # Thực hiện thao tác ADB
    if job_type == "like" and adbyn == "1" and x_like and y_like:
        os.system(f"adb shell input tap {x_like} {y_like}")
    elif job_type == "follow" and adbyn == "1" and x_follow and y_follow:
        os.system(f"adb shell input tap {x_follow} {y_follow}")
    # Đếm ngược delay
    for remaining_time in range(delay, -1, -1):
        color = "\033[1;36m" if remaining_time % 2 == 0 else "\033[1;37m"
        print(f"\r{color}| PQD-TOOL | {remaining_time}s |          ", end="")
        time.sleep(1)    
    print("\r                          \r", end="") 
    print(f"{luc}Đang Nhận Tiền          ",end = "\r")
    # Hoàn thành job
    max_attempts = 2
    attempts = 0
    nhantien = None
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien and nhantien.get("status") == 200:
                break
        except:
            pass  
        attempts += 1

    if nhantien and nhantien.get("status") == 200:
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)
                                      
        chuoi = (f'''
{tim}╔════════════╗╔═════════════════════╗
{tim}║ {lam}SỐ THỨ TỰ  {tim}║║{thanh} {lam}{dem}
{tim}║ {trang}THỜI GIAN  {tim}║║{thanh} {trang}{h}:{m}:{s}
{tim}║ {lam}NHIỆM VỤ   {tim}║║{thanh} {luc}{job_type}
{tim}║ {trang}XU NHẬN    {tim}║║{thanh} {vang}+{tien} VND
{tim}║ {lam}TỔNG XU    {tim}║║{thanh} {vang}{tong} VND
{tim}║ {trang}TRẠNG THÁI {tim}║║{thanh} {luc}THÀNH CÔNG
{tim}╚════════════╝╚═════════════════════╝
''')
        print("                                                    ", end="\r")
        print(chuoi)
        time.sleep(0.7)
        checkdoiacc = 0
    else:
        try:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            print("                                              ", end="\r")
            print(f"{thanh}{luc}Bỏ qua nhiệm vụ ", end="\r")
            time.sleep(1)
            checkdoiacc += 1
        except:
            pass
