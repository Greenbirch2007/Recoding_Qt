


import os

themes = ["5.应用程序主窗口","6.事件系统"
          ,"7.qt 对象模型与容器类","8.界面外观","9.国际化，帮助系统和qt 插件","10.2d绘图","11.图形视图，动画和状态机框架"
          ,"12.3d绘图","13.音视频播放","14.相机和音频录制","15.文件，目录和输入、输出","16.模型、视图编程"
          ,"17.数据库和xml","18.网络编程","19.进程和线程","20.qt webengine","附录a","附录b"]
base = "/home/wo/Recoding_Qt/Qt Creator快速入门(第三版)/"
for i in themes:
    file_name = base + str(i) + '/'
    print(file_name)
    # try:
    #     os.mknod("note.txt")
    #     # 创建目录
    #     # os.mkdir(file_name)
    #
    # except :
    #     pass