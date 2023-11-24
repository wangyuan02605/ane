#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from speech_model import ModelSpeech
from speech_model_zoo import SpeechModel26
from speech_features import Spectrogram
from LanguageModel import ModelLanguage
from utils.ops import cosine_similarity

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
class modelTest:
    """
    TODO:
    定义初始化方法__init__，初始化模型路径,创建声学模型对象。
    """
    def __init__(self):
        self.sm26=SpeechModel26((1600, 200, 1),1428)
        self.sm26.load_weights("save_models/PretrainedModel.h5")
        self.spec=Spectrogram()
        self.sm=ModelSpeech(self.sm26,self.spec)
        self.ml = ModelLanguage('model_language')
        self.ml.LoadModel()



    '''
    TODO:
    定义识别函数recognize()，实现模型的调用并成功输出识别到的语句。
    '''
    def recognize(self):
        pass



mt = modelTest()
sm_out=mt.sm.recognize_speech_from_file("1.wav")
mt.ml.SpeechToText(sm_out)