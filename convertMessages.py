# readd the file
def readFile(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		#print(person,': ', line)
		if person:
			new.append(person + ': ' + line)
	return new

def writeFile(filename, lines):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = readFile('input.txt')
	lines = convert(lines)
	writeFile('output.txt', lines)

main()