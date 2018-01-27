import io

def test_string(input_file):
	f = io.open(input_file, 'r', encoding = 'utf-8')
	lines = f.readlines()

	#the file should contain a single line only
	assert(len(lines) == 1)
	
	f.seek(0)
	text = f.read().strip()

	#the first line should contain only 6 unicode characters
	assert(len(text) == 6)
