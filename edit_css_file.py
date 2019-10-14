def edit_css(file):
    """
    Read Boostrap css file and arrange it in a readable format
    :param file:
    :return:
    """
    with open(file, 'r') as f:
        for line in f:
            if '}' in line:
                new = line.split('}')
                f = open("bootstrap.mins.css", "w+")
                for item in new:
                    f.write(item + '}')
                f.readlines()


edit_css('bootstrap.min.css')


