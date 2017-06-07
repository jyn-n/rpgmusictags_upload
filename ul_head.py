#!/bin/python

import os
import sys

taglist_directory = "/usr/share/tag/"

if len(sys.argv) <= 1 or sys.argv[1] != 'notest':
	print('Test=True&')

print ('IncludeLog=True\
&User=knups\
&TagsData={\
Languages:[{ISO6391Code:de,Id:0}]\
,Categories:[')


categories = list(os.walk(taglist_directory))[0][2]

def category_file (cat):
	return taglist_directory+cat

category_id = dict()

for i, cat in enumerate(categories):
	category_id[cat] = i

def category_string (cat):
	return '{Id:'+str(category_id[cat])+',Names:[{LanguageId:0,Name:'+cat+'}]}'

print (','.join(map(category_string, categories)))

print('],Tags:[')

tags = list()

for cat in categories:
	tags += [(cat, tag.replace('\n','')) for tag in open(category_file(cat), 'r')]

tag_id = dict()

for i, (_, tag) in enumerate (tags):
	tag_id[tag] = i

def tag_string (cat, tag):
	return '{Id:' + str(tag_id[tag]) + ',CategoryId:' + str(category_id[cat]) + ',Names:[{LanguageId:0,Name:' + tag + '}]}'

print (','.join((tag_string(cat, tag) for cat, tag in tags)))

print (']')

