#!/usr/bin/python
# -*- coding: utf-8 -*-

#datebase.py
import sys.shelve

# 储存
def store_person(db)
    pid = raw_input('Enter unique ID number: ')
    person = {}
    person['name'] = raw_input(‘Enter name: ')
    person['age'] = raw_input('Enter_age')
    person['phone'] = raw_input('Enter phone number: ')

    dp[pid] = person
# 读取
def lookup_person(db):
    pid = raw_input(’Enter ID number')
    field = raw_input('What would you like to know? (name, age , phone) ')
    field = field.strip().lower()
    # 格式化
    print field.capitalize()+':',\
        dp[pid][field]

def print_help():
    print 'The available commands are: '
    print 'store   : store information about a person '
    print 'lookup  : looks up a person from ID number '
    print 'quit    : save change and exit '
    print '?       : print this message '

def enter_command():
    cmd = raw_input('Enter command(? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    datebase = shelve.open('C:\\datebase.dat') #how can I find the right location
    try:
        while Ture:
            cmd = enter_command()
            if cmd == 'store'
                store_person(datebase)
            elif cmd == 'lookup':
                lookup_person(datebase)
            elif cmd == '?'
                print_help()
            elif cmd == 'quit'
                return

    finally:
    datebase.close()

if __name__ == '__main__':main()
 
