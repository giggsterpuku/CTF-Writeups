import gdb
import string

valid_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "}_"
cmp_brkpt = '*0x5655598e'
flag = 'picoCTF{'
current_flag_len = 8

gdb.execute(f'b {cmp_brkpt}')
while current_flag_len < 30: # predicted length of flag
	for c in valid_chars:
		test_str = flag + c
		f = open('test.txt', 'w')
		f.write(flag + c)
		f.close()
		gdb.execute('r < test.txt')
		for i in range(current_flag_len):
			gdb.execute('c')
		dl = gdb.parse_and_eval('$dl')
		al = gdb.parse_and_eval('$al')
		if dl == al:
			flag += c
			current_flag_len += 1
			break
		if c == '_':
			flag += c
	print(flag)
print(flag)
