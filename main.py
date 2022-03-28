import sys
from v20 import League


def main():
	league = League(sys.argv[1:])
	league.doStuff()

if __name__ == '__main__':
	main()
