#!/usr/bin/python
# -*- coding: utf-8 -*-
__metaclass__ = type 

class Person():
    
    def __init__(self, name, song):
        self.name = name
        self.song = song
    
    def getName(self):
        return self.name
        
    def greet(self):
        print "Hello, This is %s, %s is my beloved song. " % (self.name, self.song)

John = Person('Lennon', 'Imagine')
Paul = Person('Mcartney', 'Hey Jude')
Gergoe = Person('Harrison', 'Something')
Ringo = Person('Starr', 'Yellow Submarine')

John.greet()
Paul.greet()
Gergoe.greet()
Ringo.greet()

#继承
#class Beatles(Person):
#    pass
#    
#Peta = Beatles('Best', 'Drop the mic')
#Peta.greet()


