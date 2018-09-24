import pandas as pd
from sklearn import preprocessing


input_data = pd.read_csv('data/iris.csv', header=None)

cls_df = pd.DataFrame(input_data[4].tolist())
# cls_df.columns = ['classes']
# cls_df['classes'] = cls_df['classes'].apply(lambda x: 'Class '+str(x))
# cls_df.to_csv('data/iris.labels.csv', index=None, header=None)

data_df = input_data
del data_df[4]
# del data_df[17]

# Normalize the data
x = data_df.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
data_df_scaled = pd.DataFrame(x_scaled)

data_df_scaled.to_csv('data/iris.data.csv', index=None, header=None)

print('Done')


