#!/bin/bash

#
#
#  version 1.0  
#
#  Jiang Jiang




bk_base=/home/gcpadmin/iostat/data

cp -r ${bk_base}/iostat.data  ${bk_base}/iostat.data.`date +%Y%m%d%H` 

>${bk_base}/iostat.data
