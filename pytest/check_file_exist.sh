#!/bin/bash

#check file exists or not and check the statenments
#version 1.0

function usage(){
echo "Usage:$0 file_name time_hour
      file_name is just name not contain time
      tiem_hour is the number of hour"
}

function check(){
  if [ $current_time -lt $time ];then
         echo "OK,now is not the check time yet"
         exit 0;
  fi
  if [ $filenum -ge 1 ];then
        echo "OK,file exist"
        exit 0;
  else
        echo "WARNING,file is not exist,please check"
        exit 1;
  fi
}

function main(){
  
  if [ $# -ne 2 ];then
        usage
	exit 2;
  fi
  time=$2
  dir=$(cd $(dirname $1);pwd)
  current_time=$(date +%H)
  y_day=$(date -d"yesterday" +%Y%m%d)
  filename=$(basename $1)-$y_day
  filenum=`find $dir -iname "$filename*" -mtime -1|wc -l`
  check
}

main $@
