import re
from argparse import ArgumentParser


def slidebreak_filter(inpfile, outfile=None, sep="="):
    sep = 3*sep
    with open(inpfile) as f:
        lines = f.readlines()
    re_break = re.compile("..\s+break\s*\n")

    # filter out above title separtors
    sepinds = [i for i, line in enumerate(lines) if line.startswith(sep)]
    extrainds = {i for i, j in zip(sepinds[:-1], sepinds[1:]) if 2 == j - i}
    lines = [line for i, line in enumerate(lines) if i not in extrainds]

    # get the start of eash slide
    sepinds = [i for i, line in enumerate(lines) if line.startswith(sep)]
    beginds = [i - 1 for i in sepinds] + [999999999]

    # Add counter
    newlines = lines[:beginds[0]]
    for i, j in zip(beginds[:-1], beginds[1:]):
        slide = lines[i:j]
        newslide = []
        for line in slide:
            if re_break.match(line):
                newlines.extend(newslide)
                newslide = newslide[:-1]
            else:
                newslide.append(line)
        newlines.extend(newslide)

    # print or write out
    newfile = "".join(newlines)
    if outfile == '' or outfile is None:
        print newfile
    else:
        with open(outfile, 'w') as f:
            f.write(newfile)


def main():
    parser = ArgumentParser(description='Duplicate sections at breaks.')
    parser.add_argument('inpfile', type=str, help='path to input file')
    parser.add_argument('-o', dest="outfile", type=str, help='path to output file')
    parser.add_argument('--sep', dest='sep', action='store', default="=",
                        help='the topmost rst separator (=-.*~`$&^!...)')
    args = parser.parse_args()
    slidebreak_filter(args.inpfile, args.outfile, sep=args.sep)


if __name__ == "__main__":
    main()
