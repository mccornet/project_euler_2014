from tools import memoize
from operator import add


"""
A printing shop runs 16 batches (jobs) every week and each batch
requires a sheet of special colour-proofing paper of size A5.

Every Monday morning, the foreman opens a new envelope,
containing a large sheet of the special paper with size A1.

He proceeds to cut it in half, thus getting two sheets of size A2.
Then he cuts one of them in half to get two sheets of size A3
and so on until he obtains the A5-size sheet needed for the first
batch of the week.

All the unused sheets are placed back in the envelope.

At the beginning of each subsequent batch, he takes from the envelope
one sheet of paper at random. If it is of size A5, he uses it. If it
is larger, he repeats the 'cut-in-half' procedure until he has what he
needs and any remaining sheets are always placed back in the envelope.

Excluding the first and last batch of the week, find the expected number
f times (during each week) that the foreman finds a single sheet of paper
in the envelope.

Give your answer rounded to six decimal places using the format x.xxxxxx
"""


@memoize.memoized
def expected_value(envelope="a2,a3,a4,a5", job=0, single_sheet=0):

    # end of week, done!
    if job == 14:
        total = [0] * 15
        total[single_sheet] = 1
        total[-1] = 1
        total = tuple(total)
        return total

    # store results
    totals = [0] * 15

    # split string into elements
    envelope_list = envelope.split(",")

    # only one sheet?
    if len(envelope_list) == 1:
        single_sheet += 1

    # try all sheets
    for sheet in envelope_list:

        # construct new enveloppe
        new_envelope_list = list(envelope_list)  # deep_copy

        # remove from chosen sheet from enveloppe
        new_envelope_list.remove(sheet)

        # cut into pieces if needed
        if sheet == "a2":
            new_envelope_list.append("a3")
            new_envelope_list.append("a4")
            new_envelope_list.append("a5")
        if sheet == "a3":
            new_envelope_list.append("a4")
            new_envelope_list.append("a5")
        if sheet == "a4":
            new_envelope_list.append("a5")

        # sort enveloppe
        new_envelope_list.sort()

        # recursive call
        res = expected_value(",".join(new_envelope_list), job + 1, single_sheet)

        totals = list(map(add, totals, res))

    return tuple(totals)

res = expected_value()

print(res)

ev = 0
i = 0

for sub_res in res[0:4]:

    ev += ((sub_res / res[-1]) * i)
    i += 1

    print(ev)

print(res[1] / res[-1])
