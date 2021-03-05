#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-03-04 11:47:17
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os
from src.scheduler import CustomizedScheduler
from loguru import logger

scheduler = CKCScheduler().get_scheduler()

def add_job(job_id, func, args, minutes):
    scheduler.add_job(id=job_id, func=func, args=args, trigger='interval', minutes=minutes)

def remove_job(job_id):
    scheduler.remove_job(job_id)
    logger.info(f"remove job - {job_id}")

def pause_job(job_id):
    scheduler.pause_job(job_id)
    logger.info(f"pause job - {job_id}")

def resume_job(job_id):
    scheduler.resume_job(job_id)
    logger.info(f"resume job - {job_id}")

def get_jobs():
    res = scheduler.get_jobs()
    logger.info(f"all jobs - {res}")

def print_jobs():
    scheduler.print_jobs()

def shutdown():
    scheduler.shutdown()