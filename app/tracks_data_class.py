#!/usr/bin/env python3
"""
created: 2022-07-08 15:58:40
@author: seraph★1001100
contact: admin@codecrypt76.com
project: MP3 Playlist CLass Project
metadoc: Track class
license: None
"""


from dataclasses import dataclass


@dataclass
class Track:
    title: str
    artist: str
    duration: str      
