#!/usr/bin/env python
# _*_ coding: utf_8 _*_

import PySimpleGUI as sg
sg.set_options(element_padding=(0, 0), margins=(1, 1), border_width=0)

sg.change_look_and_feel('Topanga')

TRANSPARENCY = .8       # how transparent the window looks. 0 = invisible, 1 = normal window
POLL_FREQUENCY = 500    # how often to update graphs in milliseconds

red_exit_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAANkE3LLaAgAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAAASAAAAEgARslrPgAAAAl2cEFnAAAAEAAAABAAXMatwwAAAyNJREFUOMtFkk1onFUYhZ/7N9/MZDKdTvwmiUZa24CVJoHGLIIFSSm0gpEKoqsKdd8uFJcBKdKFi4CrLhQtXUmoYIUsWlQsCaUUhKabNoZGnJjENOn8Zv4y33fvdZGAi8PhXZyH88IRvljk52vXXh8cG/solc+HSmuk1kilUFojlEIeuJASvKdZKq2s3r8/13/kyI64PjV17I1z525kCoW3lVLog6BUCiEESimUMfv3AURobatbW9/NXb36qY6sfTfa3X2rbS1aKbSUKKXQQUB2dBRbqxGtryOV+h+itaJefz8cHLyht1dX+44OD6sgDPFC4KREADoMeWV8nPbaGltPn4KU+69pjTSGzvJy8vnSUlZ263WiUglfr+NqNUw2y6GJCZQQ4D0ijkmfOEFmchJhLbpaxVQquOVlbLWKFFGErddxlQqJbJbhixc5euYMSa3BWkQUkUkm6T99msPnz6PiGPHoETx4QAKQyntoNPDNJi+fPUsmDNm8eZPOkycAiG6Xxq1btO7epXdkhEQY4hbvobGohEaaA4DRmvzoKI3Hj6ncuYPb2KC5sEDn4UPE9jad27fx5TLJ4eOIQKFzGZTR6LRziEYDZS0mnaaxvo7f2cFrzYvZWRKAbrWI//4Lu7mJ7i+g+3KodgvZaKFT3iNbLaKNDaJymWBoCBHHUKvh4xi3u4ur15BjI4iBAezSHwgl0Klgf2Rp7xHNJu2VFV7Mz9N76hS56WnirS1csQjlMoQh6c8+R+VydH//FSE8OjAYKQ8a7O3h9vb4Z3aW7MmTvDozQ21igs7iIiaVoue9aVLjb9L58Qe6935BBgYNJKVAZ4zxylqkc3SLRVYvXWLo8mUOX7hAbmoKnMOurdH48gv25n9CECOyPSghfFJrxFw+/3EoxfWoUs0E1hIASSnpKRRIFwpo76BWgaiN7E2jMmlULsO/Xj/7fmnlA/GOVuEnx16bGQiCDw0kDWAA7dy+hEAmDDIwkDD4wFD3vryw/vzrK38++0Z8NRjybanaN/lSfjyTSh7yQiAAvAfnwTmEdRBbnHXEeDZa7c3fms2lXmj9BzlRUoovlDHoAAAALnpUWHRjcmVhdGUtZGF0ZQAAeNozMjCw0DWw1DUyCjE0sjIysjI21TawsDIwAABB/gUWQYgJbwAAAC56VFh0bW9kaWZ5LWRhdGUAAHjaMzIwsNA1sNQ1MgoxNLIyMrIyNtU2sLAyMAAAQf4FFiOw/pAAAAAASUVORK5CYII="
menu_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAABIAAAASABGyWs+AAAACXZwQWcAAAAQAAAAEABcxq3DAAAClElEQVQ4y42TP28cVRTFf3fmZWfH2oiQXeOFGAlp2Y29wqSD0kKiQKJ0Q49EwyeIaClAlHwGKJD4AFQuKUPhFYnXDlIss7sT2ztk1/Pnzbx3KYwdO2k47dE999x7z5Xd3V1EpDEcDr9oNpv3AM/rkDzPF6PR6OcwDOfb29tXhImiiECk2Wq1vo7j+CNAX61W9VJV1bEx5jdjzPw6Z+YOgkB4lqvccg7vvaA3VaqyICrO42537dNW6/ZwOp1KGIaSZdnS/DpxEAonLxZUFKCK6styr0qM4/uP7969/278oyqIgPcaCDwxk0mJBjVHnGA1uJhAL60rqp43GvB8a4X2bYxTBYS8KJkvbcN8tRkhQcB7/XeIoogLGpxzFEVBkWfMTk74aX/B8/0aUcUreO+pnERmrRUSBMJgtUkcx4CiXrFlyWS6YJJOiG3JwbMGjxcBgSpeFVTxzmH+uxKqirtYIlVVkSQJe6M/SdM5/f6A7z7pUge3sGVBWZaUpSXLstJczioihGGIqjJPU/b2RqTpnMFgQLvdpvtWTDNqkOWieQ555mSxFGcARC4c1HXNbDbj0aM/ODs7Y2PjPp1Oh6qq2B+PU2vtD8aYqbVWrLWyXC7/MVdREyFNUw4Pn5JlGVtbH7C6uoq1Fu893vvs6OjolyAIDnZ2dl4GqSgKVlZWmEwmHB//TZIk9Pvv0+l0sNZiraWua5xz1HUtYRjeSGnw4YMHHB7+tTUeH7x9enrKcLjJ+vo6InItynrpAu9vvor55uHDzzY2Nr9dLF4UvV7vd2OMJkly1bmqKqy1UhRFcn5+ngdBcFPgYH/8eZ7ls7P5/Ms7b9556pyjqqrX3lFVtSzL7LozAO6tddv9Xm8N4FX1/4N/AdR7ezI8buEfAAAALnpUWHRjcmVhdGUtZGF0ZQAAeNozMjCw0DWw1DUyDTEytDIxtjI10DawsDIwAABCPAUZLTMCvwAAAC56VFh0bW9kaWZ5LWRhdGUAAHjaMzIwMNM1NNA1NA8xNLMyMLYyNtA2sLAyMAAAQX8FDgMvDXEAAAAASUVORK5CYII="

main_layout = [
    [
        sg.Text('600606', size=(6, 1), key='_code_'),
        sg.Text('绿地控股', key='_security_', size=(8, 1)),
        sg.T('  '),
        sg.Text('当前持仓：'),
        sg.Text('3000股', size=(8, 1), key='_hold_'),
        sg.Text('买', size=(2, 1), key='_inout_'),
        sg.T('  '),
        sg.Button('',
                  image_data=red_exit_base64,
                  button_color=('black', 'black'),
                  size=(12, 1),
                  border_width=0,
                  key='Exit',
                  tooltip='关闭窗口')
    ],
    [
        sg.Text('6.86', size=(8, 1), key='_lastprice_'),
        sg.Text('2.5%', size=(8, 1), key='_changerate_'),
        sg.Text('-3.5%', size=(8, 1), key='_lscr_', justification='center'),
        sg.Text('6.8%', size=(8, 1), key='_lbcr_', justification='center')
    ],  #lscr:当前价格与最低卖出价格变化百分比, lbcr:当前价格与最低买入价变化百分比
    [
        sg.T('当前价', size=(8, 1)),
        sg.T('涨幅'),
        sg.T(' ' * 4),
        sg.T('比最低卖出'),
        sg.T('比最低买入'),
        sg.T(' ' * 6),
        sg.Button('',
                  image_data=menu_base64,
                  button_color=('black', 'black'),
                  size=(12, 1),
                  border_width=0,
                  key='Submenu',
                  tooltip='打开子菜单')
    ]
]

window = sg.Window('PSG System Dashboard',
                   main_layout,
                   keep_on_top=True,
                   auto_size_buttons=False,
                   grab_anywhere=True,
                   no_titlebar=True,
                   default_button_element_size=(12, 1),
                   return_keyboard_events=True,
                   alpha_channel=TRANSPARENCY,
                   use_default_focus=False,
                   finalize=True)

event, values = window.read()

window.close()
