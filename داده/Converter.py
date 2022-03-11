import pandas as pd 
fn ='tweets.csv'
File1 =pd.read_csv(fn , sep=',' , quoting=1,encoding='utf-8' ,low_memory=False)
File1.to_csv('export_'+fn, sep ='~' ,quotechar='"' ,quoting =1 , encoding ='utf-8')
