[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2022/03/campus_marica.png)](https://universidadedevassouras.edu.br/campus-marica/)

# Engenharia de Software
### Leandro Loffeu Pereira Costa - mat. 202212089
### Inteligência Artificial e Machine Learning - 8º Período
### Professor: Tiago Ruiz

### Este projeto implementa um sistema de previsão de admissão universitária usando um modelo Keras pré-treinado.

## 📋 Funcionalidades

- ✅ Carregamento de modelo Keras pré-treinado
- ✅ Validação de entrada conforme regras de negócio
- ✅ Previsão individual interativa
- ✅ Previsão em lote via arquivo CSV
- ✅ Interface amigável com emojis e formatação
- ✅ Validação robusta de dados de entrada

## 🚀 Como Usar

### Pré-requisitos

```bash
pip install numpy pandas keras tensorflow
```

### Execução

1. **Executar o programa principal:**
   ```bash
   python previsao_admissao.py
   ```

2. **Teste rápido:**
   ```bash
   python teste_previsao.py
   ```

### Opções do Menu

1. **Previsão Individual**: Digite os valores manualmente
2. **Previsão em Lote**: Use um arquivo CSV com múltiplos registros
3. **Sair**: Encerra o programa

## 📊 Regras de Negócio

| Campo | Tipo | Intervalo | Descrição |
|-------|------|-----------|-----------|
| GRE Score | Inteiro | 260-340 | Pontuação no GRE |
| TOEFL Score | Inteiro | 0-120 | Pontuação no TOEFL |
| University Rating | Inteiro | 1-5 | Avaliação da universidade |
| SOP | Inteiro | 1-5 | Statement of Purpose |
| LOR | Inteiro | 1-5 | Letter of Recommendation |
| CGPA | Decimal | 0.0-10.0 | Média acumulada |
| Research | Inteiro | 0-1 | 0=Não, 1=Sim |

## 📁 Arquivos

- `previsao_admissao.py` - Programa principal
- `teste_previsao.py` - Script de teste
- `exemplo_dados.csv` - Dados de exemplo para teste em lote
- `modelo_treinado.keras` - Modelo pré-treinado (fornecido pelo professor)

## 🧪 Exemplo de Uso

### Entrada Individual
```
GRE Score (260-340): 312
TOEFL Score (0-120): 109
University Rating (1-5): 3
SOP (1-5): 3
LOR (1-5): 3
CGPA (0.0-10.0): 8.69
Research (0-1): 0
```

### Saída
```
📊 RESULTADO DA PREVISÃO
============================================================

📋 Características fornecidas:
   • GRE Score: 312
   • TOEFL Score: 109
   • University Rating: 3
   • SOP: 3
   • LOR: 3
   • CGPA: 8.69
   • Research: Não

🎯 Chance prevista de admissão: 68.00%
📈 Status: 🟡 MÉDIA - Boa chance de admissão
```

## 📈 Interpretação dos Resultados

- 🟢 **ALTA** (≥80%): Muito provável admissão
- 🟡 **MÉDIA** (60-79%): Boa chance de admissão
- 🟠 **BAIXA** (40-59%): Chance moderada de admissão
- 🔴 **MUITO BAIXA** (<40%): Pouca chance de admissão

## 🔧 Desafio Opcional - Previsão em Lote

Para usar a funcionalidade de previsão em lote, crie um arquivo CSV com as colunas:
`GRE Score,TOEFL Score,University Rating,SOP,LOR,CGPA,Research`

Exemplo:
```csv
GRE Score,TOEFL Score,University Rating,SOP,LOR,CGPA,Research
312,109,3,3,3,8.69,0
320,115,4,4,4,9.2,1
300,100,2,2,2,7.8,0
```

O programa gerará um arquivo `_resultados.csv` com as previsões adicionadas.

## ⚠️ Observações

- O arquivo `modelo_treinado.keras` deve estar no mesmo diretório do script
- Todos os valores de entrada são validados conforme as regras de negócio
- O programa suporta valores padrão para demonstração rápida
- Pressione Enter para usar valores de exemplo durante a entrada individual
