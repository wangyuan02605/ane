#TODO 导入相关的Python库或Python模块
import re
from stanfordcorenlp import StanfordCoreNLP
from random import random
corpus_root = r""
file_pattern = r"赛位号_hospital.txt"
#TODO 将“赛位号_ hosptial.txt”文件内容作为语料，选择用于分析文本文件的方法载入语料，并输出文本内容
with open(file_pattern,"r",encoding="utf-8") as f:
    data=f.read()
#TODO 对文本内容进行数据清洗操作，要求：清洗掉出汉字以外的字符
cleandata=re.sub(r'[^\u4e00-\u9fff]+',"",data)
#要背过
print('清洗后的数据为>>>>>>>>>')
print(cleandata)
#TODO 对清洗后的数据内容进行数据扩充，要求：返回2个增强文本，文本改变率要求为25%
def enhance_text(text):
    enhanced_texts = []
    for _ in range(2):
        enhanced = ''.join(c if random() > 0.25 else '生病' for c in text)
        enhanced_texts.append(enhanced)
    return enhanced_texts

#TODO 结合循环输出数据扩充后的结果
print('扩充后的数据为>>>>>>>>>')
for  i in enhance_text(cleandata):
    print(i)

nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-02-27', lang='zh')
nlp.word_tokenize(cleandata)
nlp.pos_tag(cleandata)
nlp.ner(cleandata)