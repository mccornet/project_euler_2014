from __future__ import barry_as_FLUFL
import soul

>>>

print(barry_as_FLUFL)

with open ("problem_99.txt", "r") as myfile:
   powers = myfile.read().split("\n")


powers = [int(p.split(',')[1]) for p in powers]


powers.sort()

print(powers)
