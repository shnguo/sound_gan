import subprocess
import bleak
import argparse
import time
from log import get_logger
import os
import platform
logger = get_logger(os.path.basename(__file__))
earthquake = "./dataset/earthquake.wav"
babycry1 = "./dataset/babycry1.mp3"
babycry2 = "./dataset/babycry2.mp3"

xiyiji = "./dataset/xiyiji.aac"
yingerku ="./dataset/yingerku.aac"
weixin = "./dataset/weixin.aac"
dianzuan = "./dataset/dianzuan.aac"

import asyncio
# from bleak import BleakScanner,BleakClient


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, default='weixin_piece', help='For connection.')
    parser.add_argument('--hour',type=float,default=1.0)
    opt = parser.parse_args()
    # print_args(vars(opt))
    return opt


def main():
    start =time.time()
    opt  =  parse_opt()
    filepath = f"./dataset/{opt.type}.aac" 
    while True:
        logger.info(f'play {opt.type}')
        if platform.system()=='Darwin':
            return_code = subprocess.call(["afplay", filepath]) 
        elif  platform.system()=='Linux':
            return_code = subprocess.call(["mplayer", filepath])
        if time.time()-start>opt.hour*3600:
            break
        time.sleep(300)


if __name__=='__main__':
    main()


