import time
import math
import string


chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

charLength = 26

def getPossibleCount(length):
	return int(math.pow(charLength,length))


def generateAll(length, debug):

	count = 0
	for i in range(0,getPossibleCount(length)):
		theword = ""
		val = i

		for j in range(0, length):
			count += 1
			ch = int(val % charLength)
			theword += chars[ch]

			val = val / len(chars)
		if(debug == True):
			print(theword)


def main():

	iterCts = [1,2,3,4,5,6,7,8,9,10,15,20,25,30,35]

	timelist = []

	for ct in iterCts:
		print("On iteration {}".format(ct))
		starttime = time.time()

		generateAll(ct, False)

		endtime = time.time()

		runtime = endtime - starttime



		timelist.append(runtime)
		print(ct, runtime)


	for i in range(0, len(iterCts)):
		print(iterCts[i], timelist[i])


if __name__ == '__main__':
	main()
