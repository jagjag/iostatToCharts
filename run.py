#!/usr/bin/env python
# -*- coding: utf-8 -*-
from iostat2charts.makecharts import MakeCharts


def main():
    import sys
    if sys.argv[1:]:
        file = sys.argv[1]
        import os
        if os.path.isfile(file):
            MakeCharts(datafile=file).draw()
        else:
            print("No such file .")
    else:
        print("no file arg exit.")

if __name__ == '__main__':
    main()
