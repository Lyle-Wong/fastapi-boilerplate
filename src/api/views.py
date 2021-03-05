#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-03-06 00:07:59
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/liveiness")
def liveiness():
    return JSONResponse({'result':'sucess', 'status':'UP', 'message':'server running'})