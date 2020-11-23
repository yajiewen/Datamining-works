import numpy as np
import pickle
import matplotlib.pyplot as plt
train_num = pickle.load(open('train_num','rb'))
train_num
test_num_0 = pickle.load(open('0_test_num','rb'))
test_num_1 = pickle.load(open('1_test_num','rb'))
test_num_2 = pickle.load(open('2_test_num','rb'))
acc_0 = pickle.load(open('0_acc','rb'))
acc_1 = pickle.load(open('1_acc','rb'))
acc_2 = pickle.load(open('2_acc','rb'))
total_acc = pickle.load(open('total_acc','rb'))

fig = plt.figure()
pt1 = fig.add_subplot(111)

plt.xticks(fontsize=20) #x轴字体大小
plt.yticks(fontsize=20) #y轴字体大小

# plt.tick_params(labelsize=25)
pt1.set_title('',fontdict={'weight':'normal','size': 30})
pt1.set_xlabel('Number of train samples',fontdict={'weight':'normal','size': 30})
pt1.set_ylabel('Accuracy',fontdict={'weight':'normal','size': 30})

pt1.plot(train_num,acc_0,color = 'limegreen',linestyle='-',linewidth=3,label = "0_accuracy")
pt1.plot(train_num,acc_1,color = 'darkorange',linestyle='-',linewidth=3,label = "1_accuracy")
pt1.plot(train_num,acc_2,color = 'dodgerblue',linestyle='-',linewidth=3,label = "2_accuracy")
pt1.plot(train_num,total_acc,color = 'black',linestyle='-',linewidth=3,label = "total_accuracy")

plt.legend(loc='upper left',fontsize= 15)

pt2 = pt1.twinx()
plt.yticks(fontsize=20)
pt2.set_ylabel('Number of test samples',fontdict={'weight':'normal','size': 30})
pt2.plot(train_num,test_num_0,color = 'limegreen',linestyle='--',linewidth=3,label = "0_test_num")
pt2.plot(train_num,test_num_1,color = 'darkorange',linestyle='--',linewidth=3,label = "1_test_num")
pt2.plot(train_num,test_num_2,color = 'dodgerblue',linestyle='--',linewidth=3,label = "2_test_num")
plt.legend(loc='lower right',fontsize= 15)

plt.show()