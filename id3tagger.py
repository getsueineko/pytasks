#!/usr/bin/python
# -*- coding: utf-8 -*-


import argparse
import os
import csv


#=============DEFINES==========
TAG = 3
NAME = 30
ARTIST = 30
ALBUM = 30
YEAR = 4

def list_mp3(mp3_folder):
    print "Reading folder: %s" % mp3_folder
    result = []
    files = os.listdir(mp3_folder)
    for f in files:
        if f.endswith(".mp3"):
            fullpath = mp3_folder + f
            result.append(fullpath)
    print "Found %d mp3 files in folder: %s" % (len(result), mp3_folder)
    return result


def mp3info(file_list):
    for f in file_list:
        print "Attemp to read Idv3 tags from: %s" % f
        mfile = open(f, "rb")
        mfile.seek(TAG)
        name = mfile.read(NAME)
        mfile.seek(TAG + NAME)
        artist = mfile.read(ARTIST)
        mfile.seek(TAG + NAME + ARTIST)
        album = mfile.read(ALBUM)
        mfile.seek(TAG + NAME + ARTIST + ALBUM)
        year = mfile.read(YEAR)
        print "Full name of track: %s" % artist + name + album + year  

#def output_list():
#    RESULT = ['artist','name','album','year']
#    resultFile = open("playlist.csv",'wb')
#    wr = csv.writer(resultFile, dialect='excel')
#    wr.writerow(RESULT)
#    output_file.close()

#Function in which I have to set name of directory
#def output_dir():
#    newDirName =
#if os.path.exists(path):
#   то сюда, наверное вызов заданного ключом пути
#else:   
#    os.mkdir(newDirName)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Idv3 tags')
    parser.add_argument('-f', '--folder', dest='folder', type=str, required=True, help='Folder to scan')
    parser.add_argument('-o', '--output', dest='folder', type=str, required=False, help='Folder to result')
    args = parser.parse_args()

    #List of filtred mp3's
    filelist = list_mp3(args.folder)

    #Read files
    result = mp3info(filelist)


# Добавить в командную строку аргумент "output", это будет путь к файл в который пишется результат в CSV




