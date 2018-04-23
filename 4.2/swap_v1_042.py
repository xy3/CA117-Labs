def swap_keys_values(dic):
	keys = list(dic.keys())
	vals = list(dic.values())

	newdic = {}

	i = 0
	for val in vals:
		newdic[val] = keys[i]
		i += 1

	return newdic

def main():
	d = {'a' : 4, 'b' : 7, 'c' : 10}
	new = swap_keys_values(d)
	print(new.items())

if __name__ == '__main__':
	main()