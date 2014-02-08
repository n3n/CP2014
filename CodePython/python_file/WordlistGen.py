import itertools, sys
def combList(charString, maxLength):
    """Genorate inital word list. This is just diff combinations"""
    #var to keepmtrack of how many times we've been through the loop
    times = 0
    #list to hold combinations
    poss = []
    for iteration in range(maxLength):
        #Use try statment to make sure the max length isn't longer
        #than the characters we're going to use
        try:
            #Iter genorator for combos
            comb = itertools.combinations(charString,times+1)
        except ValueError:
            print "Character string larger than max lenght\nplease try again"
            sys.exit()

        #Genorator gives tuple with seporated values ex: ('w','o','r','d')
        for word in comb:
            #join tupe as string and add to list
            s = ''.join(word)
            poss.append(s)
        times += 1

    return poss

def permList(combinations):
    """Genorates permutations of the genorated combonation list"""
    #going to write ultimate list to a file
    #if not, you can run into virtual memory errors if the list gets above 4Gb
    f = open("wordlist.txt","w")
    #var to hold how many words we have
    x = 0
    for word in combinations:
        #loop through combonations and genorate a list of all
        #possable ways to combine letters
        permutation = itertools.permutations(word)
        for permWord in permutation:
            f.write(''.join(permWord)+"\n")
            x += 1
        #del used permutation to free up some memory
        #not so much needed, but this script will rape memory if
        #appending to a list insteady of writing to a file
        del permutation
    #always close file handles
    f.close()
    return x

def main():
    """Main program, gets user info and computes the lists"""
    ch = raw_input("characters to try: ")
    num = input("max length: ")
    combo = combList(ch,num)
    print "list genorated"
    print "doing wordlist now"
    permTotal = permList(combo)
    f = open("wordlist.txt","r")
    print "working..."
    for i in range(permTotal+1):
        word = f.readline().strip()
        #This is where you would be doing the actule brute forcing
        #you could try and log into a website or crack a password protected
        #zip file, genorate md5's and crack a password dump
        #if linux, brute force WPA wifi with iwconfig
        #and any thing else you might need for a password
        print word
    f.close()
    print "done\n"
    raw_input(".....")

main()
