from argparse import ArgumentParser


def pagenum_filter(inpfile, outfile=None, sep="=", style='arabic'):
    sep = 3*sep
    with open(inpfile) as f:
        lines = f.readlines()
    page_count_temp = ".. raw:: pdf\n\n    SetPageCounter {pagenum} {style}\n\n"

    # filter out above title separtors
    sepinds = [i for i, line in enumerate(lines) if line.startswith(sep)]
    extrainds = {i for i, j in zip(sepinds[:-1], sepinds[1:]) if 2 == j - i}
    lines = [line for i, line in enumerate(lines) if i not in extrainds]

    # get the start of eash slide
    sepinds = [i for i, line in enumerate(lines) if line.startswith(sep)]
    beginds = [i - 1 for i in sepinds]

    # Add counter
    pagenum = 1
    i = beginds[0]
    prevlines = lines[i:i+3]
    lines[i+1] += page_count_temp.format(pagenum=pagenum, style=style)
    for i in beginds[1:]:
        if prevlines != lines[i:i+3]:
            pagenum += 1
            prevlines = lines[i:i+3]
        lines[i+1] += page_count_temp.format(pagenum=pagenum, style=style)

    # print or write out
    newfile = "".join(lines)
    if outfile == '' or outfile is None:
        print newfile          
    else:
        with open(outfile, 'w') as f:
            f.write(newfile)


def main():
    parser = ArgumentParser(description='Add page numbers.')
    parser.add_argument('inpfile', type=str, help='path to input file')
    parser.add_argument('-o', dest="outfile", type=str, help='path to output file')
    parser.add_argument('--sep', dest='sep', action='store', default="=",
                        help='the topmost rst separator (=-.*~`$&^!...)')
    parser.add_argument('--style', dest='style', action='store', default="arabic",
                        help=('Page counter style, values possible: '
                             'arabic,roman,lowerroman,alpha,loweralpha.'))
    args = parser.parse_args()
    pagenum_filter(args.inpfile, args.outfile, sep=args.sep, style=args.style)


if __name__ == "__main__":
    main()
