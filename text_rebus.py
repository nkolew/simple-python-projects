def text_rebus(string):
    """
    Input: string // Eines Tages fiel der Esel eines Bauern in den Brunnen
    Output: scrambled words string // Eine Stage Sfie Lde Rese Leine Sbauer Ni Nde Nbrunne
    """

    lst = string.split()
    result = ''

    for word in range(len(lst)):
        if word == 0:
            result += (lst[word][:-1] + ' ')
        else:
            result += (lst[word-1][-1] + lst[word][:-1] + ' ')
        result = result.title()

    return(result)


text_rebus()
