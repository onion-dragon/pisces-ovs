#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,getopt
opts,args=getopt.getopt(sys.argv[1],"hi",["build"]sys.argv[2:],"hi:o",["control","file","help"])
input_file=""
output_file=""
for op,value in opts:
  if op in ( "-b","--build"):
    input_file = value
    name=args[0]
    user=args[1]
    path=args[2]
    print("build pisces_switch %s from %s,user is %s"%(path,name,user))
  elif op in ("-u","--user"):
    output_file = value
  elif op in ("-f","--file"):
    output_file = value  
  elif op in ("-h","--help"):
    print("------说明------")
    print("-b,--build  编译虚拟交换机" )
    print("-c,--control 交换管理功能 ")
    print("-f,--file 交换机源文件")
    print("-h,--help 获取帮助文件")


"""
  elif op == "-h":
    usage()
    sys.exit()
"""	  
