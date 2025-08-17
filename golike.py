import json
import os
import time
import cloudscraper
import requests
import webbrowser
from bs4 import BeautifulSoup
from colorama import Fore, init
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import box
import sys
init() 
from datetime import date, datetime
time=datetime.now().strftime("%H:%M:%S")
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
def banner():
  os.system("cls" if os.name == "nt" else "clear")
  print (f'''{lam}██████╗   ██████╗  ██████╗  ████████╗ ██████╗  ██████╗ ██╗     
{trang}██ ╔═██╗ ██╔═══██╗ ██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
{lam}██████╔╝ ██║   ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
{trang}██╔═══╝  ██║▄▄ ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
{lam}██║      ╚██████╔╝ ██████╔╝    ██║   ╚██████╔╝╚██████╔╝███████╗
{trang}╚═╝       ╚══▀▀═╝  ╚═════╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{trang}-----------------------------------------------------------------
{thanh}{luc}Admin{trang} : {vang}Phạm Quang Dũng 
{thanh}{luc}Zalo{trang} : {red}https://zalo.me/0336502026
{thanh}{luc}Ngày Hôm Nay{trang} : {red}{ngay}/{thang}/{nam}
{thanh}{luc}Giờ Hoạt Động{trang} : {red}{time}
{thanh}{luc}Đang Sử Dụng{trang} : {vang}{tentool}
{trang}-----------------------------------------------------------------''')
init(autoreset=True)
console = Console()
# Nhập auth
try:
    with open("Auth.txt", "x"):
        pass
except:
    pass

try:
    with open("Auth.txt", "r") as Auth:
        author = Auth.read().strip()
except:
    print("\033[1;31m Hãy tạo file Auth.txt\n")
    sys.exit(1)
banner()
print(f"{thanh}{luc}Nhập {red}[{vang}1{red}] {luc}Để Authorization hiện tại")
print(f"{thanh}{luc}Nhập {red}[{vang}2{red}] {luc}Để Nhập Authorization mới")
select = input(f"{thanh}{luc}Lựa Chọn Của Bạn Là : {trang}").strip()

if select == "1":
    if not author :
        print(f"{red}lỗi hãy nhập lại\n")
        sys.exit(1)
    print(f"{luc}ĐANG SỬ DỤNG LẠI AUTHORIZATION CŨ\n")
elif select == "2":
    banner()
    author = input(f"{thanh}{luc}NHẬP AUTHORIZATION GOLIKE: ").strip()
    try:
        with open("Auth.txt", "w") as Auth:
            Auth.write(author)
    except:
        print("\033[1;31m Hãy tạo file Auth.txt !\n")
        sys.exit(1)
else:
    print("\033[1;31mLựa chọn không hợp lệ! Vui lòng chọn 1 hoặc 2.")
    sys.exit(1)
banner()

print(f"{thanh}{luc}DANH SÁCH ACC CÓ TRONG TÀI KHOẢN")
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't':'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}
scraper = cloudscraper.create_scraper()

def chonacc():
    json_data = {}
    try:
        response = scraper.get(
            'https://gateway.golike.net/api/tiktok-account',
            headers=headers,
            json=json_data
        )
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict) or 'status' not in data:
            print(f"\033[1;31mInvalid account response: {data}")
            sys.exit(1)
        return data
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31mError fetching accounts: {e}")
        sys.exit(1)

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
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict) or 'status' not in data:
            print(f"\033[1;31mInvalid job response: {data}\n")
            return None
        return data
    except requests.exceptions.RequestException as e:
        return None

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
            timeout=20
        )
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict) or 'status' not in data:
            print(f"\033[1;31mInvalid complete job response: {data}")
            return None
        if data.get("status") != 200 and "already" in data.get("message", "").lower():
            return {"status": "already_completed", "message": data.get("message", "")}
        return data
    except requests.exceptions.HTTPError as e:
        return None
    except requests.exceptions.RequestException as e:
        return None
    except ValueError as e:
        return None

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
    except Exception:
        pass

def open_tiktok_link(link):
    try:
        os.system(f"termux-open-url '{link}'")
        time.sleep(2)
    except Exception:
        try:
            webbrowser.open(link)
            time.sleep(2)
        except Exception as e:
            print(f"\033[1;31mKhông mở được link tự động: {e}")
            print(f"\033[1;33mVui lòng mở link : {link}")

def countdown_delay(seconds, nickname, price_str, job_count, total, link, status):
    for i in range(seconds, -1, -1):
        display_dashboard(nickname, price_str, job_count, total, link, status, f"{i}...")
        time.sleep(1)
    display_dashboard(nickname, price_str, job_count, total, link, status, "")

def display_dashboard(nickname, price_str, job_count, total, link, status, delay_str):
    os.system('clear')  # Clear terminal

    table = Table(title=" PHẠM QUANG DŨNG GOLIKE TIKTOK", box=box.ROUNDED, border_style="bold white")
    table.add_column("📌 MỤC LỤC", justify="right", style="bold cyan")
    table.add_column("📤 THÔNG TIN", justify="left", style="bold magenta")

    table.add_row("TÀI KHOẢN TIKTOK", nickname)
    table.add_row("GIÁ XU", price_str)
    table.add_row("JOB THÀNH CÔNG", str(job_count))
    table.add_row("TỔNG XU NHẬN", str(total))
    table.add_row("LINK JOB", link)
    table.add_row("TRẠNG THÁI", status)
    table.add_row("DELAY", delay_str)
    console.print(table)
    console.print(Panel.fit("[bold green]CHÚC BẠN THÀNH CÔNG [bold green]", border_style="green"))


chontktiktok = chonacc()

def dsacc():
    if chontktiktok.get("status") != 200:
        print(f"{red}Authorization hoặc T sai\n")
        sys.exit(1)
    for i in range(len(chontktiktok["data"])):
        print(f"{thanh}{luc}Nhập {red}[{vang}{i+1}{red}] {luc}ĐỂ CHẠY TÀI KHOẢN : {trang} {chontktiktok['data'][i]['nickname']}")

dsacc()
print(f"{trang}-----------------------------------------------------------------")

while True:
    try:
        luachon = int(input(f"{thanh}{luc}Chọn tài khoản muốn chạy : {trang}"))
        if 1 <= luachon <= len(chontktiktok["data"]):
            account_id = chontktiktok["data"][luachon - 1]["id"]
            account_nickname = chontktiktok["data"][luachon - 1]["nickname"]
            break
        print(f"{thanh}Acc không có trong danh sách. Nhập lại!")
    except:
        print("\033[1;31mSai Định Dạng")

while True:
    try:
        delay = int(input(f"{thanh}{luc}DELAY THỰC HIỆN JOB : {trang}"))
        if delay >= 0:
            break
        print(f"{red}LỖI DELAY PHẢI LỚN ƠN 0")
    except:
        print(f"{red}LỖI RỒI ")

while True:
    try:
        doiacc = int(input(f"{thanh}{luc}ĐỔI ACC SAU : {trang}"))
        if doiacc > 0:
            break
        print("\033[1;31mSố lần thất bại phải lớn hơn 0!")
    except:
        print("\033[1;31m Nhập Sai \n")

dem = 0
tong = 0
checkdoiacc = 0
current_link = "N/A"
price_display = "Chưa check"
current_status = "Khởi động"

os.system('clear')

while True:
    if checkdoiacc >= doiacc:
        current_status = "Đổi acc TikTok"
        display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
        print(f" {account_nickname} gặp vấn đề ({checkdoiacc} lần thất bại) ")
        dsacc()
        while True:
            try:
                print(f"{Fore.WHITE}====================================")
                luachon = int(input("\033[1;32m Chọn tài khoản mới đê : \033[1;33m"))
                if 1 <= luachon <= len(chontktiktok["data"]):
                    account_id = chontktiktok["data"][luachon - 1]["id"]
                    account_nickname = chontktiktok["data"][luachon - 1]["nickname"]
                    checkdoiacc = 0
                    current_status = "Khởi động"
                    display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
                    break
                print("\033[1;31mAcc không hợp lệ. Nhập lại!\n")
            except:
                print("\033[1;31mSai định dạng\n")

    max_retries = 3
    retry_count = 0
    nhanjob = None
    current_status = "Lấy job"
    display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")

    while retry_count < max_retries:
        nhanjob = nhannv(account_id)
        if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
            break
        retry_count += 1
        time.sleep(2)

    if not nhanjob or retry_count >= max_retries:
        current_status = "Không lấy được job"
        display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
        time.sleep(1)
        checkdoiacc += 1
        continue

    ads_id = nhanjob["data"]["id"]
    current_link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    job_type = nhanjob["data"]["type"]

    time.sleep(3)  
# 3 giây check giá
    if "price_per_after_cost" not in nhanjob["data"]:
        price_display = "Không có giá"
        current_status = "Bỏ qua job"
        display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
        baoloi(ads_id, object_id, account_id, job_type)
        time.sleep(1)
        current_link = "N/A"
        continue

    job_price = nhanjob["data"]["price_per_after_cost"]
    price_color = "\033[1;32m" if job_price == 40 else "\033[1;31m"
    price_symbol = "=" if job_price == 40 else "≠"
    price_display = f"{job_price} {price_color}{price_symbol}\033[0m 40"
    display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
#
    if job_price != 40:
        current_status = "Bỏ qua job"
        display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
        baoloi(ads_id, object_id, account_id, job_type)
        time.sleep(1)
        current_link = "N/A"
        price_display = "Chưa check"
        continue

    if job_type != "follow":
        current_status = "Bỏ qua job"
        display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
        baoloi(ads_id, object_id, account_id, job_type)
        time.sleep(1)
        current_link = "N/A"
        price_display = "Chưa check"
        continue

    current_status = "Làm job"
    display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
    open_tiktok_link(current_link)
    countdown_delay(delay, account_nickname, price_display, dem, tong, current_link, current_status)

    current_status = "Nhận tiền"
    display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
    time.sleep(0.5)
#nhận 5 lần ko dc bỏ job 
    max_attempts = 5
    attempts = 0
    nhantien = None
    while attempts < max_attempts:
        nhantien = hoanthanh(ads_id, account_id)
        if nhantien and (nhantien.get("status") == 200 or nhantien.get("status") == "already_completed"):
            break
        attempts += 1
        time.sleep(1)

    if nhantien and nhantien.get("status") == 200:
        dem += 1
        tien = nhantien["data"].get("price_per_after_cost", job_price)
        if tien == 0:
            print(f"\033[1;31m Lỗi nhận tiền\n")
        tong += tien
        current_status = "Thành Công"
        display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
        time.sleep(0.7)
        checkdoiacc = 0
    elif nhantien and nhantien.get("status") == "already_completed":
        current_status = "Bỏ qua job vì đã nhận"
        display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
        baoloi(ads_id, object_id, account_id, job_type)
        time.sleep(1)
    else:
        current_status = "Nhận tiền lỗi"
        display_dashboard(account_nickname, price_display, dem, tong, current_link, current_status, "")
        baoloi(ads_id, object_id, account_id, job_type)
        time.sleep(1)
        checkdoiacc += 1

    current_link = "N/A"
    price_display = "Chưa check"
