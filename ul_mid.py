#!/bin/python

taglist_directory = "/usr/share/tag/"

import os
import sys

if len (sys.argv) != 2:
	print ('usage: ' + sys.argv[0] + ' TAGFILE')
	sys.exit(1)

categories = list(os.walk(taglist_directory))[0][2]

def category_file (cat):
	return taglist_directory+cat

category_id = dict()

for i, cat in enumerate(categories):
	category_id[cat] = i

def category_string (cat):
	return '{Id:'+str(category_id[cat])+',Names:[{LanguageId:0,Name:'+cat+'}]}'

tags = list()

for cat in categories:
	tags += [(cat, tag.replace('\n','')) for tag in open(category_file(cat), 'r')]

tag_id = dict()

for i, (_, tag) in enumerate (tags):
	tag_id[tag] = i

def tag_string (cat, tag):
	return '{Id:' + str(tag_id[tag]) + ',CategoryId:' + str(category_id[cat]) + ',Names:[{LanguageId:0,Name:' + tag + '}]}'

filename = sys.argv[1]
titles_filename = filename + '_titles'

f = open(filename, 'r')

artist,album = next(f).replace('\n', '').split(',')

titles = [ title.replace('\n', '') for title in open(titles_filename) ]

title_id = dict()
for i, title in enumerate(titles):
	title_id[title] = i

def title_string (title):
	return '{Id:' + '0' + ',Artist:' + artist + ',Album:' + album + ',Title:"' + title + '"}'
#
#print (','.join(map(title_string, titles)))
#
title_to_tag_id = dict()
for line in f:
	i, tags = line.replace('\n', '').split(': ')
	if tags == '':
#		continue
		title_to_tag_id[titles[int(i)-1]] = []
	else:
		title_to_tag_id[titles[int(i)-1]] = [tag_id[tag] for tag in tags.split(',')]
#
#print ('],TagsForFiles:[')
#
#print (','.join ('{FileId:' + str(title_id[title]) + ',TagIds:[' + ','.join(map (str, title_to_tag_id[title])) + ']}' for title in titles if not title_to_tag_id.keys().isdisjoint([title])))
#
#print (']')
#
for title in titles:
	#if title_to_tag_id.keys().isdisjoint([title]): continue

	print (',Files:[' + title_string ( title ) + ']' + ',TagsForFiles:[{FileID:' + '0' + ',TagIds:[' + ','.join ( map ( str , title_to_tag_id [ title ] ) ) + ']}]' )

