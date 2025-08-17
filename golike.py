import os
import subprocess
import sys
import time

while True:
    try:
        import json
        import requests
        import shutil
        import platform
        import cloudscraper
        import rich
        from bs4 import BeautifulSoup
        break
    except (ImportError, ModuleNotFoundError) as missing_lib:
        lib_name = missing_lib.name
        print(f"ĐANG CÀI ĐẶT THƯ VIỆN: [{lib_name}]")
        process = subprocess.Popen(
            [sys.executable, "-m", "pip", "install", lib_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        start_time = time.time()
        while process.poll() is None:
            elapsed = int(time.time() - start_time)
            print(f"Cài đặt {lib_name}... [{elapsed}s]", end='\r')
            time.sleep(0.1)
        if process.returncode == 0:
            print(f"THÀNH CÔNG .. [{lib_name}]")
            continue 
        else:
            print(f"THẤT BẠI .. [{lib_name}]. VUI LÒNG THỬ LẠI SAU.")
            print(process.stderr.read().decode())
            continue 
            
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
            
class Golike_Tiktok:
    def __init__(self):
        self.console = Console()
        self.headers = {}
        self.scraper = cloudscraper.create_scraper()
        self.mm = "~ [</>] -> "
        self.load_auth()
        self.chontk_data = self.get_accounts()
        self.dem = 0
        self.tong = 0
        self.delay = 0
        self.doiacc = 3
        self.checkdoiacc = 0
        self.account_id = None
        self.account_nickname = None
        self.job_type = "follow"
           
    def thanh(self, length):
        ngtuw = "=" * length + '\n'
        for x in ngtuw:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.005)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def banner(self):
        self.clear()
        ban = '''
███╗   ███╗ ██████╗ ███╗   ██╗███╗   ███╗███████╗ ██████╗
████╗ ████║██╔═══██╗████╗  ██║████╗ ████║██╔════╝██╔════╝
██╔████╔██║██║   ██║██╔██╗ ██║██╔████╔██║█████╗  ██║     
██║╚██╔╝██║██║   ██║██║╚██╗██║██║╚██╔╝██║██╔══╝  ██║     
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║ ╚═╝ ██║███████╗╚██████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝ ╚═════╝
                                                         
            © Copyright MONMEC 2025 - Do Not Edit !
'''
        for x in ban:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.005)
        self.thanh(60)
        print(self.mm + "Author: Nguyen Tu (NgTuw) Aka Thzyscoder")
        print(self.mm + "Facebook: https://fb.com/NgTuw")
        print(self.mm + "Telegram: https://t.me/NgTuw2712")
        print(self.mm + "Zalo: Key Vàng Trong Group Zalo !")
        print(self.mm + "Group Zalo: https://zalo.me/g/grthie511")
        self.thanh(60)
        print("[NAMETOOL] GOLIKE TIKTOK LỌC JOB 42Đ")       
        self.thanh(60)

    def nhap_auth(self):
        self.author = input("NHẬP AUTHORIZATION GOLIKE: ").strip()
        open("golike.txt", "w").write(self.author)
    
    def load_auth(self):
        self.banner()
        if not os.path.exists("golike.txt"):
            self.nhap_auth()
        else:
            print("[1] Sử dụng Authorization và Token hiện tại")
            print("[2] Nhập Authorization và Token mới")
            select = input("Nhập lựa chọn (1 hoặc 2): ").strip()
            if select == '1':
                data = open("golike.txt", "r").read().strip('\n').split('\n')
                if len(data) == 2:
                    self.author = data[0]
                else:
                    self.nhap_auth()
            elif select == "2":
                self.nhap_auth()

        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': self.author,
            't': 'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent': 'Mozilla/5.0',
            'Referer': 'https://app.golike.net/account/manager/tiktok'
        }

    def get_accounts(self):
        try:
            res = self.scraper.get('https://gateway.golike.net/api/tiktok-account', headers=self.headers)
            data = res.json()
            if data.get("status") != 200:
                raise Exception("Token/Auth không đúng")
            return data.get("data", [])
        except:
            print("Lỗi khi lấy danh sách tài khoản!")
            sys.exit(1)

    def show_accounts(self):
        print("\nDanh sách tài khoản TikTok:")
        for i, acc in enumerate(self.chontk_data):
            print(f"[{i+1}] {acc['nickname']}")

    def choose_account(self):
        self.show_accounts()
        while True:
            try:
                chon = int(input("Chọn tài khoản TikTok muốn chạy: "))
                if 1 <= chon <= len(self.chontk_data):
                    self.account_id = self.chontk_data[chon - 1]['id']
                    self.account_nickname = self.chontk_data[chon - 1]['nickname']
                    break
            except:
                pass
            print("Sai định dạng hoặc không hợp lệ, nhập lại!")

    def display_dashboard(self, price, link, status, delay_str):
        self.clear()
        table = Table(title="THÔNG TIN JOB GOLIKE", box=box.ROUNDED)
        table.add_column("Mục", justify="right")
        table.add_column("Thông tin", justify="left")
        table.add_row("Nick TikTok", self.account_nickname)
        table.add_row("Giá", price)
        table.add_row("Job thành công", str(self.dem))
        table.add_row("Tổng xu", str(self.tong))
        table.add_row("Link job", link)
        table.add_row("Trạng thái", status)
        table.add_row("Delay", delay_str)
        self.console.print(table)
        self.console.print(Panel.fit("Chúc bạn sài Tool vui vẻ"))

    def open_link(self, url):
        system = platform.system()
        try:
            if system == "Windows":
                subprocess.run(["start", "", url], shell=True)
            elif system == "Darwin":
                subprocess.run(["open", url])
            elif system == "Linux":
                if shutil.which("xdg-open"):
                    subprocess.run(["xdg-open", url])
                elif shutil.which("termux-open-url"):
                    subprocess.run(["termux-open-url", url])
                elif shutil.which("w3m"):
                    subprocess.run(["w3m", url])
                elif shutil.which("lynx"):
                    subprocess.run(["lynx", url])
                else:
                    print("Không tìm thấy lệnh nào để mở link.")
            else:
                print("Hệ điều hành không được hỗ trợ.")
        except Exception as e:
            print("Lỗi:", e)

    def countdown(self, sec, price, link, status):
        for i in range(sec, -1, -1):
            self.display_dashboard(price, link, status, f"{i}s")
            time.sleep(1)

    def nhan_job(self):
        params = {'account_id': self.account_id, 'data': 'null'}
        try:
            res = self.scraper.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs', headers=self.headers, params=params)
            return res.json()
        except:
            return None

    def hoanthanh(self, ads_id):
        payload = {'ads_id': ads_id, 'account_id': self.account_id, 'async': True, 'data': None}
        try:
            res = self.scraper.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=self.headers, json=payload)
            return res.json()
        except:
            return None

    def run(self):
        self.choose_account()
        self.delay = int(input("Delay giữa các job (giây): "))
        self.doiacc = int(input("Số lần thất bại thì đổi acc: "))
        while True:
            job = self.nhan_job()
            if not job or job.get("status") != 200:
                self.checkdoiacc += 1
                if self.checkdoiacc >= self.doiacc:
                    self.choose_account()
                    self.checkdoiacc = 0
                continue
            data = job.get("data", {})
            link = data.get("link", "")
            ads_id = data.get("id")
            price = data.get("price_per_after_cost", 0)
            type_job = data.get("type", "")
            if not link or not ads_id or price != 42 or type_job != "follow":
                self.checkdoiacc += 1
                continue
            self.open_link(link)
            self.countdown(self.delay, str(price), link, "Đang làm job")
            nhantien = self.hoanthanh(ads_id)
            if nhantien and nhantien.get("status") == 200:
                self.dem += 1
                self.tong += price
                self.checkdoiacc = 0
                self.display_dashboard(str(price), link, "Thành công", "")
                time.sleep(1)
            else:
                self.checkdoiacc += 1

if __name__ == "__main__":
    bot = Golike_Tiktok()
    bot.run()
