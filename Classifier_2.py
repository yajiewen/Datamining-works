from feature_extractor import *
from get_options import get_opt
from sklearn.ensemble import RandomForestClassifier
import pickle
data_list = get_data()

opts = get_opt()
print(opts)

# data_dict = {
#     'train_features':[],
#     'train_lables':[],
#     'test_features':[],
#     'test_lables':[],

# }
total_acc_list = []
train_numm = []

test_dict = {
    '0':[],
    '1':[],
    '2':[],
}

acc_dict = {
    '0':[],
    '1':[],
    '2':[],
}

for j in range(1,1800,9):
    data_dict = {
        'train_features':[],
        'train_lables':[],
        'test_features':[],
        'test_lables':[],
    }

    test_num_ = []

    for sample_name in ['0','1','2']:
        count_num = 0
        num_train=0
        num_test=0
        for sample in data_list[sample_name]:
            sample_features = []
            #获得特征
            # sample_features.extend(client_to_server_time_features(sample[:]))
            # sample_features.extend(server_to_client_time_features(sample[:]))
            # sample_features.extend(client_to_client_time_features(sample[:]))
            # sample_features.extend(server_to_server_time_features(sample[:]))
            # sample_features.extend(packet_to_packet_time_features(sample[:]))
            sample_features = sample #特征就是他自己
            if count_num < j:
                #保存训练特征和lables
                data_dict['train_features'].append(sample_features)
                data_dict['train_lables'].append(int(sample_name))
                num_train+=1
            else:
                #保存测试特征和lables
                data_dict['test_features'].append(sample_features)
                data_dict['test_lables'].append(int(sample_name))
                num_test+= 1

            count_num += 1
        #输出划分结果看是否正确
        print('{}的训练样本数和测试样本数为 : {} {} 总的样本数为{}'.format(sample_name,num_train,num_test,num_test+num_train))
        #记录每一类的测试样本数
        test_dict[sample_name].append(num_test)

        test_num_.append(num_test)


    #训练分类器
    RFC=RandomForestClassifier(n_jobs=-1, n_estimators=1000, oob_score=True)
    RFC.fit(data_dict['train_features'],data_dict['train_lables'])

    Out_lables = RFC.predict(data_dict['test_features'])
    #得到每一类的Outlables he inlables
    out_lables_0 = Out_lables[:test_num_[0]]
    out_lables_1 = Out_lables[test_num_[0]:test_num_[0]+test_num_[1]]
    out_lables_2 = Out_lables[test_num_[0]+test_num_[1]:test_num_[0]+test_num_[1]+test_num_[2]]

    # print(len(out_lables_0)+len(out_lables_1)+len(out_lables_2))

    in_lables_0 = data_dict['test_lables'][:test_num_[0]]
    in_lables_1 = data_dict['test_lables'][test_num_[0]:test_num_[0]+test_num_[1]]
    in_lables_2 = data_dict['test_lables'][test_num_[0]+test_num_[1]:test_num_[0]+test_num_[1]+test_num_[2]]
    # print(len(in_lables_0)+len(in_lables_1)+len(in_lables_2))

    #0类的准确率
    right_num = 0
    for out_lable,in_lable in zip(out_lables_0,in_lables_0):
        if out_lable == in_lable:
            right_num+=1
    L =len(out_lables_0)

    acc_dict['0'].append(right_num/L)
    print('0 类的accuracy: {}'.format(right_num/L))


    right_num = 0
    for out_lable,in_lable in zip(out_lables_1,in_lables_1):
        if out_lable == in_lable:
            right_num+=1
    L =len(out_lables_1)

    acc_dict['1'].append(right_num/L)
    print('1 类的accuracy: {}'.format(right_num/L))


    right_num = 0
    for out_lable,in_lable in zip(out_lables_2,in_lables_2):
        if out_lable == in_lable:
            right_num+=1
    L =len(out_lables_2)

    acc_dict['2'].append(right_num/L)
    print('2 类的accuracy: {}'.format(right_num/L))

    #总的准确率
    right_num = 0
    for Out_lable,In_lables in zip(Out_lables,data_dict['test_lables']):
        if Out_lable == In_lables:
            right_num+=1
    print('Total_Accuracy :{}'.format(right_num/len(Out_lables)))
    total_acc_list.append(right_num/len(Out_lables))
    train_numm.append(j)



    # test_feature = get_test_2020()
    # test_lables1 = RFC.predict(test_feature)
    # with open('test_lables','w') as file_:
    #     for lable in test_lables1:
    #         file_.write(str(lable)+'\n') 
    # print(test_lables1)
    # print('共预测{}个样本'.format(len(test_lables1)))
pickle.dump(acc_dict['0'],open('0_acc','wb'))
pickle.dump(acc_dict['1'],open('1_acc','wb'))
pickle.dump(acc_dict['2'],open('2_acc','wb'))
pickle.dump(total_acc_list,open('total_acc','wb'))

pickle.dump(test_dict['0'],open('0_test_num','wb'))
pickle.dump(test_dict['1'],open('1_test_num','wb'))
pickle.dump(test_dict['2'],open('2_test_num','wb'))

pickle.dump(train_numm,open('train_num','wb'))

