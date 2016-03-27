#!/usr/bin/python

import os, re

p1 = re.compile('\d{8}$')
p2 = re.compile('\d+\.\d{2}$')

this_dir = os.path.dirname(os.path.realpath(__file__))
filenames = []
for filename in os.listdir(this_dir + '/logs'):
  if p1.match(filename):
    filenames.append(filename)
filenames.sort()

with open(this_dir + '/data/data.csv', 'w') as f_out:
  f_out.write('pressure,date\n')
  for filename in filenames:
    with open(this_dir + '/logs/' + filename, 'r') as f_in:
      content = f_in.readlines()
    for line in content:
      m = p2.search(line)
      if m:
        value = m.group()
        string = '{},{}-{}-{} {}\n'.format(value, filename[0:4], filename[4:6], filename[6:8], line[0:2])
        f_out.write(string)

