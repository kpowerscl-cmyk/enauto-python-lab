from pathlib import Path
import os
import socket

def get_hostname():
    return socket.gethostname()

def get_ip_address():
    try:
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        test_socket.connect(("8.8.8.8", 80))
        ip_address = test_socket.getsockname()[0]
        test_socket.close()
        return ip_address
    except OSError:
        return "Unable to get IP address"

def get_available_ram():
    meminfo = Path("/proc/meminfo").read_text()

    for line in meminfo.splitlines():
        if line.startswith("MemAvailable:"):
            ram_kb = int(line.split()[1])
            ram_gib = ram_kb / 1024 / 1024
            return round(ram_gib, 2)

    return None

def get_total_ram():
    meminfo = Path("/proc/meminfo").read_text()

    for line in meminfo.splitlines():
        if line.startswith("MemTotal:"):
            ram_kb = int(line.split()[1])
            ram_gib = ram_kb / 1024 / 1024
            return round(ram_gib, 2)

    return None

def get_cpu_cores():
    return os.cpu_count()

def display_device_info():
    hostname = get_hostname()
    ip_address = get_ip_address()
    available_ram = get_available_ram()
    total_ram = get_total_ram()
    cpu_cores = get_cpu_cores()

    print("===== Device Information =====")
    print("Hostname:", hostname)
    print("IP Address:", ip_address)
    print("Available RAM:", available_ram, "GiB")
    print("Total RAM:", total_ram, "GiB")
    print("CPU Cores:", cpu_cores)

def check_ram(ram):
    if ram >= 4:
       print("Enough RAM for lab.")
    else:
       print("Not enough RAM.")

def check_cpu(cpu_cores):
    if cpu_cores >= 2:
       print("Enough CPU cores for lab.")
    else:
       print("Not enough CPU cores.")

def lab_ready(ram, cpu_cores):
    if ram >= 4 and cpu_cores >= 2:
        print("LAB STATUS: READY")
    else:
        print("LAB STATUS: NOT READY")

def main():
    available_ram = get_available_ram()
    cpu_cores = get_cpu_cores()

    display_device_info()
    check_ram(available_ram)
    check_cpu(cpu_cores)
    lab_ready(available_ram, cpu_cores)

if __name__=="__main__":
    main()
