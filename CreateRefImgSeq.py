#!/usr/bin/env python

import os
import sys
import commands
import optparse

parser = optparse.OptionParser("usage: %prog [options] arg1")
parser.add_option("-d", "--dryrun", action="store_true", dest="dry",  help="Dry run. Which commands will be run.")
(options, files) = parser.parse_args()

flist = commands.getoutput("ls").split('\n')[1:]

src_link = [(   '\ '.join(line.split()[8:])  ,  '_'.join(line.split()[8:])  )  for line in flist]

counter = 0

if options.dry:
    print 'Creating Path: ' + files[0] + '/symlink'
    
    for line in src_link:
        counter = counter + 1
    
        frame = str(counter)
    
        if counter < 10:
            print '/bin/ln -s ' + files[0] + '/' + line[0] + ' ' + files[0] + '/symlink/' + files[1] + '.000' + frame + '.jpg'
        elif counter < 100:
            print '/bin/ln -s ' + files[0] + '/' + line[0] + ' ' + files[0] + '/symlink/' + files[1] + '.00' + frame + '.jpg'
        elif counter < 1000:
            print '/bin/ln -s ' + files[0] + '/' + line[0] + ' ' + files[0] + '/symlink/' + files[1] + '.0' + frame + '.jpg'
        elif counter < 10000:
            print '/bin/ln -s ' + files[0] + '/' + line[0] + ' ' + files[0] + '/symlink/' + files[1] + '.' + frame + '.jpg'
else:
    commands.getoutput('/bin/mkdir -v ' + files[0] + '/symlink')
    
    for line in src_link:    
        counter = counter + 1
    
        frame = str(counter)
    
        if counter < 10:
            commands.getoutput('/bin/ln -s ' + files[0] + '/' + line[0] + ' ' + files[0] + '/symlink/' + files[1] + '.000' + frame + '.jpg')
        elif counter < 100:
            commands.getoutput('/bin/ln -s ' + files[0] + '/' + line[0] + ' ' + files[0] + '/symlink/' + files[1] + '.00' + frame + '.jpg')
        elif counter < 1000:
            commands.getoutput('/bin/ln -s ' + files[0] + '/' + line[0] + ' ' + files[0] + '/symlink/' + files[1] + '.0' + frame + '.jpg')
        elif counter < 10000:
            commands.getoutput('/bin/ln -s ' + files[0] + '/' + line[0] + ' ' + files[0] + '/symlink/' + files[1] + '.' + frame + '.jpg')
