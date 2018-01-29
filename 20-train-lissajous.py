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
from keras.layers import Multiply, Conv1D, MaxPool1D, BatchNormalization, RepeatVector, GRU, LSTM
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
from keras.layers.embeddings import Embedding
input1 = Input( shape=(1,) )
enc1 = input1
#enc1 = Embedding(1,256,input_length=1)(enc1)
enc1 = Dense(1000, activation="relu")(enc1)
enc1 = Dense(1000, activation="relu")(enc1)
#enc1 = Flatten()(enc1)

dec = Dense(1000, activation="relu")(enc1)
dec = Dense(1000, activation="relu")(dec)

decode  = Dense(2, activation='linear')(dec)


model = Model(inputs=[input1], outputs=decode)
model.compile(loss='mse', optimizer=Adam(lr=0.0008), metrics=['mse'])

import pickle
import gzip
import numpy as np
import glob
import sys

if '--train' in sys.argv:
  dataset = pickle.loads( open('リサージュ曲線.pkl', 'rb').read() )
  X1, y, X1test, ytest = [], [], [], []
  for data in dataset:
    _x1, _y = data
    if random.random() < 0.999:
      X1.append( _x1 ) 
      y.append( _y )
    else: 
      X1test.append( _x1 ) 
      ytest.append( _y )

  X1, y, X1test, ytest = map(np.array, [X1, y, X1test, ytest])
  open('testdataset.pkl', 'wb').write( pickle.dumps( (X1test, ytest) ) )
  model.fit( X1, y, shuffle=True, epochs=50)#, validation_data=([X1test, X2test], ytest) )
  model.save_weights('models/model.h5')

if '--predict' in sys.argv:
  #print(dataset)
  X1test, X2test, ytest = pickle.loads( open('testdataset.pkl', 'rb').read() )

  model.load_weights('models/model.h5')

  yps = model.predict([X1test, X2test])
  for index, (x1test, x2test, yp) in enumerate(zip(X1test.tolist(), X2test.tolist(), yps.tolist())):
    #print( index, x1test.pop(), x2test.pop(), yp[0] )
    print( index, yp[0], yp[1] )
