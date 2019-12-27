#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PySimpleGUI as sg

sg.change_look_and_feel('Topanga')

red_x = "R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="

main_layout = [[sg.Text('600606', size=(6, 1), key='--code--'), sg.Text('绿地控股', key='--security--', size=(8, 1)), sg.Text('当前持仓：'),
                sg.Text('3000股', size=(10, 1), key='--hold--'), sg.Text('买', size=(2, 1), key='--inout--'), 
                sg.Button('', image_data=red_x, button_color=('black', 'black'), size=(12, 1), key='Exit', tooltip='Close the window')],
                [sg.Text('6.86', size=(8, 1), key='--lastprice--'), sg.Text('2.5%', size=(8, 1), key='--changerate--'),
                sg.Text('-3.5%', size=(8, 1), key='--lscr--'), sg.Text('6.8%', size=(8, 1), key='--lbcr--')],          #lscr:当前价格与最低卖出价格变化百分比
                [sg.T('当前价', size=(8, 1)), sg.T('涨幅'), sg.T('相对最低卖出'), sg.T('相对最低买入'), sg.Button('展开')]]  #lbcr:当前价格与最低买入价s各变化百分比

window = sg.Window('PSG System Dashboard', main_layout,
                   keep_on_top=True,
                   auto_size_buttons=False,
                   grab_anywhere=True,
                   no_titlebar=True,
                   default_button_element_size=(12, 1),
                   return_keyboard_events=True,
                   alpha_channel=0.8,
                   use_default_focus=False,
                   finalize=True)

event, values = window.read()

window.close()
