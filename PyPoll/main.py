import pandas as pd 
df = pd.read_csv (r'/Users/jeffhitt/Desktop/JeffGitHW/python-challenge/PyPoll/Resources/election_data.csv')

new_df=df.groupby('Candidate')['Voter ID'].count().reset_index(name='Count').sort_values('Count',ascending=False)

new_df

new_df['Percent']=round(new_df.Count/new_df.Count.sum()*100,5)
new_df 

print('Election Results')
print('-------------------------')
print ('Total Votes:' ,df['Voter ID'].count())
print('-------------------------')
for index, row in new_df.iterrows():
    print (row['Candidate']+': ',str('%.3f'%row['Percent'])+'% ','('+str(row['Count'])+')')
print('-------------------------')
print('Winner: ', new_df['Candidate'][new_df['Percent'] == new_df['Percent'].max()].iloc[0])
print('-------------------------')


print('Election Results', file=open('output.txt', 'a'))
print('-------------------------', file=open('output.txt', 'a'))
print ('Total Votes:' ,df['Voter ID'].count(), file=open('output.txt', 'a'))
print('-------------------------', file=open('output.txt', 'a'))
for index, row in new_df.iterrows():
    print (row['Candidate']+': ',str('%.3f'%row['Percent'])+'% ','('+str(row['Count'])+')', file=open('output.txt', 'a'))
print('-------------------------', file=open('output.txt', 'a'))
print('Winner: ', new_df['Candidate'][new_df['Percent'] == new_df['Percent'].max()].iloc[0], file=open('output.txt', 'a'))
print('-------------------------', file=open('output.txt', 'a'))


