import string
import glob  
import sys   

# this is for using the tweet_input location to get the input text files:
ip=str(sys.argv[1]+"/*")
# this is for using ft1 file as the location for output files:
op=str(sys.argv[2])

files=glob.glob(ip)
# wc - wordcount dictionary to count thenumber of word instances:
wc = {}
# parsing all the files in twp_ip directory
for file in files:
    with open(file, 'r') as fl:
        # checking every line in the file
        for line in fl:
            special_character_map = dict.fromkeys(map(ord, string.punctuation))
            # removing all the special characters from text
            line=line.translate(special_character_map)
            # converting all the letters in line to lower case.
            words = line.lower().split()
            # for each word checking if it has already appeared or not and then count the no. of appearances
            for w in words:
                if(w in wc): 
                    wc[w]+=1
                else: 
                    wc[w]=1
with open (op, 'w') as fout:
   # writing the words and their number of instances in the ft1 file
   for w in sorted(wc):
      fout.write(w +"\t" +str(wc[w])+ "\n")

