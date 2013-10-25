#!/bin/bash
echo "<insetando sql de la base de datos>"
python2.7 manage.py syncdb
echo "indroduce el usuario de la base de datos"
read user
echo "introduce la base de datos"
read base
mysql -u $user -p -B $base < $HOME/archivo.sql
