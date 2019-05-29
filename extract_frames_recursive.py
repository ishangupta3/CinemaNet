import os
import sys
import subprocess
from subprocess import Popen
from multiprocessing import Pool

p = Pool(8)
input_dir = sys.argv[1]
output_dir = sys.argv[2]
extension = sys.argv[3]

def processFile(filename):
	if filename.endswith(extension):
		current_file = os.path.join(root, filename)
		destination = os.path.join(output_dir, filename)
		destination = os.path.splitext(destination)[0]+'_%04d.jpg'

		print('processing :' + current_file)
		print('to ' + destination)
		return subprocess.Popen(["ffmpeg", "-i", str(current_file),  "-vf", "fps=1/3", "-q:v 2" str(destination), "-hide_banner"]).wait()

print('scanning ' + input_dir + ' for files with extension ' + extension)
print('outputing to ' + output_dir)

for root, subdirs, files in os.walk(input_dir):
	files = [f for f in files if not f[0] == '.']
	subdirs[:] = [d for d in subdirs if not d[0] == '.']

	for filename in files:
		processFile(filename)