def display_device_info(hostname, ip_address, ram):

    print("===== Device Information =====")
    print("Hostname:", hostname)
    print("IP Address:", ip_address)
    print("Available RAM:", ram, "GiB")

def check_ram(ram):

    if ram >= 4:
       print("Enough ram for lab.")
    else:
       print("Not enough ram for lab.")
