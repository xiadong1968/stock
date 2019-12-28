#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""该文件定义了股票数据源
"""

import requests
import re
import abc

class ShareSource(metaclass=abc.ABCMeta):
    """数据源抽象类
    """
    def __init__(self, url):    
        """
        Arguments:
            url {string} -- [数据源网址]
        """
        self.url = url
    @abc.abstractmethod
    def last_price(self, codes):
        """返回当前股票价格
        
        Arguments:
            codes {[list of string]} -- [股票代码：shxxxxxx, szxxxxxx]
        
        """
        pass

class SinaSource(ShareSource):
    """新浪数据源
    """
    def __init__(self, url='http://hq.sinajs.cn/'):
        super.__init__(self, url)
    
    def last_price(self, codes):
        url = self.url + '/list='
        first = True
        for code in codes:
            url += '' if first else ',' + code
            first = False 
        try:
            r = requests.get(url, timeout=0.01)
            r.raise_for_status()
        except:
            return None
        else:
            p_data = re.Pattern('"[^"]"')
            p_code = re.Pattern('hq_str_s[hz]([0-9]{6,6})')
            try:
                data = p_data.search(r.text).split(',')
                code = p_code.search(r.text).group(1) 

            


