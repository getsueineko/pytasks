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
    result = []
    for f in file_list:
        #print "Attemp to read Idv3 tags from: %s" % f
        mfile = open(f, "rb")
        mfile.seek(TAG)
        name = mfile.read(NAME)
        mfile.seek(TAG + NAME)
        artist = mfile.read(ARTIST)
        mfile.seek(TAG + NAME + ARTIST)
        album = mfile.read(ALBUM)
        mfile.seek(TAG + NAME + ARTIST + ALBUM)
        year = mfile.read(YEAR)
        result.append({
            "Name": name,
            "Artist": artist,
            "Album": album,
            "Year": year
        })
    return result


def csv_maker(fullpath, mp3_list, fieldnames):
    with open(fullpath, 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        #Name;Artist;Album....
        for item in mp3_list:
            writer.writerow(item)




def validate(path):
    if not path.endswith("/"):
        path = path + "/"
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Idv3 tags')
    parser.add_argument('-f', '--folder', dest='folder', type=str, required=True, help='Folder to scan')
    parser.add_argument('-o', '--output', dest='out_folder', type=str, required=False, help='Folder to result')
    args = parser.parse_args()

    #List of filtred mp3's
    filelist = list_mp3(args.folder)

    #Read files
    result = mp3info(filelist)
    print "Files found: %d" % len(result)

    #Validate path
    path = validate(args.out_folder)
    filename = path + "123.csv"
    print "Output: " + filename

    #Fieldnames
    fieldnames = ["Artist", "Name", "Album", "Year"]

    #Run
    data = csv_maker(filename, result, fieldnames)




