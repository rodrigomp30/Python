import pandas as pd;

#criando dataframe
keywords = pd.read_csv('resources/keywords.csv')

#lista de palavras prodibidas
kws = ['crm', 'programa', 'plataforma', 'software', 'sistema', 'app', 'aplicativo',]
NotKws = ['zoho', 'zoro', 'rd', 'station', 'bitrix', 'piperun', 'pipedrive', 'moskit', 
          'guincho', 'eleva', 'instagram', 'loja', 'estoque', 'digital', 'digitais', 'assistencia', 
          'foto', 'max', 'olx', 'curso', 'grupo', 'caixa', 'apple', 'iphone', 'afiliado', 'garota', 'carro', 'caminhão', 
          'hair', 'ebook']

#filtrando keywords
KwsImportantes = keywords[keywords['Keyword'].str.contains('|'.join(kws)) & ~keywords['Keyword'].str.contains('|'.join(NotKws))]


# See the result
print(KwsImportantes)
#KwsImportantes.to_csv('resources/kw-filtradas.csv')