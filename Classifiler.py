from feature_extractor import *
from get_options import get_opt
from sklearn.ensemble import RandomForestClassifier

data_list = get_data()

opts = get_opt()
print(opts)

data_dict = {
    'train_features':[],
    'train_lables':[],
    'test_features':[],
    'test_lables':[],

}

for sample_name in ['0','1','2']:
    count_num = 0
    num_train=0
    num_test=0
    for sample in data_list[sample_name]:
        sample_features = []
        #获得特征
        sample_features.extend(client_to_server_time_features(sample[:]))
        sample_features.extend(server_to_client_time_features(sample[:]))
        sample_features.extend(client_to_client_time_features(sample[:]))
        sample_features.extend(server_to_server_time_features(sample[:]))
        sample_features.extend(packet_to_packet_time_features(sample[:]))
        if count_num < int(opts['train_num']):
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

#训练分类器
RFC=RandomForestClassifier(n_jobs=-1, n_estimators=1000, oob_score=True)
RFC.fit(data_dict['train_features'],data_dict['train_lables'])

Out_lables = RFC.predict(data_dict['test_features'])

#计算准确率
right_num = 0
for Out_lable,In_lables in zip(Out_lables,data_dict['test_lables']):
    if Out_lable == In_lables:
        right_num+=1
print('Accuracy :{}'.format(right_num/len(Out_lables)))




