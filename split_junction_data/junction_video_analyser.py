import pandas as pd


filename = 'C:/Users/pc/Desktop/JunctionDS/Annotations_num.txt'
outfile = 'C:/Users/pc/Desktop/JunctionDS/ground_truth.csv'
train_file = 'C:/Users/pc/Desktop/JunctionDS/train_clips.csv'

content = ''

with open(filename, 'r') as f:
    content = f.read().split('\n')

rows = []
for idx, line in enumerate(content):
    row = line.split('. ')[1].split('\t')[0].rstrip()

    s_min = int(row.split(':')[0])
    s_sec = int(row.split(':')[1].split(' - ')[0])
    s_time = int(s_min*60 + s_sec)

    e_min = int(row.split(' - ')[1].split(':')[0])
    e_sec = int(row.split(':')[-1])
    e_time = int(e_min*60 + e_sec)

    rows.append([s_min, s_sec, e_min, e_sec, s_time, e_time])


max_diff = 0
min_diff = 10000
for i in range(1, len(rows)):

    if max_diff < (rows[i][-2] - rows[i-1][-1]):
        max_diff = (rows[i][-2] - rows[i-1][-1])

    if min_diff > (rows[i][-2] - rows[i-1][-1]):
        min_diff = (rows[i][-2] - rows[i-1][-1])

    print(i, min_diff)

df = pd.DataFrame(rows, columns=['start_min', 'start_sec', 'end_min', 'end_sec', 'start_time', 'end_time'])

df['frame_start'] = df['start_min'] * 1500 + df['start_sec'] * 25 - 1
df['frame_end'] = df['end_min'] * 1500 + df['end_sec'] * 25 + 1

df.to_csv(outfile, index=None)

train_rows = []
for index, row in df.iterrows():

    if index == 0:
        train_rows.append([1, df.iloc[index]['frame_start']-1])
    else:
        train_rows.append([df.iloc[index-1]['frame_end']+1, df.iloc[index]['frame_start']-1])

df_train = pd.DataFrame(train_rows, columns=['frame_start', 'frame_end'])
df_train.to_csv(train_file)
