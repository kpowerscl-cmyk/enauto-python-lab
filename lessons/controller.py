"""Use functions from lesson8 as a reusable system-check module."""

from datetime import datetime

import lesson8


def main():
    available_ram = lesson8.get_available_ram()
    cpu_cores = lesson8.get_cpu_cores()

    print("Available RAM:", available_ram, "GiB")
    lesson8.check_ram(available_ram)

    print("CPU Cores:", cpu_cores)
    lesson8.check_cpu(cpu_cores)

    lesson8.lab_ready(available_ram, cpu_cores)

    checked_at = datetime.now()
    print("Checked at:", checked_at.isoformat(timespec="seconds"))


if __name__ == "__main__":
    main()
