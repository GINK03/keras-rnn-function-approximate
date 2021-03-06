import pickle
import gzip
import numpy as np
import random
import os
import sys
import statistics
import glob
import re
import json
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model, load_model
from keras.layers import Lambda, Input, Activation, Dropout, Flatten, Dense, Reshape, merge
from keras.layers import Multiply, Conv1D, MaxPool1D, BatchNormalization, RepeatVector, GRU
from keras.layers.merge import Concatenate
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization as BN
from keras.layers.core import Dropout
from keras.layers.noise import GaussianNoise as GN
from keras.optimizers import SGD, Adam, RMSprop
from keras import backend as K
from keras.layers.wrappers import Bidirectional as Bi
from keras.layers.wrappers import TimeDistributed as TD

input1 = Input( shape=(9,) )

enc1 = input1
enc1 = Reshape((1,9))(enc1)
enc1 = GRU(512, dropout=0.2, recurrent_dropout=0.2, return_sequences=False)(enc1)
#enc1 = Dense(512, activation="relu")(enc1)

input2 = Input( shape=(9,) )
enc2 = input2
#enc2 = Reshape((1,9))(enc2)
#enc2 = GRU(256, dropout=0.2, recurrent_dropout=0.2, return_sequences=False)(enc2)
enc2 = Dense(512,activation="relu")(enc2)

m   = Concatenate(axis=-1)([enc1,enc2])
dec = Dense(3000, activation='relu')(m)
dec = Dense(1000, activation='relu')(dec)
decode  = Dense(2, activation='linear')(dec)


model = Model(inputs=[input1, input2], outputs=decode)
model.compile(loss='mse', optimizer='adam', metrics=['mse'])

import pickle
import gzip
import numpy as np
import glob
import sys

if '--train' in sys.argv:
  dataset = pickle.loads( open('対数らせん.pkl', 'rb').read() )
  X1, X2, y, X1test, X2test, ytest = [], [], [], [], [], []
  for data in dataset:
    _x1, _x2, _y = data
    if random.random() < 0.992:
      X1.append( _x1 ) 
      X2.append( _x1 ) 
      y.append( _y )
    else: 
      X1test.append( _x1 ) 
      X2test.append( _x2 ) 
      ytest.append( _y )

  X1, X2, y, X1test, X2test, ytest = map(np.array, [X1, X2, y, X1test, X2test, ytest])
  open('testdataset.pkl', 'wb').write( pickle.dumps( (X1test, X2test, ytest) ) )
  model.fit( [X1, X2], y, shuffle=True, epochs=200, validation_data=([X1test, X2test], ytest) )
  model.save_weights('models/model.h5')

if '--predict' in sys.argv:
  #print(dataset)
  X1test, X2test, ytest = pickle.loads( open('testdataset.pkl', 'rb').read() )

  model.load_weights('models/model.h5')

  yps = model.predict([X1test, X2test])
  for index, (x1test, x2test, yp) in enumerate(zip(X1test.tolist(), X2test.tolist(), yps.tolist())):
    #print( index, x1test.pop(), x2test.pop(), yp[0] )
    print( index, yp[0], yp[1] )
