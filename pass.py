
string = "life!!"

def password(string):
    lc = sum([ 1 for s in string if s == str.lower(s) and s != str.upper(s) ])
    uc = sum([ 1 for s in string if s == str.upper(s) and s != str.lower(s) ])
    oth = sum([ 1 for s in string if s == str.upper(s) and s == str.lower(s) ])
    return lc > 0 and uc > 0 and oth > c

print (password(string))

def strength(string):
    lc = sum([ 1 for s in string if s == str.lower(s) and s != str.upper(s) ])
    uc = sum([ 1 for s in string if s == str.upper(s) and s != str.lower(s) ])
    oth = sum([ 1 for s in string if s == str.upper(s) and s == str.lower(s) ])
    return lc /4  +  uc / 4 + oth

print (strength(string))


    
