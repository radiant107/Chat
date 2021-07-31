
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding = 'utf-8-sig') as record:
		for line in record:
			chat.append(line.strip())
	return chat

def transform_file(chat):
	chat1 = []
	person = None
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			chat1.append(person + '： ' + line)
	return chat1

def print_file(chat):
	for c in chat:
		print(c)

def write_file(filename2, chat):
	with open(filename2, 'w', encoding = 'utf-8-sig') as r:
		for line in chat:
			r.write(line + '\n')

def main():
	chat = read_file('input.txt')
	chat1 = transform_file(chat)
	print_file(chat1)
	write_file('output.txt', chat1)

main()
