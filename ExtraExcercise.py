def main():
    s1 = 'Hello'
    s2 = 'olleH'
    s3 = 'ollH'
    print(s1, ' and ', s2, ' are ', isAnagram(s1, s2))
    print(s1,' and ',s3, ' are ',isAnagram(s1, s3))


def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return 'not Anagram!!'
    temp = ''
    for i in range(len(s2) -1,-1,-1):
        temp += s2[i]
    if s1 == temp:
        return 'Anagram!'
    else:
        return 'not Anagram!'

if __name__ == '__main__':
    main()
