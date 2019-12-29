#!/usr/bin/env python
# _*_ coding: utf_8 _*_

import PySimpleGUI as sg
from share import SinaSource

sg.set_options(element_padding=(0, 0),
               margins=(1, 1),
               border_width=0,
               font=('Times', 9),
               text_justification='center')

sg.theme(new_theme='Topanga')

TRANSPARENCY = .8  # how transparent the window looks. 0 = invisible, 1 = normal window
POLL_FREQUENCY = 500  # how often to update data in milliseconds
FLIP_TIME = 3000  # how long to show flowed share in milliseconds
BACKGROUND_COLOR = sg.theme_background_color()

red_exit_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAANkE3LLaAgAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAAASAAAAEgARslrPgAAAAl2cEFnAAAAEAAAABAAXMatwwAAAyNJREFUOMtFkk1onFUYhZ/7N9/MZDKdTvwmiUZa24CVJoHGLIIFSSm0gpEKoqsKdd8uFJcBKdKFi4CrLhQtXUmoYIUsWlQsCaUUhKabNoZGnJjENOn8Zv4y33fvdZGAi8PhXZyH88IRvljk52vXXh8cG/solc+HSmuk1kilUFojlEIeuJASvKdZKq2s3r8/13/kyI64PjV17I1z525kCoW3lVLog6BUCiEESimUMfv3AURobatbW9/NXb36qY6sfTfa3X2rbS1aKbSUKKXQQUB2dBRbqxGtryOV+h+itaJefz8cHLyht1dX+44OD6sgDPFC4KREADoMeWV8nPbaGltPn4KU+69pjTSGzvJy8vnSUlZ263WiUglfr+NqNUw2y6GJCZQQ4D0ijkmfOEFmchJhLbpaxVQquOVlbLWKFFGErddxlQqJbJbhixc5euYMSa3BWkQUkUkm6T99msPnz6PiGPHoETx4QAKQyntoNPDNJi+fPUsmDNm8eZPOkycAiG6Xxq1btO7epXdkhEQY4hbvobGohEaaA4DRmvzoKI3Hj6ncuYPb2KC5sEDn4UPE9jad27fx5TLJ4eOIQKFzGZTR6LRziEYDZS0mnaaxvo7f2cFrzYvZWRKAbrWI//4Lu7mJ7i+g+3KodgvZaKFT3iNbLaKNDaJymWBoCBHHUKvh4xi3u4ur15BjI4iBAezSHwgl0Klgf2Rp7xHNJu2VFV7Mz9N76hS56WnirS1csQjlMoQh6c8+R+VydH//FSE8OjAYKQ8a7O3h9vb4Z3aW7MmTvDozQ21igs7iIiaVoue9aVLjb9L58Qe6935BBgYNJKVAZ4zxylqkc3SLRVYvXWLo8mUOX7hAbmoKnMOurdH48gv25n9CECOyPSghfFJrxFw+/3EoxfWoUs0E1hIASSnpKRRIFwpo76BWgaiN7E2jMmlULsO/Xj/7fmnlA/GOVuEnx16bGQiCDw0kDWAA7dy+hEAmDDIwkDD4wFD3vryw/vzrK38++0Z8NRjybanaN/lSfjyTSh7yQiAAvAfnwTmEdRBbnHXEeDZa7c3fms2lXmj9BzlRUoovlDHoAAAALnpUWHRjcmVhdGUtZGF0ZQAAeNozMjCw0DWw1DUyCjE0sjIysjI21TawsDIwAABB/gUWQYgJbwAAAC56VFh0bW9kaWZ5LWRhdGUAAHjaMzIwsNA1sNQ1MgoxNLIyMrIyNtU2sLAyMAAAQf4FFiOw/pAAAAAASUVORK5CYII="
menu_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAABIAAAASABGyWs+AAAACXZwQWcAAAAQAAAAEABcxq3DAAAClElEQVQ4y42TP28cVRTFf3fmZWfH2oiQXeOFGAlp2Y29wqSD0kKiQKJ0Q49EwyeIaClAlHwGKJD4AFQuKUPhFYnXDlIss7sT2ztk1/Pnzbx3KYwdO2k47dE999x7z5Xd3V1EpDEcDr9oNpv3AM/rkDzPF6PR6OcwDOfb29tXhImiiECk2Wq1vo7j+CNAX61W9VJV1bEx5jdjzPw6Z+YOgkB4lqvccg7vvaA3VaqyICrO42537dNW6/ZwOp1KGIaSZdnS/DpxEAonLxZUFKCK6styr0qM4/uP7969/278oyqIgPcaCDwxk0mJBjVHnGA1uJhAL60rqp43GvB8a4X2bYxTBYS8KJkvbcN8tRkhQcB7/XeIoogLGpxzFEVBkWfMTk74aX/B8/0aUcUreO+pnERmrRUSBMJgtUkcx4CiXrFlyWS6YJJOiG3JwbMGjxcBgSpeFVTxzmH+uxKqirtYIlVVkSQJe6M/SdM5/f6A7z7pUge3sGVBWZaUpSXLstJczioihGGIqjJPU/b2RqTpnMFgQLvdpvtWTDNqkOWieQ555mSxFGcARC4c1HXNbDbj0aM/ODs7Y2PjPp1Oh6qq2B+PU2vtD8aYqbVWrLWyXC7/MVdREyFNUw4Pn5JlGVtbH7C6uoq1Fu893vvs6OjolyAIDnZ2dl4GqSgKVlZWmEwmHB//TZIk9Pvv0+l0sNZiraWua5xz1HUtYRjeSGnw4YMHHB7+tTUeH7x9enrKcLjJ+vo6InItynrpAu9vvor55uHDzzY2Nr9dLF4UvV7vd2OMJkly1bmqKqy1UhRFcn5+ngdBcFPgYH/8eZ7ls7P5/Ms7b9556pyjqqrX3lFVtSzL7LozAO6tddv9Xm8N4FX1/4N/AdR7ezI8buEfAAAALnpUWHRjcmVhdGUtZGF0ZQAAeNozMjCw0DWw1DUyDTEytDIxtjI10DawsDIwAABCPAUZLTMCvwAAAC56VFh0bW9kaWZ5LWRhdGUAAHjaMzIwMNM1NNA1NA8xNLMyMLYyNtA2sLAyMAAAQX8FDgMvDXEAAAAASUVORK5CYII="

col1 = [
    [sg.Text('', size=(6, 1), key='_code_')],
    [sg.Text('', size=(6, 1), key='_lastprice_', text_color=BACKGROUND_COLOR)],
    [sg.T('当前价')]
]

col2 = [
    [sg.Text('', key='_security_', size=(8, 1))],
    [sg.Text('2.5%', size=(8, 1), key='_changerate_')],
    [sg.T('涨幅', size=(8, 1))]
]

col3 = [
    [sg.Text('当前持仓', size=(10, 1))],
    [sg.Text('-3.5%', size=(10, 1), key='_lscr_')],     #lscr: lowest sold change rate
    [sg.T('比最低卖出')]
]

col4 = [
    [sg.Text('3000股', size=(8, 1), key='_hold_')],     #持仓量
    [sg.Text('6.8%', size=(10, 1), key='_lbcr_')],      #lbcr: lowest bought change rate
    [sg.T('比最低买入')]
]

col5 = [
    [sg.T('')],
    [sg.Text('买', key='_inout_')],
    [sg.T('')]
]

col6 = [
    [
        sg.Button('',
                  image_data=red_exit_base64,
                  button_color=(BACKGROUND_COLOR, BACKGROUND_COLOR),
                  border_width=0,
                  key='Exit',
                  tooltip='关闭窗口')
    ],
    [sg.T('')],
    [
        sg.Button('',
                  image_data=menu_base64,
                  button_color=(BACKGROUND_COLOR, BACKGROUND_COLOR),
                  border_width=0,
                  key='Submenu',
                  tooltip='打开子菜单')
    ]
]

cols = [col1, col2, col3, col4, col5, col6]
main_layout = [[sg.Column(col) for col in cols]]

window = sg.Window('股票实时行情',
                   main_layout,
                   keep_on_top=True,
                   auto_size_buttons=False,
                   grab_anywhere=True,
                   no_titlebar=True,
                   return_keyboard_events=True,
                   alpha_channel=TRANSPARENCY,
                   use_default_focus=False
                   )

sina = SinaSource()
shares = [
    'sh501029', 'sh510880', 'sh512880', 'sh512000', 'sh600606', 'sh600611'
]

index = 0           
length = len(shares)
poll_time = 0                        #存放已经流逝的poll时间
visible = False                      #设置闪烁效果
background_color = sg.theme_text_color()
while True:
    event, values = window.read(timeout=POLL_FREQUENCY)
    if event == 'Exit':
        break
    code, security, lastprice, changerate = sina.last_price(shares[index % length])
    window['_code_'].update(code)
    window['_security_'].update(security)
    window['_lastprice_'].update(lastprice, background_color=background_color)  #将字符的颜色与背景色设为一致，通过改变背景色实现闪烁效果
    window['_changerate_'].update(changerate)

    if visible:
        background_color = 'Green'
        visible = False
    else:
        background_color = BACKGROUND_COLOR 
        visible = True

    if poll_time >= FLIP_TIME:
        index += 1                  #如果显示当前的股票时间大于FLIP_TIME， 则切换至下一只股票
        poll_time = 0
    else:
        poll_time += POLL_FREQUENCY

window.close()
