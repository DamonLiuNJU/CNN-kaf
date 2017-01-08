# -*- coding: utf-8 -*-
import data_helpers
import keras
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import gensim

model = gensim.models.Word2Vec.load('./data/review.model.bin')
key = '京东'
key = key.decode('utf8')
# print model[key]

x = data_helpers.my_get_input_sentence()
model = keras.models.load_model('./simple_net.h5')
y = model.predict(x)
dict = ['business', 'service', 'others', 'product',
        'platform']
print y
predict_label = []
# for index in range(len(x)):
#     predict_label[index] = dict[y[index]]

result = model.predict_proba(x)

# print result
