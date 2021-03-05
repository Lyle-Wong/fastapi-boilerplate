#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-03-04 11:37:56
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import atexit
import os
import platform

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.base import BaseScheduler
from loguru import logger
from pytz import utc
from src.utils import tmp_path
from src.core import singleton

@singleton
class CustomizedScheduler:
    scheduler = None

    @classmethod
    def get_scheduler(cls):
        if cls.scheduler:
            return cls.scheduler
        jobstores = {
            'default': SQLAlchemyJobStore(url=f'sqlite:///{tmp_path}/jobs.sqlite')
            }
        executors = {
            'default': ThreadPoolExecutor(max_workers=2)
            }
        job_defaults = {
            'coalesce': True,
            'max_instances': 1
            }
        logger.info('job.sqlite path:' + tmp_path)
        cls.scheduler = AsyncIOScheduler()
        cls.scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
        cls.__scheduler_init(scheduler=cls.scheduler)
        return cls.scheduler

    @classmethod
    def __scheduler_init(cls, scheduler: BaseScheduler):
        """
        make sure only one scheduled job will be run
        :param app:
        :return:
        """
        if platform.system() != 'Windows':
            fcntl = __import__("fcntl")
            f = open('scheduler.lock', 'wb')
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                scheduler.start()
                logger.info('Scheduler Started,---------------')
            except:
                pass

            def unlock():
                fcntl.flock(f, fcntl.LOCK_UN)
                f.close()

            atexit.register(unlock)
        else:
            msvcrt = __import__('msvcrt')
            f = open('scheduler.lock', 'wb')
            try:
                msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
                scheduler.start()
                logger.info('Scheduler Started,----------------')
            except:
                pass
            def _unlock_file():
                try:
                    f.seek(0)
                    msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
                except:
                    pass
            atexit.register(_unlock_file)
