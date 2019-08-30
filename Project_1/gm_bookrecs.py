# Garrett Matthews
# Project 1: Book Recommendations

# I declare that the following source code was written solely by me. I understand that copying any source code,
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation
# of this policy. #

# Read booklist.txt as a list of tuples (author name, title)

book = open('booklist.txt', 'r')

books = []
for line in book:
    books.append(tuple(line.split(',')))
# Remove '\n' from each tuple, and remake into tuple
q = 0
for i in books:
    for z in i:
        temp = [x.replace('\n','') for x in i]
        books[q] = temp
    q += 1

books = [tuple(r) for r in books]

# Read ratings into dictionary keyed by name, lowercase, preserving original order
rate = open("ratings.txt",'r')
# Changing the names to lowercase
rating_total = []
for line in rate:
    for words in line.split(','):
        rating_total.append(words.lower())

# Making lists of just names, removing '\n', and a list of the ratings
rating_name = rating_total[0::2]
rating_name = [x.replace('\n','') for x in rating_name]
rating_value = rating_total[1::2]

# Changing the list of scores into a nested list of integers for convenience
scores = []

for i in range(len(rating_value)):
    sc_str = str(rating_value[i])
    scores.append(sc_str.split())
for i in scores:
    for numb in range(len(i)):
        i[numb] = int(i[numb])

# Combining the lists into a dictionary
ratings = {}
ratings = dict(zip(rating_name,scores))


# Write a function dotprod(x,y)

def dotprod(x,y):
    """Function to find the dot product of list x and list y"""
    ans = 0
    if len(x) == len(y):
        for i in range(len(x)):
            ans += x[i] * y[i]
        return ans
    elif x == '' or y == '':
        return None
    else:
        return None

# Compute similarity score for each user, and map these scores to another dictionary which maps the names of the
# other readers to their name (example: {ben: {moose : 134, etc}...}

def sim_score(dict):
    """Finds the similarity score of users based on a inputted dictionary dict"""
    # Finding dot product for each set of scores
    result = {}
    for key1 in dict:
        temp = {}
        for key2 in dict:
            if key1 != key2:
                ans = dotprod(dict[key1],dict[key2])
                temp[key2] = ans
                result[key1] = temp
    return result

# Write friends using heapq.nlargest so you don't have to sort the whole thing

def friends(name, dict, nfriends = 2):
    """Finds a number of friends n that have the greatest similarity to name, using a dictionary. Defaults to two"""
    from heapq import nlargest
    from operator import itemgetter
    res = sim_score(dict)
    top = nlargest(nfriends,res[name].items(), key= lambda i: i[1])
    name = []
    for i in range(len(top)):
        temp = top[i]
        for z in range(len(temp)):
            var = temp[z]
            name.append(var)
    name = name[0::2]
    return(name)

# Write recommend, calling friends

def recommend(name, dict, nfriends = 2):
    """Recommend books from number of friends n that have similar taste"""
    rec = friends(name, dict, nfriends)
    list = []
    person = dict[name]
    for key in range(len(rec)):
        top = rec[key]
        like = dict[top]
        for i in range(len(like)):
            if float(person[i]) == 0:
                if float(like[i]) >= 3:
                    list.append(books[i])
    return list



# Have your main logic call friends and recommend to produce the required report

def main():
    """This function compiles the book recommendation report, based on readers who have similar interests"""
    with open('recommendations.txt', 'w') as rcm:
        for key in ratings:
            friend = friends(key,ratings)
            recom = recommend(key,ratings)
            rcm.write("{}{}{}".format(key,':',friend) + '\n')
            for i in recom:
                rcm.write("{}{}{}".format('\t',i,'\n'))


main()