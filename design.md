对于目前的设计来说，分块进行描述：
1.编译模块
编译模块应当实现的功能为：对于用户（网络管理员）提供接口，可以选择P4文件进行编译，生成Vagrant box，然后将vagrant box存储在指定的文件夹目录下。同时，向数据库中插入一条表，记录该交换机镜像存入仓库。

------表项内容------
name:虚拟交换机镜像名称
user:虚拟交换机创建人名称（用户/应用开发者）
path:虚拟交换机存储路径（在向交换机上部署虚拟交换机时需要调用）
------end------

具体操作流程：
1.用户调用python脚本，命令格式如下：
./pisces_switch build -n switch_name -u user_name -p /home/r630-2/longlcy/p4/test.p4(path_p4)
2.程序调用build函数
3.build函数调用shell脚本将p4文件复制到vagrant共享文件夹
cp /home/r630-2/longlcy/p4/test.p4(path_p4) /home/r630-2/longlcy/p4_common/
4.vagrant up 启动vagrant虚拟机
5.vagrant虚拟机执行编译脚本
6.vagrant虚拟机关闭
vagrant halt vagrant_name
7.打包vagrant虚拟机存储到指定目录
8.存储vagrant虚拟机信息到数据库
 
