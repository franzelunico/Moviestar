#!/bin/bash
echo "<extraendo sql de la base de datos>"
echo "indroduce el usuario de la base de datos"
read user
echo "introduce la base de datos"
read base
mysqldump -u $user -p -B $base >$HOME/archivo.sql
