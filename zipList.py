tableData = [['apples', 'oranges', 'cherries', 'banana'],
                     ['Alice', 'Bob', 'Carol', 'David'],
                     ['dogs', 'cats', 'moose', 'goose']]




for a, b, c in zip(tableData[0], tableData[1], tableData[2]):
    print(a.rjust(10), b.rjust(10), c.rjust(10))
