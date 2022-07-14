
from random import randint


def pick_lotto():
    maxm = 69
    maxj = 5
    m = maxm
    r = list(range(m + 1))
    v = []
    for j in range(maxj):
        i = randint(1, m)
        n = r[i]
        r[i:i + 1] = []
        m = m - 1
        v.append(n)
    power_ball = randint(1, 26)
    v.append(f'Power Ball: {power_ball}')
    return(v)


def run():
    done = False
    while not done:
        try:
            x = input('\npress Enter for Power Ball picks (Q to quit). ')
        except EOFError:
            x = 'q'
        if x and (x[0] == 'q' or x[0] == 'Q'):
            done = True
            print('done')
        else:
            print(pick_lotto())


# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
    run()
else:
    print("Module lotto imported.")
    print("To run, type: lotto.run()")
    print("To reload after changes to the source, type: reload(lotto)")
# end of lotto.py
