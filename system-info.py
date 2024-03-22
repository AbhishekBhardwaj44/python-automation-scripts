import platform
import time
import psutil #sudo pip3.9 install psutil
import humanize #sudo pip3.9 install humanize

print("="*40,"SYSTEM INFORMATION","="*40)
uname = platform.uname()
print(f"Hostname: {uname.node}")
print(f"OS Type: {uname.system}")
print(f"Kernel Version: {uname.release}")
boot_time_stamp = psutil.boot_time()
print(f"Boot Time: {time.ctime(boot_time_stamp)}")

print("="*40,"CPU INFORMATION","="*40)
print(f"Total Cores: {psutil.cpu_count()}")
print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
print(f"Current CPU Frequency: {psutil.cpu_freq().current} Mhz")

print("="*40,"MEMORY INFORMATION","="*40)
mem = psutil.virtual_memory()
print(f"Total Memory: {humanize.naturalsize(mem.total)}")
print(f"Available Memory: {humanize.naturalsize(mem.available)}")
print(f"Used Memory: {humanize.naturalsize(mem.used)}")
print(f"Percentage Usage: {mem.percent}%")

print("="*40,"SWAP INFORMATION","="*40)
swap = psutil.swap_memory()
print(f"Total Swap: {humanize.naturalsize(swap.total)}")
print(f"Available Swap: {humanize.naturalsize(swap.free)}")
print(f"Used Swap: {humanize.naturalsize(swap.used)}")
print(f"Percentage Usage: {swap.percent}%")

print("="*40,"DISK INFORMATION","="*40)
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"Device Path: {partition.device}")
    print(f"Mountpoint: {partition.mountpoint}")
    print(f"FStype: {partition.fstype}")
    partition_usage = psutil.disk_usage(partition.mountpoint)
    print(f"Total Size: {humanize.naturalsize(partition_usage.total)}")
    print(f"Used Size: {humanize.naturalsize(partition_usage.used)}")
    print(f"Free Size: {humanize.naturalsize(partition_usage.free)}")
    print(f"Percentage Usage: {partition_usage.percent}%")
    print("------")

print("="*40,"PROCESS INFORMATION","="*40)
n = 0
for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(f"Process Name: {proc.info['name']} | Process ID: {proc.info['pid']}")
    n = n + 1
print(f"Total Number of Processes are: {n}")

print("="*40,"NETWORK INFORMATION","="*40)
network= psutil.net_if_addrs()
for interface_name,address in network.items():
    print(interface_name)
    for interface_data in address:
        if str(interface_data.family)=="AddressFamily.AF_INET":
            print(f"IP adress: {interface_data.address}")
