#!/usr/bin/env python
# -*- coding: utf-8 -*-
from iostat2charts.makecharts import MakeCharts


def main():
    MakeCharts(datafile=r'/home/gcpadmin/iostat/data/iostat.data.20151227').draw()


if __name__ == '__main__':
    main()
