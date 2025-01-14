#!/bin/bash
#
# script to initially copy files to user directory ~/PhyPi/
#

# -----------------------------------------

if [ "$1" != "" ]; then
    USERDIR=$1
else
    USERDIR="PhyPi"
fi

# -----------------------------------------

DIR=$HOME/$USERDIR
echo "copying files to "$DIR

mkdir -p $DIR

if [ -d $DIR ]; then
# enter here, if directory exists

  # create desktop icon
  cp -auv *.desktop $HOME/Desktop
  chmod a+x $HOME/Desktop/*.desktop

  # copy documentation
  # mkdir -p $DIR/doc
  # cp -auv doc/*.pdf $DIR/doc/
  # cp -auv README_de.pdf $DIR

  #copy python code
  cp -auv phypi.py $DIR
  cp -auv run_phypi.py $DIR

  #copy config examples
  cp -auv config/ $DIR
  cp -auv *.daq $DIR

  # copy examples
  cp -auv examples/ $DIR
fi

echo "The full documentation (software, hardware and educational guidelines) can be found on GitHub:"
echo "https://github.com/PhyPiDAQ"
