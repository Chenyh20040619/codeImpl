from config import ModelConfig
from dataset import Data_convert

config=ModelConfig()#实例化配置
data_train = Data_convert(config.input_path_train, config.seq_len, config.batch_size)
vocab_train, sentence_train, label_train, sentences_train = data_train.count_s()  # 返回字典，分词句子，标签
# print('字典')
# print(vocab_train) # {'，': 1, '的': 2, '。': 3, ' ': 4, '是': 5, '、': 6, '《': 7, '》': 8, '了': 9, '年': 10, '在': 11, '很': 12,
# print('分词句子')
# print(sentences_train) # ['毕棚', '沟', '的', '风景', '早有所闻', '，', '尤其', '以', '秋
# print('标签')
# print(label_train) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
# print(sentences_train) # ['毕棚', '沟', '的', '风景', '早有所闻', '，', '尤其', '以', '秋季', '的', '风景', '最美', '，', '
print(len(vocab_train))
print(len(sentence_train))
print(len(label_train))
print(len(sentences_train))
# train_loader = data_train.data_for_train_txt(sentence_train, vocab_train, label_train)
