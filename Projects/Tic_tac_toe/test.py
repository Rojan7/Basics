board = [' ' for x in range(9)]
for row in [board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


