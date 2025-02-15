import os

def run(**args):
	print("[*] No modulo dirlister.")
	files = os.listdir(".")
	return str(files)
