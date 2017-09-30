import time

test1 = "Exercises 10: 4, 6, 12, 16, 20, 22, 24, 39, 40, 41, 43, 44"

def make_path_name():
    return "tmp/" + time.strftime("%Y%m%d-%H%M%S") + ".txt"


def gen_latex(txt, path=make_path_name()):



    lst = text_to_lst(txt)
    f = open(path, 'w')
    f.write("\section{Textbook Exercises}\n")
    for exercise in lst:

        block = make_latex_block(exercise)
        f.write(block)


    f.close()
    



def text_to_lst(txt):
    # Assume input looks like this: Exercises 10: 4, 6, 12, 16, 20, 22, 24, 39, 40, 41, 43, 44

    txt = txt.replace(":", "")
    txt = txt.replace(",", "")
    lst = txt.split(" ")
    chapter = lst[1]
    # Ignore "Exercises" and the chpater number
    lst = lst[2:]
    lst = [chapter + "." + x for x in lst]

    return lst

def make_latex_block(exercise):
    # Desired about for input "10.1":
    # \begin{mdframed}
    # \textbf{10.6}
    # 
    # 
    # \end{mdframed}

    block = "\\begin{mdframed}\n"
    block += "\\textbf{" + exercise + "}\n"
    block += "\n\n"
    block += "\\end{mdframed}\n"
    return block


lst1 = text_to_lst(test1)
