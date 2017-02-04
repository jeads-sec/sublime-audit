import sublime
import sublime_plugin
import mdpopups
import time
import os
import json

class ListAnnotationTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		folders = sublime.active_window().folders()
		if len(folders) == 1:
			proj_folder = folders[0]
			file_name = "annotations.json"
			self.annotations_file = os.path.join(proj_folder, file_name)
			if os.path.exists(self.annotations_file):
				f = open(self.annotations_file, "r")
				self.annotations = json.loads(f.read())
				f.close()
			else:
				self.annotations = {}
				self.annotations['by_file'] = {}
				self.annotations['by_tag'] = {}

		for t in self.annotations['by_tag']:
			if len(self.annotations['by_tag'][t]) > 0:
				print(t)
