#Modules#
import os
import sys
import re

#Locate the file#
home =  os.environ['HOME']

infile_path = os.path.join(home, 'lulu_mix_16.csv')

f1 = open(infile_path, 'r')

#Iteration on the file#
line = iter(f1)

next(line)

for line in f1:
        parsed = line.strip('\r\n').split(',')
        songs = []
        songs.append(Song)

#Class#
class Song(object):
	def __init__(self, title, artist, duration):
		self.title = title
		self.artist = artist
		self.duration = duration
		self.track = {}

	def addSong(self):
		self.track += {self}

#	def pretty_duration(self):
		

#	def play(self):
		
