import sys

 def returnLargerthan5(wl):
	return [w for w in wl if len(w) > 4]

def reverseCheck(w5):
	wLower = [word.lower() for word in w5]
	return [word for word in w5 if binarySearch(wLower, word[::-1].lower())]

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def main():
	wl = [word.rstrip() for word in sys.stdin]
	w5 = returnLargerthan5(wl)
	print(reverseCheck(w5))

if __name__ == '__main__':
	main()