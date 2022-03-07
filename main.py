import sys
from IPL import IPL


def main():
	ipl = IPL(sys.argv[1:])
	ipl.doStuff()

if __name__ == '__main__':
	main()
