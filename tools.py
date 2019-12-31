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
        grid_spacing {float} -- [与下层网格之间的间隔] (default: {0.9})
    
    Returns:
        [list] -- [初始持仓网格]
    """

    prices = []
    price = decimal.Decimal(str(price))
    for i in range(layer_num):
        prices.append(price)
        price = (price * decimal.Decimal(grid_spacing)).quantize(
            decimal.Decimal(price))
    return [[i + 1, str(prices[i]), None, None] for i in range(layer_num)]

def make_a_transaction(date, price, amount):
    """生成一条交易记录
    
    Arguments:
        date {[string]} -- [成交日期]
        price {[string]} -- [成交价格]
        amount {[string]} -- [成交数量]
    
    Returns:
        [tuple] -- [包含日期、价格及数量的元组]
    """
    return date, price, amount

def find_trigger_layer(grid_tbl, lastprice):
    """根据传入的价格找到触发层
    
    Arguments:
        grid_tbl {[list]} -- [持仓表格]
        lastprice {[string]} -- [当前股票价格]
    """

    if len(grid_tbl) <= 1:
        return None
    else: 



if __name__ == "__main__":
    f = open('data.json', 'w')
    json.dump({'600606': {'position_tbl': make_grid_position(3.88)}}, f)
    f.close()
