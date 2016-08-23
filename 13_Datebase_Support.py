#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
def convert(value):
    if value.startwith('-'):
        return value.strip('-')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('foo.db')
curs = conn.cursor()

curs.exexute('''
CREATE TABLE food(
    id     TEXT     PRIMARY KEY，
    desc   TEXT
    water  FLOAT
)
‘’‘’)

query = 'INSERT INTO food VALUES (?,?,?)'

for line in open ('A')
