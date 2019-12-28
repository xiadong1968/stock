"""该文件定义了股票数据源
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import abc

TIME_OUT = 0.1

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
    def last_price(self, code):
        """返回当前股票价格
        
        Arguments:
            codes {[string]} -- [股票代码：shxxxxxx, szxxxxxx]
        
        """
        pass


class SinaSource(ShareSource):
    """新浪数据源
    """
    def __init__(self, url='http://hq.sinajs.cn/'):
        ShareSource.__init__(self, url)

    def last_price(self, code):
        """获取当前股票价格
        
        Arguments:
            codes {[string]} -- [股票代码列表]
        
        Returns:
            [tuple] -- [股票代码，股票名称，当前股价]
        """
        url = self.url + 'list=' + code

        try:
            r = requests.get(url, timeout=TIME_OUT)
            r.raise_for_status()
        except:
            return '*' * 6, '*' * 6, '*' * 6
        else:
            p_data = re.compile('"([^"]*)"')  #提取股票数据
            p_code = re.compile('hq_str_s[hz]([0-9]{6,6})')  #提取股票代码
            try:
                data = p_data.search(r.text).group(1).split(',')
                code = p_code.search(r.text).group(1)
                return code, data[0].strip(), data[3].strip()
            except:
                return '*' * 6, '*' * 6, '*' * 6
