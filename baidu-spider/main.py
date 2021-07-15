# -*- coding: utf-8 -*-
"""
Created on 2021-07-15 20:42:39
---------
@summary: 爬虫入口
---------
@author: Boris
"""

from spiders import *
from feapder.utils.custom_argparse import ArgumentParser


def baidu_spider1():
    baidu_spider.BaiduSpider(thread_count=100).start()


def baidu_spider2():
    baidu_spider2.BaiduSpider(thread_count=100, redis_key="baidu_spider").start()


if __name__ == "__main__":

    parser = ArgumentParser(description="测试")

    parser.add_argument(
        "--baidu_spider", action="store_true", help="", function=baidu_spider
    )
    parser.add_argument(
        "--baidu_spider2", action="store_true", help="", function=baidu_spider2
    )

    parser.start()
