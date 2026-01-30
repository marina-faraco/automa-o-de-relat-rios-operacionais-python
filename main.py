import pandas as pd

def processar_relatorios():
    # Ler dados
    print('Lendo dados...')
    df = pd.read_csv('dados_hospitalares.csv')

    # Limpar espaços e valores nulos
    df['Setor'] = df['Setor'].str.strip()
    df['Custo_Real'] = df['Custo_Real'].fillna(0) # 'None' --> 0

    # Calcular variação do orçamento
    df['variacao'] = df['Custo_Real'] - df['Custo_Previsto']

    # Resumo por setor
    resumo = df.groupby('Setor')['Custo_Real'].sum().reset_index()

    # exportar
    resumo.to_excel('output/relatorio_final.xlsx', index=False)
    print("Relatório 'relatorio_final.xlsx' gerado com sucesso!")

if __name__=="__main__":
    processar_relatorios()