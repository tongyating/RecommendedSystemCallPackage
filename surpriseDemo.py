import os
import surprise
import pandas as pd
from surprise import accuracy

##########第一部分、加载内置数据集#######################
#加载数据集
# data = surprise.Dataset.load_builtin('ml-100k')

####1.通过将数据集分成多份进行交叉验证
#一个基本的交叉验证迭代器。每一个折叠都作为一个测试集使用一次，而其余的k-1折叠是用于训练。
# kf = surprise.model_selection.KFold(n_splits=3)
#拆分数据集
# trainset,testset = surprise.model_selection.train_test_split(data,test_size=0.2)\
#通过k折交叉分数据集
# for trainset,testset in kf.split(data):
#     svd = surprise.SVD()
#     predictions = svd.fit(trainset).test(testset)
#     accuracy.rmse(predictions,verbose=True)

####2.使用整个数据集
#将整个算法用于整个的数据集，不用交叉验证
# trainset = data.build_full_trainset()
# svd = surprise.SVD()
# svd.fit(trainset)
# uid: (Raw) id of the user
# iid: (Raw) id of the item
# r_ui(float): The true rating
# verbose(bool): Whether to print details of the prediction
# pred = svd.predict(uid=196,iid=302,r_ui=4.00,verbose=True)
#################第一部分结束###########################



##################第二部分、加载自定义数据集#################

######1.加载文件
# file_path = os.path.expanduser('~/.surprise_data/ml-100k/ml-100k/u.data')
# reader = surprise.Reader(line_format='列名',sep='\t')
# data = surprise.Dataset.load_from_file(file_path,reader=reader)

#多个文件的状态
# files_dir = os.path.expanduser('~/.surprise_data/ml-100k/ml-100k/')
#name如果指定，则返回内置数据集之一的Reader，而忽略任何其他参数。可接受的值为“ ml-100k”，“ ml-1m”和“jester”。默认值为None。
# reader = surprise.Reader(name='ml-100k')
# train_file = files_dir + 'u%d.base'
# test_file = files_dir + 'u%d.test'
# folds_files = [(train_file%i,test_file%i) for i in (1,2,3,4,5)]
# data = surprise.Dataset.load_from_folds(folds_files,reader=reader)
#一种交叉验证迭代器，用于使用该load_from_folds 方法加载数据集
# pkf = surprise.model_selection.PredefinedKFold()
# svd = surprise.SVD()
# for trainset,testset in pkf.split(data):
#     predictions = svd.fit(trainset).test(testset)
#     accuracy.rmse(predictions,verbose=True)

#####2.加载df
# ratings_dict = {'itemID': [1, 1, 1, 2, 2],
#                 'userID': [9, 32, 2, 45, 'user_foo'],
#                 'rating': [3, 2, 4, 3, 1]}
# df = pd.DataFrame(ratings_dict)
# #可选参数,rating_scale用于每个评分的评分量表
# reader = surprise.Reader(rating_scale=(1,5))
# data = surprise.Dataset.load_from_df(df,reader=reader)
# per = surprise.model_selection.cross_validate(surprise.NormalPredictor(),data,cv=2)
# print(per)
#################第二部分结束#######################################



#################第三部分、GridSearchCV调整算法参数###################
#该cross_validate()功能针对​​一组给定的参数通过交叉验证过程报告准确性度量。如果您想知道哪种参数组合会产生最佳结果，则 GridSearchCV该类可以帮助您解决问题。
# data = surprise.Dataset.load_builtin('ml-100k')
#n_epochs迭代次数
# param_grid = {'n_epochs':[5,10],'lr_all':[0.002,0.005],'reg_all':[0.4,0.6]}
#param_grid（dict）：以算法参数为键和作为键的值列表。所有组合将用所需的算法
#cv（交叉验证迭代器，int或“None”）：数据将被拆分（即训练集和测试集将被定义），若为数字定义拆分的数据为几份，若为None，则调用的KFold使用默认参数
# gs = surprise.model_selection.GridSearchCV(algo_class=surprise.SVD,param_grid=param_grid,measures=['rmse','mae'],cv=3)
# gs.fit(data)
# print(gs.best_score)
# print(gs.best_params)
#根据最优参数集成算法实例
# algo = gs.best_estimator['rmse']
# algo.fit(data.build_full_trainset())
######################第三部分结束############################




