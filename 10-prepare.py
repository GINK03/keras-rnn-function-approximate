import math

import random

import sys

import pickle
# サイクロイド
"""
x = a ( theta  - sin theta )
y = a ( theta  - cos theta )
"""
pairs = []
for i in range(-100000,100000):
  theta = i/100.0
  a = 1
  x = a * ( theta - math.sin(theta) )
  y = a * ( 1. - math.cos(theta) )
  pairs.append( (x, y) )

datasets = []
for i in range(len(pairs)-10):
  X1 = [[y] for x,y in pairs[i:i+9]]
  X2 = [[x] for x,y in pairs[i:i+9]]
  y = list(pairs[i+9])[1]
  datasets.append( (X1, X2, y) )

open('サイクロイド.pkl', 'wb').write( pickle.dumps( datasets ) )

# アステロイド
pairs = []
for i in range(-100000, 100000):
  theta = i/100.0
  a = 1
  x = a * ( math.pow(math.sin(theta),3) )
  y = a * ( math.pow(math.cos(theta),3) )
  pairs.append( (x, y) )

datasets = []
for i in range(len(pairs)-10):
  X1 = [[y] for x,y in pairs[i:i+9]]
  X2 = [[x] for x,y in pairs[i:i+9]]
  y = list(pairs[i+9])
  datasets.append( (X1, X2, y) )

open('アステロイド.pkl', 'wb').write( pickle.dumps( datasets ) )

# カージオイド
pairs = []
for i in range(-100000,100000):
  theta = i/1000.0
  a = 1
  x = a * ( 1. + math.cos(theta) ) * math.cos(theta)
  y = a * ( 1. + math.cos(theta) ) * math.sin(theta)
  pairs.append( (x, y) )

datasets = []
for i in range(len(pairs)-10):
  X1 = [[y] for x,y in pairs[i:i+9]]
  X2 = [[x] for x,y in pairs[i:i+9]]
  y = list(pairs[i+9])
  datasets.append( (X1, X2, y) )
open('カージオイド.pkl', 'wb').write( pickle.dumps( datasets ) )
sys.exit()

# 対数らせん
pairs = []
for i in range(100):
  theta = i/20.0
  a = 1
  x = a * ( math.pow(math.e, theta/(2*math.pi) ) ) * math.cos(theta)
  y = a * ( math.pow(math.e, theta/(2*math.pi) ) ) * math.sin(theta)
  pairs.append( (x, y) )

for pair in pairs:
  x, y = pair
  print(x, y)

# リサージュ曲線
pairs = []
for i in range(100):
  theta = i/20.0
  a = 1
  x = a * math.sin(3. * theta + 0.0)
  y = a * math.cos(4. * theta)
  pairs.append( (x, y) )

for pair in pairs:
  x, y = pair
  print(x, y)

# インボリュート
pairs = []
for i in range(100):
  theta = i/20.0
  a = 1
  x = math.cos(theta) + theta * math.sin(theta)
  y = math.sin(theta) - theta * math.cos(theta)
  pairs.append( (x, y) )

for pair in pairs:
  x, y = pair
  print(x, y)


