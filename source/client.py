'''Example python interface

**Not to be run on the feather**

'''

import serial
import csv
from time import sleep
import matplotlib.pyplot as plt

class fc():
  def __init__(self, *argv):
      self.s = serial.Serial(argv[0],11500,timeout=1)

  def send(self, cmd):
      self.s.write(f'{cmd}\n\r'.encode('utf-8'))

  def read(self, *argv):
      r = []
      while self.s.in_waiting:
      	r = self.s.readlines()
      if len(argv) > 0:
          r = clean(r)
      return r

  def dia(self, cmd, duration = 1):
      self.send(cmd)
      sleep(duration)
      return [i.rstrip().decode() for i in self.read()]

def clean(response):
  out = []
  for i in response:
      try:
          out += [ list(map(float,i.strip(b'][\r\n').split(b', '))) ]
      # Silently ignore non-numbers
      except ValueError:
          pass
  return out

def save(filename, data):
  with open(filename, mode='w', newline='') as f:
      fw = csv.writer(f, delimiter=',')
      for i in data:
          fw.writerow(i)

def plot(*data):
    for d in data:
        x = [i[0] for i in d]
        y = [i[1] for i in d]
        plt.plot(x, y)
    plt.xlabel("Potential (V)")
    plt.ylabel("Current (A)")
    plt.show()
