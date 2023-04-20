import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
pd.get_dummies(data)
data['whoAml_human'] = data['whaml'].map({'human': False, 'robot': True})
data['whoAml_robot'] = data['whaml'].map({'robot': True, 'human': False})
data.head()