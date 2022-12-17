#coding='utf-8'

class ModelConfig:
    batch_size = 64
    batch_size_pred = 100
    output_size = 1#输出维度
    hidden_dim = 128   #256/2
    seq_len=100#句长
    embed=100
    n_layers = 2
    dropout=0.5
    bidirectional = True  #这里为True，为双向LSTM
    # training params
    epochs = 50
    lr=0.0003#学习率
    print_every = 20
    input_path_pred= r'pred.txt'  #待预测文件
    input_path_train=r'dataset/data.txt'#训练集文件
    input_path_test=r'dataset/test.txt'#测试集文件
    input_path_all=r'dataset/data.txt'#训练集和测试集在一个文件
    save_model_path = r'result\model\bi-lstm.tar'#模型保存路径
    save_dict_path = r'result\dict\vocab_train.dict'#字典保存路径，npy文件
    save_pred_path = r'result\prediction\predict_out.xlsx'#预测结果保存路径，excel

