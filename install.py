#!/usr/bin/env python
#
# Appcelerator Titanium Module Installer
#
#
import os, sys, subprocess

ti = "/Library/Application Support/Titanium/mobilesdk/osx/2.0.1/titanium.py"

def run(args, cwd=None):
	proc = run_pipe(args, cwd)
	rc = None
	while True:
		print_emulator_line(proc.stdout.readline())
		rc = proc.poll()
		if rc!=None: break
	return rc

def run_pipe(args, cwd=None):
	return subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, cwd=cwd)

def print_emulator_line(line):
	if line:
		s = line.strip()
		if s!='':
			if s.startswith("["):
				print s
			else:		
				print "[DEBUG] %s" % s
			sys.stdout.flush()

directories = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
for directory in directories:
	iosDir = "%s/mobile/ios/" % directory
	if os.path.isdir(iosDir):
		rc = run([sys.executable, ti, "install"], iosDir)
		if rc != 0:
			print "[ERROR] %s install failed." % iosDir