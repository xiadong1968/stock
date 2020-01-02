#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
定义一组操作股票数据的工具
"""

import decimal
import json


def make_grid_position(price, layer_num=6, grid_spacing=0.9):
    """生成初始持仓表格
    
    Arguments:
        price {[数值或数字字符型]} -- [网格第一层价格]
    
    Keyword Arguments:
        layer_num {int} -- [网格层数] (default: {6})
        grid_spacing {float} -- [层与层网格之间的间隔] (default: {0.9})
    
    Returns:
        [list] -- [初始持仓网格]
    """

    prices = []
    price = decimal.Decimal(str(price))
    for i in range(layer_num):
        prices.append(price)
        price = (price * decimal.Decimal(grid_spacing)).quantize(
            decimal.Decimal(price))
    return {str(i+1): [str(prices[i]), None, None] for i in range(layer_num)}  # 返回字典 {层号: [触发价格，持仓价格，持仓量]}



def find_buy_layer(grid_tbl, last_price):
    """根据传入的价格找到买入触发层
    
    Arguments:
        grid_tbl {[dict]} -- [持仓表格]
        lastprice {[string]} -- [当前股票价格]
    """

    layer = len(grid_tbl)
    while True:
        if layer <= 1:
            layer = None                            # 如果当前层号为最顶层，则返回None
            break
        if decimal.Decimal(last_price) <= decimal.Decimal(grid_tbl[str(layer)][0]) and not grid_tbl[str(layer)][2]:
            break                                   # 如果最新股价低于或等于当前层的触发价并且当前层持仓数为0，则结束当前查找
        layer = layer - 1                           # 否则将当前层的上一层当作当前层 
    
    return layer                                    # 如果找到，则返回当前找到的层号,否则返回None


def find_sell_layer(grid_tbl, last_price):
    """根据传入的价格找到卖出触发层
    
    Arguments:
        grid_tbl {[dict]} -- [持仓表格]
        last_price {[string]} -- [当前股票价格]
    """
    layer = 1                                       # 最顶层层号
    depth = len(grid_tbl)

    while True:
        if  layer >= depth:
            layer = None                            # 如果当前层达到或超过表格最大深度返回None
            break
        if decimal.Decimal(last_price) >= decimal.Decimal(grid_tbl[str(layer)][0]):
            layer += 1                              # 如是股票价格高于当前层触发价，则给出下一层的卖出信号，如果下一层持仓数不为0, 否则返回None
            layer = layer if layer <= depth and grid_tbl[str(layer)][2] else None
            break
        else:
            layer += 2                              # 如果股票价格小于当前层触发价，则将下面隔层层号做为当前层
    
    return layer                                    # 如果找到，则返回当前找到的层号，否则返回None


if __name__ == "__main__":
    import pprint

    grid_tbl = make_grid_position(3.88)
    print(grid_tbl)

    f = open('data.json', 'w')
    json.dump(grid_tbl, f)
    f.close()

    grid_tbl = json.load(open('data.json'))

    grid_tbl['2'][2] = '200'

    last_price = None

    while last_price != '0.0':
        print(grid_tbl)
        last_price = input('实时股票价格：')
        print('当前买入层号：{}'.format(find_buy_layer(grid_tbl, last_price)))
        print('当前卖出层号：{}'.format(find_sell_layer(grid_tbl, last_price)))

