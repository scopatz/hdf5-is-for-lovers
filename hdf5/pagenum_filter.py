from argparse import ArgumentParser


def pagenum_filter(inpfile, outfile, sep="=")
    sep = 3*sep
    outlines = []
    with open(inpfile) as f:
        inplines = f.readlines()

    # filter out above title separtors
    sepinds = [i for i, line in enumerate(inplines) if line.startswith(sep)]
    extrainds = {i for i, j in zip(sepinds[:-1], sepinds[1:]) if 2 == j - i}
    inplines = [line for i, line in enumerate(inplines) if i not in extrainds]
    sepinds = [i for i, line in enumerate(inplines) if line.startswith(sep)]

    pagenum = 0
    title = inpline[sepinds[0]-1]
    first_line = inpline[sepinds[0]+1]
    #for i, line in enumerate(inplines):
        

    #with open(outfile, 'w') as f:
    #    f.write("".join(outlines))


def main():
    parser = ArgumentParser(description='Add page numbers.')
    parser.add_argument('inpfile', type=str, help='path to input file')
    parser.add_argument('outfile', type=str, help='path to output file')
    parser.add_argument('--sep', dest='sep', action='store', default="=",
                        help='the topmost rst separator (=-.*~`$&^!...)')
    args = parser.parse_args()
    pagenum_filter(args.inpfile, args.outfile, sep=args.sep)


if __name__ == "__main__":
    main()
