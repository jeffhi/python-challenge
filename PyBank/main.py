
import pandas as pd 
df = pd.read_csv (r'/Users/jeffhitt/Desktop/JeffGitHW/python-challenge/PyBank/Resources/budget_data.csv')

count1 = df['Date'].count()
sum1 = df['Profit/Losses'].sum()
df['Profit/Loss_Shifted']=df['Profit/Losses'].shift(1)
df['Change']=df['Profit/Losses']-df['Profit/Loss_Shifted']
mean1 = df['Change'].mean()
print('Financial Analysis')
print('----------------------------')
print ('Count of Months: '+str(count1))
print ('Total: $'+str(sum1))
print('Average Change: $'+str(round(mean1,2)))
print('Greatest Increase in Profits: ' +df['Date'][df['Change'] == df['Change'].max()].iloc[0]+ ' ($'+str(int(df['Change'].max()))+')')
print('Greatest Increase in Profits: ' +df['Date'][df['Change'] == df['Change'].min()].iloc[0]+ ' ($'+str(int(df['Change'].min()))+')')


print('Financial Analysis', file=open('output.txt', 'a'))
print('----------------------------', file=open('output.txt', 'a'))
print ('Count of Months: '+str(count1), file=open('output.txt', 'a'))
print ('Total: $'+str(sum1), file=open('output.txt', 'a'))
print('Average Change: $'+str(round(mean1,2)), file=open('output.txt', 'a'))
print('Greatest Increase in Profits: ' +df['Date'][df['Change'] == df['Change'].max()].iloc[0]+ ' ($'+str(int(df['Change'].max()))+')', file=open('output.txt', 'a'))
print('Greatest Increase in Profits: ' +df['Date'][df['Change'] == df['Change'].min()].iloc[0]+ ' ($'+str(int(df['Change'].min()))+')', file=open('output.txt', 'a'))







