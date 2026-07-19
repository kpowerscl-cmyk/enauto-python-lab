hostname = "enauto-pi"
ssh_enabled = True
ram = 7.4

if ssh_enabled == True:
    print(hostname, "is ready for remote administration.")
else:
    print(hostname, "is NOT ready for remote administration.")

if ram >= 4:
    print("Enough RAM for automation lab.")
else:
    print("Not enough RAM.")
