import os

def get_opt():
    opt_lists = []
    op_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'options'))

    with open(op_path,'r') as opts:
        line_s = [opt.strip() for opt in opts.readlines() if len(opt.strip())!=0] #空行会读取为一个换行符
        print(line_s)
        for opt in line_s:
            if opt[0] != '#':
                key_value = opt.strip().split('=')
                opt_lists.append([key_value[0].strip(),key_value[1].strip()])
    opt_dict = dict(opt_lists)
    return opt_dict.copy() #不能返回引用
