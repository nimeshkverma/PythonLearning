class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line*10

happy_bday = Song(["fjjlnvsjfdjvsf","sdi ","euihwduaeifsaew"])
bull = Song(["qqqqqqqqq","qwqwqwwwq","wqqd	wdwe","edwedqw"])

happy_bday.sing_me_a_song()
bull.sing_me_a_song()

# h = Song(1)
# b = Song(1.1)
# c = Song("qqqqq")
# h.sing_me_a_song()
# b.sing_me_a_song()
# c.sing_me_a_song()