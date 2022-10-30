# Definition:
#  A word w is an anagram of a word v if a permutation of the letters transforming w into v exists. 
#  Given a set of n words of length at most k, we would like to detect all possible anagrams. 

# input:​below the car is a rat drinking cider and bending its elbow while this thing 
#       is an arc that can act like a cat which cried during the night caused by pain 
#       in its bowel1 
      
# output: ​{bowel below elbow}, {arc car}, {night thing}, {cried cider}, {act cat} 

# Complexity The proposed algorithm solves this problem in time O(nk log k) on average, 
# and in O(n2 k log k) in the worst case, due to the use of a dictionary. 

# Algorithm: The idea is to compute a signature for each word, so that two words 
#            are anagrams of each other if and only if they have the same signature. 
#            This signature is simply a new string made up of the same letters sorted 
#            in lexicographical order. 
#            The data structure used is a dictionary associating with each signature the list of words with this signature.


def anagram(input):
    return []


def main():
    print(anagram("""
    ​below the car is a rat drinking cider and bending its elbow while this thing 
    is an arc that can act like a cat which cried during the night caused by pain 
    in its bowel1
    """))

if __name__ == "__main__":
    main()