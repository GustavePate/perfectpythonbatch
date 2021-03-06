# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pps.demos.demo_tempfiles as demo_tempfiles
import pytest


@pytest.mark.usefixtures("initloggers")
def test_module():
    try:
        res = demo_tempfiles.demo("blabla")
        print(res)
        assert res == "blabla"
    except Exception:
        assert False
