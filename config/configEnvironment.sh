#!/bin/bash

# Prepare the folder where we will compile SQLite3. In this case, we will choose a temporary location 
echo "Creating folder compilation folder..."
COMPILEPATH="/tmp/compile"
mkdir $COMPILEPATH
echo "Moving to $COMPILEPATH ..."
cd $COMPILEPATH

# Download lnd extract latest version of SQLite3 from official site
echo "Downloading SQLite3..."
wget "www.sqlite.org/2018/sqlite-autoconf-3220000.tar.gz"

tar -xvzf "./sqlite-autoconf-3220000.tar.gz"
cd sqlite-autoconf-3220000

echo "Configuring compilation..."
mkdir ${HOME}/SQLite
echo $(pwd)
./configure --prefix=${HOME}/SQLite/sqlite3 --disable-static --enable-fts5 --enable-json1 CFLAGS="-g -O2 -DSQLITE_ENABLE_FTS3=1 -DSQLITE_ENABLE_FTS4=1 -DSQLITE_ENABLE_RTREE=1"


make
make install
echo "RESULT: #############################################################################################"
echo "DONE!!"
echo "SQLite3 was installed at ${HOME}/SQLite. Run ${HOME}/SQLite/sqlite3 <path-of-db-file>"

