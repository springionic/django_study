#!/usr/bin/env python
# -*- coding:utf-8 -*-+
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tulingxueyuan_views.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
