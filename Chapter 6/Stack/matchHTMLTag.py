from arrayStack import ArrayStack

#htmlDocx = '<body > <center > <h1 > The Little Boat < /h1 > </center > <p> The storm tossed the little boat like a cheap sneaker in an old washing machine. The three drunken fishermen were used to such treatment, of course, but not the tree salesman, who even as a stowaway now felt that he had overpaid for the voyage.</p><ol><li > Will the salesman die? < /li ><li > What color is the boat? < /li ><li > And what about Naomi? < /li ></ol></body >'
''' This program will check whether given a html document as string input,
    The html file is perfectly has closing and opening tag
    This will also print the text in bewteen each open tag and closing tag.
'''
def main():
    htmlDocx = '<body><li> And what about Naomi?<li> And what about Naomi? </li><li> And what about Naomi? </li></body>'
    print(isTagMatched(htmlDocx))


def isTagMatched(pattern):
    lastClosingBrac = 0
    s = ArrayStack()
    j = pattern.find('<')
    while j != -1:
        k = pattern.find('>',j+1)
        if k == -1:
            return False
        tag = pattern[j+1:k]
        if not tag.startswith('/'):
            s.push(tag)
            lastClosingBrac = k
        else:
            if s.isEmpty():
                return False
            l = s.pop()
            if tag[1:] != l:
                return False
            if k == len(pattern)-1:
                '''if k equals to length of the string, then we reach at the end of the string.
                Now we can print till j starting from current tag length + 1 '''
                print(pattern[len(tag)+1:j])
            else:
                ''' j has the index of current '<' and lastClosingBrac has the index of last seen '>' 
                So print in between text of both index from lastClosing Brac+1 till j.
                '''
                print(pattern[lastClosingBrac+1:j])
        j = pattern.find('<', k + 1)
    return s.isEmpty()


if __name__ == '__main__':
    main()

