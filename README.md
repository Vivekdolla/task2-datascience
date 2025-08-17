# task2-datascience
First 5 rows: 
total_bill   tip     sex smoker  day    time  size 
0       16.99  1.01  Female     No  Sun  Dinner     2 
1       10.34  1.66    Male     No  Sun  Dinner     3 
2       21.01  3.50    Male     No  Sun  Dinner     3 
3       23.68  3.31    Male     No  Sun  Dinner     2 
4       24.59  3.61  Female     No  Sun  Dinner     4 
Dataset Info: 
<class 'pandas.core.frame.DataFrame'> 
RangeIndex: 244 entries, 0 to 243 
Data columns (total 7 columns): 
#   Column      Non-Null Count  Dtype    ---  ------      --------------  -----    
0   total_bill  244 non-null    float64  
1   tip        
2   sex        
 244 non-null    float64  
 244 non-null    category 
3   smoker      244 non-null    category 
4   day        
5   time        
6   size        
 244 non-null    category 
244 non-null    category 
244 non-null    int64    
dtypes: category(4), float64(2), int64(1) 
memory usage: 7.4 KB 
Summary Statistics: 
total_bill         
tip        
size 
count  244.000000  244.000000  244.000000 
mean    19.785943    2.998279    2.569672 
std      8.902412    1.383638    0.951100 
min      
3.070000    1.000000    1.000000 
25%     13.347500    2.000000    2.000000 
50%     17.795000    2.900000    2.000000 
75%     24.127500    3.562500    3.000000 
max     50.810000   10.000000    6.000000 
Central Tendency (total_bill) using NumPy: 
Mean: 19.78594262295082 
Median: 17.795 
Mode: 13.42 
Central Tendency (total_bill) using Pandas: 
Mean: 19.78594262295082 
Median: 17.795 
Mode: 13.42 
Gender Distribution: 
sex 
Male      157 
Female     87 
Name: count, dtype: int64 
Day Distribution: 
day 
Sat     87 
Sun     76 
Thur    62 
Fri     
19 
Name: count, dtype: int64 
Average Tip by Gender: 
sex 
Male      3.089618 
Female    2.833448 
Name: tip, dtype: float64 
Average Total Bill by Day: 
day 
Thur    17.682742 
Fri     
17.151579 
Sat     20.441379 
Sun     21.410000 
Name: total_bill, dtype: float64 
Correlation Matrix: 
total_bill      
 tip     
 size 
total_bill    1.000000  0.675734  0.598315 
tip          
size          
 0.675734  1.000000  0.489299 
0.598315  0.489299  1.000000
