#!/usr/bin/python

import sqlite3
import sys

conn = sqlite3.connect('cantonese.db')
#conn = sqlite3.connect('cantonhk.db')
c = conn.cursor()

#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(c.fetchall())

#[(u'ime',), (u'goucima',), (u'pinyin',), (u'phrases',)]

## configure
#c.execute("SELECT * FROM ime ;")
#print(c.fetchall())

## empty
#c.execute("SELECT * FROM goucima ;")
#print(c.fetchall())

## empty
#c.execute("SELECT * FROM pinyin ;")
#print(c.fetchall())

#c.execute("SELECT * FROM phrases ;")
#print(c.fetchall())

#['id', 'tabkeys', 'phrase', 'freq', 'user_freq']      'tabkeys' => 'phrase'
#names = list(map(lambda x: x[0], c.description))
#print names


def lookup(cur, ch):
        cur.execute("SELECT tabkeys FROM phrases WHERE phrase = \"" + ch + "\" ;")
	rows = cur.fetchall()
	result = ""
	for row in [x[0] for x in rows]:
		if len(result) > 0:
			result += "/"
		result += row
	return result



if len(sys.argv) > 1:
	input = sys.argv[1]
	result = ""
	for word in unicode(input, "utf-8"):
		typing = lookup(c, word)
		if len(typing) == 0:
			typing = "?"
		result += typing + " "
	print result

#if len(sys.argv) > 1:
#	phrase = sys.argv[1]
#	c.execute("SELECT tabkeys FROM phrases WHERE phrase = \"" + phrase + "\" ;")
#	c.execute("SELECT tabkeys FROM phrases WHERE id = 12018 ;")
#	result = c.fetchall()
#	print result[0][0]

conn.close()
