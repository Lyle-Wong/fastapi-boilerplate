#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-03-04 10:38:32
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os
from typing import Dict, List

from loguru import logger
from sqlalchemy.orm.session import Session
from src.core import db
from sqlalchemy.engine.result import ResultProxy, RowProxy

import socket

from src.scheduler import job_manager
from apscheduler.jobstores.base import ConflictingIdError


class CustomizedJob():
    def job_a(self):
        logger.info('running job')


def job():
    CustomizedJob().job_a()

def add_a_job():
    try:
        job_manager.add_job('job_a', job, (), 20)
    except ConflictingIdError as e:
        logger.warning('job with id job_a aleady exist')
        job_manager.get_jobs()