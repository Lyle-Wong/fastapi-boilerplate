#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-03-04 10:46:45
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os
from pathlib import Path
import tempfile

home_path: Path = Path(__file__).parent.parent.parent

tmp_path = tempfile.gettempdir()