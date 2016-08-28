#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
def convert(value):
    if value.startwith('-'):
        return value.strip('-')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE food (
    id     TEXT     PRIMARY KEY，
    desc   TEXT,
    water  FLOAT,
)
''')

query = 'INSERT INTO food VALUES (?, ?)'

for line in open ('FOOD_DES.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()
