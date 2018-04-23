import sys

def letters17(wlist):
	return [word for word in wlist if len(word) == 17]

def letters18(wlist):
	return [word for word in wlist if len(word) > 17]

def smallVowels(wlist):
	return min([word for word in wlist if havevowels(word.lower())], key=len)

def havevowels(word):
	return all(x in word for x in ['a','e','i','o','u'])

def fourAs(wlist):
	return [word for word in wlist if word.lower().count("a") == 4]

def moreQs(wlist):
	return [word for word in wlist if word.lower().count("q") > 1]

def cie(wlist):
	return [word for word in wlist if "cie" in word.lower()]

def anaAngle(wlist):
	return [word for word in wlist if isAna(word.lower()) and word != "angle"]

def isAna(word):
	return sorted(list(word)) == sorted(list("angle"))

def endiary(wlist):
	return len([word for word in wlist if word.lower().endswith("iary")])

def qButNotU(wlist):
	return [word for word in wlist if quEstion(word.lower())]

def quEstion(word):
	return 'q' in word and 'qu' not in word

def mostEs(wlist):
	mn = max([word for word in wlist if 'e' in word.lower()], key=countE)
	mn = mn.count('e')
	return [word for word in wlist if word.lower().count('e') == mn]

def countE(word):
	return word.count('e')

def main():
	wordlist = [word.rstrip() for word in sys.stdin]
	print("Words containing 17 letters: {}".format(letters17(wordlist)))
	print("Words containing 18+ letters: {}".format(letters18(wordlist)))
	print("Shortest word containing all vowels: {}".format(smallVowels(wordlist)))
	print("Words with 4 a's: {}".format(fourAs(wordlist)))
	print("Words with 2+ q's: {}".format(moreQs(wordlist)))
	print("Words containing cie: {}".format(cie(wordlist)))
	print("Anagrams of angle: {}".format(anaAngle(wordlist)))
	print("Words ending in iary: {}".format(endiary(wordlist)))
	print("Words with q but no u: {}".format(qButNotU(wordlist)))
	print("Words with most e's: {}".format(mostEs(wordlist)))

if __name__ == '__main__':
	main()