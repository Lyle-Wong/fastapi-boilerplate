#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-03-03 12:55:43
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.core import db

router = APIRouter()


@router.get('/')
async def index(request: Request):
    return {"message": "it works"}

