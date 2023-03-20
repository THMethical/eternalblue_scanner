import tkinter as tk
from tkinter import ttk
import socket
import nmap
import threading

root = tk.Tk()
root.title("EternalBlue Scanner")
root.geometry("400x250")

header_label = tk.Label(root, text="EternalBlue Scanner", font=("Arial", 16))
header_label.pack(pady=10)

def check_ip():
    ip_address = ip_entry.get()

    # Überprüfe, ob die IP-Adresse gültig ist
    try:
        socket.inet_aton(ip_address)
    except socket.error:
        result_label.config(text="Invalid IP address")
        return

    # Verwende Nmap, um den EternalBlue-Exploit-Status der IP-Adresse zu überprüfen
    nm = nmap.PortScanner()

    # Thread für den Scan starten
    scan_thread = threading.Thread(target=run_scan, args=(nm, ip_address))
    scan_thread.start()

def run_scan(nm, ip_address):
    # Fortschrittsbalken aktualisieren
    update_progress(nm, ip_address)

    if nm[ip_address]['tcp'][445]['name'] == 'microsoft-ds' and 'MS17-010' in nm[ip_address]['tcp'][445]['script']:
        result_label.config(text="EternalBlue exploit is possible")
    else:
        result_label.config(text="EternalBlue exploit is not possible")

    # Fortschrittsbalken zurücksetzen
    scan_progress.config(value=0)

def update_progress(nm, ip_address):
    while nm.still_scanning():
        # Fortschritt des Scans berechnen und in den Fortschrittsbalken schreiben
        progress = (len(nm[ip_address].all_hosts()) / nm._host_count) * 100
        scan_progress.config(value=progress)

    # Fortschrittsbalken auf 100% setzen, wenn der Scan abgeschlossen ist
    scan_progress.config(value=100)

ip_label = tk.Label(root, text="Enter an IP address:")
ip_label.pack()

ip_entry = tk.Entry(root, width=30)
ip_entry.pack()

check_button = tk.Button(root, text="Check", command=check_ip)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

scan_progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
scan_progress.pack(pady=10)

root.mainloop()
