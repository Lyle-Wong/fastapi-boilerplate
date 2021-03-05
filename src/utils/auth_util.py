#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-02-24 18:42:24
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os

from sqlalchemy.engine.base import Connection
from sqlalchemy.orm.session import Session
from loguru import logger
from functools import wraps
from fastapi.encoders import jsonable_encoder
from fastapi import Request, HTTPException, Depends
from sqlalchemy.engine.result import ResultProxy, RowProxy
from src.config import SKIP_AUTHENTICATION
from src.core import db

def __perform_sql_interaction(query, conn=None) -> ResultProxy:
        if not conn:
            conn: Session = next(db.get_db())
        try:
            # cursor = conn.cursor()
            rs = conn.execute(query)
        except Exception as err:
            logger.exception(err)
            raise err
        return rs, rs.keys()

def login_required(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(request: Request, *args, **kwargs):
        if SKIP_AUTHENTICATION:
            return function_to_protect(request, *args, **kwargs)
        auth_header = request.headers.get('Authorization')
        if auth_header:
            """get the user from the database"""
            session_id = auth_header.split()[-1]
            q = "Select * from T_JP_InsUser WITH (NOLOCK) where session_id= '%s'" % session_id
            rs, keys = __perform_sql_interaction(q)
            if rs.rowcount:
                rec: RowProxy = rs.first()
                request.state.user = rec.uid
                request.state.userid = rec.id
                return function_to_protect(request, *args, **kwargs)
            #"""pass the error unauthorized, please login first"""
            return HTTPException(status_code=401,detail=jsonable_encoder({"message":"error","messageList":[{"error":"bad token"}],"auth_header": auth_header}))
        else:
            #"""pass the error unauthorized, please login first"""
            return HTTPException(status_code=401, detail=jsonable_encoder({"message":"error","messageList":[{"error":"User Unauthorized"}]}))
    return wrapper