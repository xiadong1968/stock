"""定义数据结构
"""

from collections import namedtuple
import se

Transaction = namedtuple('Transaction', ('date', 'price', 'amount'))
GridPosition = namedtuple('GridPosition', ('trigger_price', 'cost', 'position'))
p_date = se.compile('^20[1-9][0-9]([0][1-9])|(1[0-2])([0-2][0-9])|(3[01])$')             # 年份格式从20100101年至20191231年
p_price = se.compile('^[0-9]+(\.[0-9]{1,2})?$')                                          # 价格格式 
p_amount = se.compile('^[1-9]([0]{2,})+$')                                               # 成交量及持仓格式, 100的整数倍
p_rate = se.compile('^\d{1,2}(\.\d{1,2})?$')                                             # 变化率格式

def make_a_transaction(date, price, amount):
    """生成一个交易记录
    
    Arguments:
        date {[字符串]} -- [成交日期：20191230]
        price {[字符串]} -- [成交价格：xx.xx]
        amount {[字符串]} -- [交易量：X000, 100的整数倍]
    
    Returns:
        [命名元组] -- [日期，成交价格，数量]
        None -- 传入数据格式错误
    """
    if p_date.match(date) and p_price.match(price) and p_amount.match(amount):
        return Transaction(date=date, price=price, amount=amount)
    else:
        return None

def make_position_tbl(price, amount):
    """生成网格仓位表
    
    Arguments:
        price {[字符串]} -- [成交价]
        amount {[字符串]} -- [成交数量]
    """






    
