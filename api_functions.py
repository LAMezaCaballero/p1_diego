#Importing the libraries
import pandas as pd


#Getting the data
df_games=pd.read_parquet(r"./Data/games_cleaned2.parquet")

df_items=pd.read_parquet(r"./Data/items_cleaned.parquet")
df_reviews=pd.read_parquet(r"./Data/reviews_cleaned2.parquet")
df_greviews=pd.read_parquet(r"./Data/g_reviews2.parquet")
#unir los datos de  gitems_cleaned porque no cabian todos

p1=pd.read_parquet(r"./Data/gitems_cleaned1.parquet")
p2=pd.read_parquet(r"./Data/gitems_cleaned2.parquet")
p3=pd.read_parquet(r"./Data/gitems_cleaned3.parquet")
#p4=pd.read_parquet(r"./Data/gitems_cleaned4.parquet")
#p5=pd.read_parquet(r"./Data/gitems_cleaned5.parquet")
df_gitems= pd.concat([p1,p2], ignore_index= True)#,p3,p4,p5
#restablecer los índices del DataFrame resultante
df_gitems.reset_index(drop=True, inplace=True)


#Functions


def developer(desarrollador: str):

  df_dev=df_games[df_games["developer"]==desarrollador][["year","id","price"]]

  grouped_data = df_dev.groupby('year')
  unique_id_count = grouped_data['id'].nunique()
  zero_price_percentage = grouped_data.apply(lambda group: str(round((group['price'] == 0).mean() * 100))+"%")

  result_df = pd.DataFrame({
    'Cantidad de items': unique_id_count,
    'Contenido Free': zero_price_percentage
    }).reset_index()
  #convertir en dict/json
  result_dict = result_df.to_dict(orient='records')
    
  return result_dict


def userdata(user_id: str):

  df_user=df_greviews[df_greviews["user_id"]==user_id][["price","item_id","recommend"]]

  total_money=str(round(df_user["price"].sum()))+" "+"USD"
  items_count=df_user["item_id"].nunique()
  recommend=str(round(((df_user["recommend"].sum()*100)/len(df_user["recommend"]))))+"%"
  result={"UserX":user_id,"Dinero gastado":total_money,"% de recomendacion":recommend,"Cantidad de items": items_count}

  return result


def userForGenre(genero: str):

  df_gen=df_gitems[df_gitems["genres"]==genero][["user_id","hours_game","year"]]

  df_use_gen=df_gen.groupby("user_id")["hours_game"].sum().reset_index()
  df_use_gen.sort_values(by=["hours_game"],ascending=False,inplace=True,ignore_index=True)

  user=df_use_gen.iloc[0,0]
  df_user=df_gen[df_gen["user_id"]==user]

  df_user_final=df_user.groupby("year")["hours_game"].sum().reset_index()
  df_user_final["hours_game"]=df_user_final["hours_game"].round()
  df_user_final.rename(columns={"year":"Año","hours_game":"Horas"},inplace=True)
  hours=[]
  for i in range(len(df_user_final)):
     hours.append(df_user_final.iloc[i].to_dict())

  return {f"Usuario con mas horas jugadas para genero {genero}":user,"Horas jugadas":hours}


def best_developer_year(year: int):

  df_dev=df_greviews[df_greviews["year"]==year][["developer","sentiment_analysis"]]

  df_sen_an=df_dev[df_dev["sentiment_analysis"]==2]
  df_recommend=df_sen_an.groupby("developer")["sentiment_analysis"].count().reset_index()

  df_recommend.sort_values(by=["sentiment_analysis"],ascending=False,inplace=True,ignore_index=True)
  final_series=df_recommend.iloc[:3,0]

  return {"Puesto 1":final_series[0],"Puesto 2":final_series[1],"Puesto 3":final_series[2]}


def developer_reviews_analysis(desarrolladora: str):
  df_dev_rev=df_greviews[df_greviews["developer"]==desarrolladora]

  dev_rev_new=df_dev_rev["sentiment_analysis"].value_counts().reset_index()

  if not (dev_rev_new['index'] == 0).any():
    dev_rev_new = pd.concat([dev_rev_new, pd.DataFrame({'index': [0], 'sentiment_analysis': [0]})], ignore_index=True)
  if not (dev_rev_new['index'] == 1).any():
    dev_rev_new = pd.concat([dev_rev_new, pd.DataFrame({'index': [1], 'sentiment_analysis': [0]})], ignore_index=True)
  if not (dev_rev_new['index'] == 2).any():
    dev_rev_new = pd.concat([dev_rev_new, pd.DataFrame({'index': [2], 'sentiment_analysis': [0]})], ignore_index=True)
  dev_rev_new.sort_values(by=["index"],inplace=True,ignore_index=True)
  positive=dev_rev_new.iloc[1,1]
  negative=dev_rev_new.iloc[0,0]

  return {f"{desarrolladora}:[Negativos:{negative}, Positivos:{positive}]"}

  
