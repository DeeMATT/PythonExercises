import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants"""
    total = os.path.getsize(path)                       # account for direct usage
    if os.path.isdir(path):                             # if this is a directory,
        for filename in os.listdir(path):               # then for each child:
            childpath = os.path.join(path, filename)    # compose full path to child
            try:
                total += disk_usage(childpath)                 # add child's usage to total
            except TypeError:
                total += 0
        print('{0:<7}'.format(total), path)             # descriptive output (optional)
        return total
    
    
print(disk_usage("/home/codemask/Documents/Python/PythonWorks/AlgorithmsLessons"))

