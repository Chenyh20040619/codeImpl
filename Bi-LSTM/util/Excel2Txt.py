import pandas


# 格式转换
def Excel_to_Txt(input_path, output_path):
    df = pandas.read_excel(input_path, header=None)
    print('开始写入txt文件')
    df.to_csv(output_path, header=None, sep='\t', index=False)  # sep指定分隔符，分隔单元格
    print('写入成功')


# 创建同路径同名TXT文件
def creat_txt(input_path):
    length = len(input_path)
    output_path = ''
    for i in range(length - 1, -1, -1):
        if input_path[i] == '.':
            break
    for j in range(0, i + 1):
        output_path = output_path + input_path[j]
    output_path = output_path + 'txt'
    # file = open(output_path,)
    return output_path


if __name__ == '__main__':
    in_path = r'D:\Programme\Python\py_project\github\BI-LSTM-sentiment-classify\dataset\cqk.xlsx'
    out_path = r'D:\Programme\Python\py_project\github\BI-LSTM-sentiment-classify\dataset\test.txt'
    Excel_to_Txt(in_path, out_path)