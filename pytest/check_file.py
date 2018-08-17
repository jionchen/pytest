#!/bin/env python
#coding:utf-8

import time
import sys
import os

def checktime(p):
    flag='null'
    t=time.strftime("%H", time.localtime(time.time()))
    if int(p) > int(t):
        flag='false'
    elif int(p) <= int(t):
        flag='true'
    return flag


if len(sys.argv) !=3:
    print("Usage:jiaobenming  lujing  shijian")
    os._exit(1)
elif len(sys.argv) ==3:
    m=checktime(sys.argv[2])
    if m=="false":
      print("shijianweidao")
      os._exit(0)
    elif m=="true":
      filename=sys.argv[1]
      if os.path.exists(filename):
         print("OK")
         os._exit(0)
      else:
         print("WARNING")
         os._exit(1)
