#Modules#
import os
import warnings
import webbrowser

#Locate the file#
home =  os.environ['HOME']

infile_path = os.path.join(home, 'lulu_mix_16.csv')

f1 = open(infile_path, 'r')

#Iteration on the file#
line = iter(f1)

next(line)

for line in f1:
        parsed = (*line.strip('\r\n').split(','))
        songs = []
        songs.append(Song(parsed))

for s in songs:
	print s.artist
for s in songs:
	print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play()

#Class#
class Song(object):
	def __init__(self, title, artist, duration):
		self.title = title
		self.artist = artist
		self.duration = duration

		if type(duration) == int:
			pass
		else:
			warnings.warn('The duration of %s is not a number. It will be set to 0' % self.title)
			duration = 0
		if duration < 0:
			raise Exception('The duration of %s is negative. The program will stop' % self.title)				

	def pretty_duration(self):
		secs = self.duration
		mins = secs / 60
		hours = mins / 60
		sec_rest = secs % 60
		min_rest = mins % 60
		return '%02i hours %02i minutes %02i seconds" % (hours, min_rest, sec_rest)			
	def play(self):
		base_url ="https://www.youtube.com/results?search_query="
		complete_url = base_url + self.title.replace(' ', '+')
		webbrowser.open(complete_url)

