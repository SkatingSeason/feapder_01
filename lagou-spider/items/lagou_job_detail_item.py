# -*- coding: utf-8 -*-
"""
Created on 2021-03-19 22:16:25
---------
@summary:
---------
@author: liubo
"""

from feapder import Item


class LagouJobDetailItem(Item):
    """
    This class was generated by feapder.
    command: feapder create -i lagou_job_detail.
    """

    def __init__(self, *args, **kwargs):
        # self.id = None
        self.title = None  # 职位名称
        self.detail = None  # 职位详情
        self.batch_date = None  # 批次信息
