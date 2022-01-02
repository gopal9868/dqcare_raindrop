def final_df_convert(df,pk_column):
    #df['pk_id']=''
    pk_column_list=pk_column.split(',')
    df=df.applymap(str)
    df['pk_id']=df[pk_column_list].agg('~'.join, axis=1)
    df = df.drop(columns=pk_column_list)
    #print("here you come")
    #print(df)
    return df
