#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

class Timer:
	def __init__(self, delta):
		self._delta = delta
		self.beginTimer()

	def beginTimer(self):
		self._alertTime = datetime.today() + self._delta

	def check(self):
		now = datetime.today()
		if now > self._alertTime:
			self._alertTime = now + self._delta
			return True

		return False