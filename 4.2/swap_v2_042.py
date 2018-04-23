def swap_unique_keys_values(dic):
	keys = list(dic.keys())
	vals = list(dic.values())

	newdic = {}

	i = 0
	for val in vals:
		if vals.count(val) == 1:
			newdic[val] = keys[i]
		i += 1

	return newdic

def main():
	d = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
	new = swap_unique_keys_values(d)
	print(new.items())

if __name__ == '__main__':
	main()