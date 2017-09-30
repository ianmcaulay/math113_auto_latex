import time


def make_path_name():
    return "tmp/" + time.strftime("%Y%m%d-%H.%M.%S") + ".txt"


def write_latex(txt, path=make_path_name()):

    f = open(path, 'w')
    f.write("\section{Textbook Exercises}\n")
    txt_lst = txt.split("\n")
    for chap_txt in txt_lst:
        write_chapter_latex(chap_txt, f)

    f.close()


def write_chapter_latex(chap_txt, f):

    lst = text_to_lst(chap_txt)
    for exercise in lst:
        block = make_latex_block(exercise)
        f.write(block)


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
    # Desired about for input "10.1" (including newline after \end):
    # \begin{mdframed}
    # \textbf{10.6}
    # 
    # 
    # \end{mdframed}
    # 

    block = "\\begin{mdframed}\n"
    block += "\\textbf{" + exercise + "}\n"
    block += "\n\n"
    block += "\\end{mdframed}\n\n"
    return block

def run_tests():
    # Single chapter
    test1 = "Exercises 10: 4, 6, 12, 16, 20, 22, 24, 39, 40, 41, 43, 44"
    write_latex(test1)
    # Two chapters
    f2 = open("test/multiline.txt")
    test2 = f2.read()
    f2.close()
    write_latex(test2)
