#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

class Timer:
	def __init__(self, delta):
		self._begin = datetime.today()
		self._delta = delta
		self._alertTime = self._begin + self._delta

	def check(self):
		now = datetime.today()
		# print("now: {0} alert_time: {3}\n".format(now, self._alertTime))
		if now > self._alertTime:
			self._alertTime = now + self._delta
			return True

		return False