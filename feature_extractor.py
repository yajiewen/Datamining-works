import numpy as np
def get_data():

    data_dict={

        '0' : [],
        '1' : [],
        '2' : [],
    }
    with open('kddtrain2020.txt','r') as datas:
        for line_ in datas.readlines():
            line_=line_.strip()
            list_s = line_[:].split(' ')
            # print(list_s) 显示每一行

            data_dict[list_s[-1]].append([float(num) for num in list_s[:-1]])

            print('0 的样本数量为{}\n1 的样本数量为{}\n3 的样本数量为{}\n'.format(len(data_dict['0']),len(data_dict['1']),len(data_dict['2'])))
        
        print('0 每个样本长度{}\n1 每个样本长度{}\n3 每个样本长度{}\n'.format(len(data_dict['0'][15]),len(data_dict['1'][60]),len(data_dict['2'][1000])))
        return data_dict.copy()
    
#WF ATTACK FEATURES===========================================================================================
#client time span 平均数，最大最小值，标准差，75百分位数 （-1 减去+1）
def client_to_server_time_features(time_list):
    sub_list=[]
    L = len(time_list)
    for j in range(1,L,2):
        sub_list.append(time_list[j]-time_list[j-1])

    cum_array = np.cumsum(sub_list)
    if sub_list:
        return (np.sum(sub_list),np.mean(sub_list),np.max(sub_list),np.min(sub_list),np.std(sub_list),np.ptp(sub_list),np.percentile(sub_list,100),np.percentile(sub_list,75),np.percentile(sub_list,50),np.percentile(sub_list,25),np.max(sub_list)/np.sum(sub_list),np.min(sub_list)/np.sum(sub_list),
        np.sum(cum_array),np.mean(cum_array),np.max(cum_array),np.min(cum_array),np.std(cum_array),np.ptp(cum_array),np.percentile(cum_array,100),np.percentile(cum_array,75),np.percentile(cum_array,50),np.percentile(cum_array,25))
    else:
        return tuple([0]*22)



def server_to_client_time_features(time_list):
    sub_list=[]
    L = len(time_list)
    for j in range(2,L,2):
        sub_list.append(time_list[j]-time_list[j-1])

    cum_array = np.cumsum(sub_list)
    if sub_list:
        return (np.sum(sub_list),np.mean(sub_list),np.max(sub_list),np.min(sub_list),np.std(sub_list),np.ptp(sub_list),np.percentile(sub_list,75),np.max(sub_list)/np.sum(sub_list),np.min(sub_list)/np.sum(sub_list),
        np.sum(cum_array),np.mean(cum_array),np.max(cum_array),np.min(cum_array),np.std(cum_array),np.ptp(cum_array),np.percentile(cum_array,75))
    else:
        return tuple([0]*16)


def client_to_client_time_features(time_list):
    sub_list=[]
    L = len(time_list)
    for j in range(2,L,2):
        sub_list.append(time_list[j]-time_list[j-2])

    cum_array = np.cumsum(sub_list)
    if sub_list:
        return (np.sum(sub_list),np.mean(sub_list),np.max(sub_list),np.min(sub_list),np.std(sub_list),np.ptp(sub_list),np.percentile(sub_list,75),np.max(sub_list)/np.sum(sub_list),np.min(sub_list)/np.sum(sub_list),
        np.sum(cum_array),np.mean(cum_array),np.max(cum_array),np.min(cum_array),np.std(cum_array),np.ptp(cum_array),np.percentile(cum_array,75))
    else:
        return tuple([0]*16)


def server_to_server_time_features(time_list):
    sub_list=[]
    L = len(time_list)
    for j in range(3,L,2):
        sub_list.append(time_list[j]-time_list[j-2])

    cum_array = np.cumsum(sub_list)
    if sub_list:
        return (np.sum(sub_list),np.mean(sub_list),np.max(sub_list),np.min(sub_list),np.std(sub_list),np.ptp(sub_list),np.percentile(sub_list,75), np.max(sub_list)/np.sum(sub_list),np.min(sub_list)/np.sum(sub_list),
        np.sum(cum_array),np.mean(cum_array),np.max(cum_array),np.min(cum_array),np.std(cum_array),np.ptp(cum_array),np.percentile(cum_array,75))
    else:
        return tuple([0]*16)


#packet两两间时间间隔的 和 平均数 ,最大值，最小值 标准差 75百分位数
def packet_to_packet_time_features(time_list):
    sub_list =[]
    L = len(time_list)
    for i in range(1,L):
        sub_list.append(time_list[i]-time_list[i-1])

    if sub_list:
        return (np.sum(sub_list),np.mean(sub_list),np.max(sub_list),np.min(sub_list),np.std(sub_list),np.ptp(sub_list),np.percentile(sub_list,75), np.max(sub_list)/np.sum(sub_list),np.min(sub_list)/np.sum(sub_list))
    else:
        return tuple([0]*9)
