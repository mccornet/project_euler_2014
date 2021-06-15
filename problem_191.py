from tools import memoize


"""
A particular school offers cash rewards to children
with good attendance and punctuality. If they are
absent for three consecutive days or late on more
than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed
for each child consisting of L's (late), O's (on time),
and A's (absent).

Although there are eighty-one trinary strings for a
4-day period that can be formed, exactly forty-three
strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?
"""


@memoize.memoized
def week(days_left, late=0, absent_streak=0):
    """
    Solves problem recursivly.
    Returns the number of succes out of the number of total possibilities.
    """

    # end case 1: 'midweek' but late > 1 or absent streak of 3
    if late > 1 or absent_streak == 3:
        # 0 succes out of all the number of possible remaining day options
        return 0, 3**days_left if days_left else 1

    # end case 2: end of week without tripping absent streak or late penalty
    if days_left == 0:
        return 1, 1  # 1 succes out of 1 try

    # pick all three possibilities
    # 1. on time
    s_o, t_o = week((days_left - 1), late, 0)  # keep late, reset absent streak

    # 2. absent
    s_a, t_a = week(days_left - 1, late, absent_streak + 1)

    # 3. late
    s_l, t_l = week(days_left - 1, late + 1, 0)

    assert(t_o + t_a + t_l == 3 ** days_left)

    # Return: number of succes, total_possibilities
    return (s_o + s_a + s_l), (t_o + t_a + t_l)

s, t = week(30)

print(s, t)
