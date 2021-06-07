import sys

def argCheck():
    if len(sys.argv) == 2 and sys.argv[1][-4:] == '.txt':
        pass #check OK
    else:
        print('Invalid arguments')
        sys.exit(1)
    
    return sys.argv[1]


def rmTags(fn):
    newtext = ''

    with open(fn,'r') as f:
        text = f.read().split('\n')

        for line in text:
            #remove comment
            if '#' in line:
                line = line.split('#')[0]

            #remove tabs
            if '\t' in line:
                newtext += line.split('\t')[0]
            else:
                newtext += line
    
            #add space at end of line
            if line != '':
                newtext += ' '
    return newtext


def toBin(text, outputFile):
    binList = bytes([int(i, 16) for i in text.split()])

    with open(outputFile,'wb') as f:
        f.write(binList)

    print('Create ' + outputFile)


fn = argCheck()

text = rmTags(fn)

outputFile = fn.split('.')[0] + '.bin'
toBin(text, outputFile)
