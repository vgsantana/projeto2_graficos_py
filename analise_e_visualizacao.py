import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r'data\ecommerce_estatistica.csv')
print(df.head().to_string())

# Analise e informacoes do df
print(df.info())
print(df.describe())

# Graficos para visualizacao

# Histograma 
plt.figure(figsize=(20,6))
sns.histplot(df['Preço'], bins=30, kde=True)
plt.title('Preços')
plt.show()

''' 
O Gráfico de Histograma nos permite perceber a precificacão dos produtos e onde ela está mais concentrada, podendo extrair daí o público alvo (segmentacão).
'''


# Grafico de densidade
generos_validos = df['Gênero'].value_counts()
generos_validos = generos_validos[generos_validos > 10].index
df_filtrado = df[df['Gênero'].isin(generos_validos)]
plt.figure(figsize=(10,6))
sns.kdeplot(data = df_filtrado, x='Preço', hue='Gênero', fill=True)
plt.title('Densidade de Preço por Gêneros')
plt.xlabel('Preço')
plt.show()

''' 
O Gráfico de Densidade nos mostra a variedade de precos por categoria, Algumas categorias foram excluídas por baixa representatividade estatística.
'''

# Barra
plt.figure(figsize=(20,6))
sns.barplot(data=df, x='Gênero', y='Qtd_Vendidos_Cod')
plt.title('Quantidade Média de Vendas por Gênero')
plt.show()

''' 
O Gráfico de Barra nos mostra a média de vendas por categoria.
'''

# Dispersao
plt.figure(figsize=(10,6))
sns.scatterplot(x='Preço', y='Desconto', alpha=0.4, data=df)
plt.title('Relação entre Preço do Produto e Desconto Aplicado')
plt.xlabel('Preço')
plt.ylabel('Desconto (%)')
plt.show()

''' 
O Gráfico de Dispersão aponta para descontos dados, o valor daos descontos por valor de produto, também importante para saber se tem impacto nas vendas.
'''

# Pizza
df['Avaliacoes'] = pd.cut(
    df['Nota'],
    bins=[0,2,3,4,5.1],
    labels=['Ruim (1-2)', 'Regular (3)', 'Bom (4)', 'Excelente (5)']
)

avaliacoes_por_faixa = df['Avaliacoes'].value_counts().sort_index()

plt.figure(figsize=(10,6))
plt.pie(
    avaliacoes_por_faixa,
    startangle=90
)
plt.legend(
    [f'{label}: {value:.1f}%' for label, value in 
     zip(avaliacoes_por_faixa.index,
         avaliacoes_por_faixa / avaliacoes_por_faixa.sum() * 100)],
    title='Faixa de Avaliação',
    loc='center left',
    bbox_to_anchor=(1, 0.5)
)

plt.title('Distribuicao das avaliacoes dos produtos')
plt.tight_layout()
plt.show()

''' 
O Gráfico de Pizza mostra a avaliacão dos produtos, para extrair a qualidade percebida pelos clientes, importante para saber se o produto
é capaz de fazer o cliente se fidelizar e recomendar para outras pessoas, o que impacta nas vendas.
'''

# Regressao
plt.figure(figsize=(10,6))
sns.regplot(
    x='Nota',
    y='Qtd_Vendidos_Cod',
    scatter_kws={'alpha': 0.3},
    line_kws={'color': 'red'},
    data=df
)
plt.title('Vendas por Nota')
plt.xlabel('Nota')
plt.ylabel('Quantidade de Vendas')
plt.show()

''' 
O Gráfico de Regressão análisa a qualidade do produto percebida pelo cliente e o impacto nas vendas.
'''

# Mapa de calor
df_corr =  df[['Qtd_Vendidos_Cod', 'Preço_MinMax', 'Desconto_MinMax', 'Nota_MinMax']].corr()
plt.figure(figsize=(10,6))
sns.heatmap(df_corr, annot=True, fmt='.2f')
plt.title('Mapa de calor da correlacao entre variáveis')
plt.show()

''' 
O Gráfico de calor nos mostra a correlacao entre as variáveis analisadas com o numero de vendas.
'''

