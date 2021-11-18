# -*- coding: utf-8 -*-
"""
author:Fang Bicheng, Hu Xiaobo, Xue Renjie
instructor:Shen Ying
Tongji University
"""
'''
系统环境变量设置：
QT_QPA_PLATFORM_PLUGIN_PATH
（非常神奇的bug）
'''
'''
备注一下思路：
1 分为三个子文件 login register authentication（内含success 和fail 界面）
2 界面逻辑在这个文件内完成 剩下的ui设计和内部功能实现放在其余三个文件内
3 可能另外加一个behavior文件？
'''

from PyQt5.QtWidgets import *

import authentication
import login
import register

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    # 所有的ui转变的py文件都有修改
    # 初始化所有ui
    login_ui = login.Ui_login()
    login_ui.setupUi(login_ui)

    register_ui = register.Ui_user_register()
    register_ui.setupUi(register_ui)

    authentication_ui = authentication.Ui_authentication()
    authentication_ui.setupUi(authentication_ui)

    success_ui = authentication.Ui_success()
    success_ui.setupUi(success_ui)

    fail_ui = authentication.Ui_fail()
    fail_ui.setupUi(fail_ui)

    # 先写好各个ui间的逻辑关系 再细化
    # login
    login_ui.show()
    login_ui.register_pushButton.clicked.connect(register_ui.show)  # 不用括号表示函数！！
    login_ui.verification_pushButton.clicked.connect(authentication_ui.show)
    # register
    register_ui.record_pushButton.clicked.connect(register_ui.record_data)
    register_ui.save_pushButton.clicked.connect(register_ui.save)
    register_ui.back_pushButton.clicked.connect(register_ui.close)
    # authentication
    authentication_ui.back_pushButton.clicked.connect(authentication_ui.close)
    authentication_ui.start_pushButton.clicked.connect(authentication_ui.authenticate)

    sys.exit(app.exec_())
