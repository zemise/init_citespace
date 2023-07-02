# Author zhaowang
# Date 2023-07-01 20:00
# CiteSpace启动脚本，同时日志记录
# version 1.0

import subprocess
import datetime
import os
import sys


# 检查字符是否为整数
def is_integer(input_str):
    try:
        num = int(input_str)
        return True
    except ValueError:
        return False


print(
    '''
    # Author zhaowang
    # Date 2023-07-01 20:00
    # CiteSpace启动脚本，同时日志记录
    # version 1.0
    
    # 此脚本默认运行CiteSpace最小内存为1G，最大内存为64G
    # 可调整最小内存限制，增强CiteSpace运行

Starting CiteSpace...
    '''
)

Xmx = input("请输入运行CiteSpace的最小内存(取值为整数，不大于电脑内存)：")

if not is_integer(Xmx):
    print("内存大小输入错误，本次启动默认最小内存为1G")
    Xmx = 1


def start_java_program():
    java_program_path = "CiteSpaceV.jar"
    log_dir_path = 'log/'
    logs_file = log_dir_path + datetime.datetime.now().strftime("log %m-%d.txt")

    if not os.path.exists(log_dir_path):
        os.mkdir(log_dir_path)

    time_stamp = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
    with open(logs_file, "a") as log_file:
        log_file.write(f"--- Java Program Log [{time_stamp}] ---\n")

    process = subprocess.Popen(
        ["java", "-Dfile.encoding=UTF-8", "-Duser.country=US", "-Duser.language=en", f"-Xms{Xmx}g", "-Xmx64g", "-Xss1m",
         "-jar", java_program_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        universal_newlines=True)

    for line in process.stdout:  # Print and write the output to the log file simultaneously
        timestamp = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
        print(f"[{timestamp}] {line}", end='')  # Print without newlines
        with open(logs_file, "a") as log_file:
            log_file.write(f"[{timestamp}] {line}")

    process.wait()


start_java_program()
