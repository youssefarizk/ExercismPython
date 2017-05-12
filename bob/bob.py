def hey(convo):
    if convo.isupper(): 
        return "Whoa, chill out!"
    elif convo.split() == []:
        return "Fine. Be that way!"
    elif convo.split()[-1][-1] == '?':
        return "Sure."
    else: return "Whatever."

