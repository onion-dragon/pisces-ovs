#!/usr/bin/env python3
import sys,getopt
opts,args=getopt.getopt(sys.argv[1:],"hi:o",["name","user","file","help"])
input_file=""
output_file=""
for op,value in opts:
  if op in ( "-n","--name"):
    input_file = value
  elif op in ("-u","--user"):
    output_file = value
  elif op in ("-f","--file"):
    output_file = value
  elif op in ("-h","--help"):
    print("------说明------")
    print("-n,--name 指定虚拟交换机的名称" )
    print("-u,--user 交换机所属用户 ")
    print("-f,--file 交换机源文件")
    print("-h,--help 获取帮助文件")


"""
  elif op == "-h":
    usage()
    sys.exit()
"""	  
