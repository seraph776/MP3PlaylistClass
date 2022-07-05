#!/usr/bin/env python3
"""
created: 2022-07-05 12:34:30
@author: seraph776
contact: admin@codecrypt76.com
project: MP3 Playlist Class
license: None
"""


class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title}, artist={self.artist}, duration={self.duration} seconds)'
