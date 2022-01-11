import pandas as pd

pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports = pd.read_csv('test/sports.csv')
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

common = pd.concat([general, prenatal, sports], ignore_index=True)
common.drop(columns=['Unnamed: 0'], inplace=True)

col_count = common.shape[1]
row_count = common.shape[0]

common_null = common.isnull().sum(axis=1)
for i in range(row_count):
    if common_null.iloc[i] == col_count:
        common.drop(index=i, inplace=True)

row_count = common.shape[0]

for i in range(row_count):
    if common.iloc[i, 1] in ('male', 'man'):
        common.iloc[i, 1] = 'm'
    else:
        common.iloc[i, 1] = 'f'

common['bmi'].fillna(0, inplace=True)
common['diagnosis'].fillna(0, inplace=True)
common['blood_test'].fillna(0, inplace=True)
common['blood_test'].fillna(0, inplace=True)
common['ultrasound'].fillna(0, inplace=True)
common['mri'].fillna(0, inplace=True)
common['xray'].fillna(0, inplace=True)
common['children'].fillna(0, inplace=True)
common['months'].fillna(0, inplace=True)

# 1 question
# Which hospital has the highest number of patients?
df = common
df_count = df[['gender', 'hospital']].groupby('hospital').count()
df_count_max = df_count.max()['gender']
df_1 = df_count[df_count['gender'] == df_count_max]
print(f"The answer to the 1st question is {df_1.index[0]}")

# 2 question
# What share of the patients in the general hospital suffers from stomach-related issues?
# Round the result to the third decimal place.

df_general = common[common['hospital'] == 'general']
df_general_stomach = df_general[df_general['diagnosis'] == 'stomach']
answer2 = round(df_general_stomach.count().iloc[0] / df_general.count().iloc[0], 3)
# print(df_general_stomach.count().iloc[0])
# print(df_general.count().iloc[0])
print(f'The answer to the 2nd question is {answer2}')

# 3 question
# What share of the patients in the sports hospital suffers from dislocation-related issues?
# Round the result to the third decimal place.
df_sports = common[common['hospital'] == 'sports']
df_sports_dislocation = df_sports[df_sports['diagnosis'] == 'dislocation']
answer2 = round(df_sports_dislocation.count().iloc[0] / df_sports.count().iloc[0], 3)
print(f'The answer to the 3nd question is {answer2}')

# 4 question
# What is the difference in the median ages of the patients in the general and sports hospitals?
dif = int(df_general['age'].median()- df_sports['age'].median())
print(f'The answer to the 4th question is {dif}')

# 5 question
#  In which hospital the blood test was taken the most often
#  (there is the biggest number of t in the blood_test column among all the hospitals)?
#  How many blood tests were taken?
df2 = df[['hospital', 'blood_test']]
pt = df.pivot_table(index='hospital', columns='blood_test', aggfunc='count')['age']
pt = pt.fillna(0)
pt_max = pt['t'].max()
pt_5 = pt[pt['t'] == pt_max]
print(f'The answer to the 5th question is {pt_5.index[0]}, {pt_max} blood tests')

# # 6 question
# # What is the most common age of a patient among all hospitals?
# common['age'].plot(kind='hist', bins=5)
# plt.show()
# print(f'The answer to the 1st question: 15-35')
#
# # 7 question
# # What is the most common diagnosis among patients in all hospitals?
#
# # print(common.groupby('diagnosis').count().iloc[::,0])
# common.groupby('diagnosis').count().iloc[::,0].plot()
# # common['diagnosis'].count().plot(y='diagnosis', kind='pie')
# plt.show()
# print(f'The answer to the 1st question: pregnancy')
#
#
# # 8 question
# sns.set_theme(style="whitegrid")
# # tips = sns.load_dataset(common)
# ax = sns.violinplot(x=common["height"])
# plt.show()
#
# print(f'The answer to the 3rd question: It\'s because of something')