import pandas as pd

data = {
    'Data': ['2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02', '2023-10-02'],
    'Setor': ['Pediatria', '  UTI  ', 'Pediatria', 'Cardiologia', 'UTI'],
    'Paciente': ['Ana Silva', 'Bruno Costa', 'Carlos Oliveira', 'Daniela Lima', 'Eduardo Souza'],
    'Custo_Real': [1200.50, 5000.00, 850.00, 3200.00, None], # None --> simulação de erro
    'Custo_Previsto': [1000, 4500, 1000, 3000, 4000]
    }

df = pd.DataFrame(data)
df.to_csv('output/dados_hospitalares.csv', index=False)
print("Arquivo 'dados_hospitalares.cvs criado com sucesso!")