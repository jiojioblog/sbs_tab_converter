import argparse
import subprocess
from typing import List
import os
types: List[str] = ["sbsl", "sbsr", "sbs2l", "sbs2r", "abl", "abr", "ab2l", "ab2r"]
parser = argparse.ArgumentParser(description='3D video format conversion')
parser.add_argument('-f', dest='file', required=True, help='The name of the file to convert')
parser.add_argument('-s', dest="source", choices=types, required=True, help='The source format of the file')
parser.add_argument('-t', dest="target", choices=types, required=True, help='The target format of the file')
args = parser.parse_args()
filePath: str
fullFileName: str
fileName: str
fileExtension: str
filePath, fullFileName = os.path.split(args.file)
fileName, fileExtension = os.path.splitext(fullFileName)
targetFile: str = f'{filePath}/{fileName}_{args.target}{fileExtension}'
command: str = f'ffmpeg -i {args.file} -vf stereo3d={args.source}:{args.target} -c:a copy {targetFile}'
try:
    subprocess.run(command, shell=True, check=True, timeout=60)
except subprocess.TimeoutExpired:
    print("转换执行超时(超过60秒)")
except subprocess.CalledProcessError as e:
    print("转换执行失败，退出码:" + str(e.returncode))
