import os
while True:
    filename = raw_input("input you file: ")
    if os.path.exists(filename):
    	fp = open(filename, 'r')
    	lines = []
    	for line in fp.readlines():
            lines.append(line.rstrip())
    	os.remove(filename)
    	fp.close()
    	with open(filename, 'a') as f:
            for l in lines:
    	       f.write(l + '\n')
        print 'Done'
    else:
        if filename == 'no':
	    break
        print 'file not exist'
	continue


