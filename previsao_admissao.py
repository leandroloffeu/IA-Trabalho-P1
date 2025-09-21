
"""
Este programa carrega um modelo Keras pré-treinado e faz previsões de admissão
baseadas nas características fornecidas pelo usuário.
"""

import numpy as np
import pandas as pd
from keras.models import load_model
import os
import csv

def validar_entrada(valor, tipo, min_val, max_val, nome_campo):
    """
    Valida a entrada do usuário conforme as regras de negócio.
    
    Args:
        valor: Valor a ser validado
        tipo: Tipo esperado ('int' ou 'float')
        min_val: Valor mínimo permitido
        max_val: Valor máximo permitido
        nome_campo: Nome do campo para mensagens de erro
    
    Returns:
        Valor validado ou None se inválido
    """
    try:
        if tipo == 'int':
            valor = int(valor)
        elif tipo == 'float':
            valor = float(valor)
        
        if min_val <= valor <= max_val:
            return valor
        else:
            print(f"❌ {nome_campo} deve estar entre {min_val} e {max_val}")
            return None
    except ValueError:
        print(f"❌ {nome_campo} deve ser um número válido")
        return None

def solicitar_entrada_usuario():
    """
    Solicita e valida as características do usuário.
    
    Returns:
        Lista com os valores validados ou None se houver erro
    """
    print("\n" + "="*60)
    print("🎓 SISTEMA DE PREVISÃO DE ADMISSÃO UNIVERSITÁRIA")
    print("="*60)
    print("\nPor favor, forneça as seguintes informações:")
    print("(Pressione Enter para usar valores padrão de exemplo)\n")
    

    colunas = ["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]
    

    validacoes = [
        ("GRE Score", "int", 260, 340),
        ("TOEFL Score", "int", 0, 120),
        ("University Rating", "int", 1, 5),
        ("SOP", "int", 1, 5),
        ("LOR", "int", 1, 5),
        ("CGPA", "float", 0.0, 10.0),
        ("Research", "int", 0, 1)
    ]
    
   
    valores_padrao = [312, 109, 3, 3, 3, 8.69, 0]
    
    valores = []
    
    for i, (campo, tipo, min_val, max_val) in enumerate(validacoes):
        while True:
            try:
                entrada = input(f"{campo} ({min_val}-{max_val}): ").strip()
                
              
                if not entrada:
                    valor = valores_padrao[i]
                    print(f"   → Usando valor padrão: {valor}")
                    valores.append(valor)
                    break
                
              
                valor = validar_entrada(entrada, tipo, min_val, max_val, campo)
                if valor is not None:
                    valores.append(valor)
                    break
                    
            except KeyboardInterrupt:
                print("\n\n❌ Operação cancelada pelo usuário.")
                return None
    
    return valores

def carregar_modelo():
    """
    Carrega o modelo Keras pré-treinado.
    
    Returns:
        Modelo carregado ou None se houver erro
    """
    try:
        if not os.path.exists('modelo_treinado.keras'):
            print("❌ Erro: Arquivo 'modelo_treinado.keras' não encontrado!")
            print("   Certifique-se de que o arquivo está no mesmo diretório do script.")
            return None
        
        print("🔄 Carregando modelo pré-treinado...")
        modelo = load_model('modelo_treinado.keras')
        print("✅ Modelo carregado com sucesso!")
        return modelo
        
    except Exception as e:
        print(f"❌ Erro ao carregar o modelo: {e}")
        return None

def fazer_previsao(modelo, valores):
    """
    Faz a previsão usando o modelo carregado.
    
    Args:
        modelo: Modelo Keras carregado
        valores: Lista com os valores de entrada
    
    Returns:
        Probabilidade de admissão (0.0 a 1.0)
    """
    try:
      
        entrada_array = np.array(valores).reshape(1, -1)
        
        print("\n🔄 Gerando previsão...")
        previsao = modelo.predict(entrada_array, verbose=0)
        
      
        probabilidade = previsao[0][0]
        
        return probabilidade
        
    except Exception as e:
        print(f"❌ Erro ao fazer previsão: {e}")
        return None

def exibir_resultado(valores, probabilidade):
    """
    Exibe o resultado final formatado.
    
       valores: Lista com os valores de entrada
        probabilidade: Probabilidade de admissão
    """
    colunas = ["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]
    
    print("\n" + "="*60)
    print("📊 RESULTADO DA PREVISÃO")
    print("="*60)
    
    print("\n📋 Características fornecidas:")
    for i, (coluna, valor) in enumerate(zip(colunas, valores)):
        if coluna == "Research":
            valor_display = "Sim" if valor == 1 else "Não"
        elif coluna == "CGPA":
            valor_display = f"{valor:.2f}"
        else:
            valor_display = str(valor)
        print(f"   • {coluna}: {valor_display}")
    
    print(f"\n🎯 Chance prevista de admissão: {probabilidade:.2%}")
    

    if probabilidade >= 0.8:
        status = "🟢 ALTA - Muito provável admissão"
    elif probabilidade >= 0.6:
        status = "🟡 MÉDIA - Boa chance de admissão"
    elif probabilidade >= 0.4:
        status = "🟠 BAIXA - Chance moderada de admissão"
    else:
        status = "🔴 MUITO BAIXA - Pouca chance de admissão"
    
    print(f"📈 Status: {status}")

def previsao_lote_csv(modelo, nome_arquivo):
    """
    Função para previsão em lote usando arquivo CSV (desafio opcional).
    
    Args:
        modelo: Modelo Keras carregado
        nome_arquivo: Nome do arquivo CSV
    """
    try:
        print(f"\n🔄 Processando arquivo CSV: {nome_arquivo}")
        
      
        df = pd.read_csv(nome_arquivo)
        
      
        colunas_necessarias = ["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]
        
        if not all(col in df.columns for col in colunas_necessarias):
            print("❌ Erro: Arquivo CSV deve conter as colunas:")
            for col in colunas_necessarias:
                print(f"   • {col}")
            return
        
        print(f"✅ Arquivo carregado com {len(df)} registros")
        
       
        resultados = []
        for idx, row in df.iterrows():
            valores = [row[col] for col in colunas_necessarias]
            entrada_array = np.array(valores).reshape(1, -1)
            previsao = modelo.predict(entrada_array, verbose=0)
            probabilidade = previsao[0][0]
            resultados.append(probabilidade)
        
 
        df['Chance_Admissao'] = resultados
        df['Chance_Admissao_Percentual'] = [f"{p:.2%}" for p in resultados]
        
    
        nome_saida = nome_arquivo.replace('.csv', '_resultados.csv')
        df.to_csv(nome_saida, index=False)
        
        print(f"✅ Resultados salvos em: {nome_saida}")
        
    
        print(f"\n📊 Resumo das previsões:")
        print(f"   • Média de chance de admissão: {np.mean(resultados):.2%}")
        print(f"   • Maior chance: {np.max(resultados):.2%}")
        print(f"   • Menor chance: {np.min(resultados):.2%}")
        
    except Exception as e:
        print(f"❌ Erro ao processar CSV: {e}")

def main():
    """
    Função principal do programa.
    """
    print("🎓 SISTEMA DE PREVISÃO DE ADMISSÃO UNIVERSITÁRIA")
    print("Desenvolvido para o Trabalho P1")
    
  
    modelo = carregar_modelo()
    if modelo is None:
        return
    
    while True:
        print("\n" + "="*60)
        print("📋 MENU PRINCIPAL")
        print("="*60)
        print("1. Fazer previsão individual")
        print("2. Previsão em lote (CSV)")
        print("3. Sair")
        
        try:
            opcao = input("\nEscolha uma opção (1-3): ").strip()
            
            if opcao == "1":
                
                valores = solicitar_entrada_usuario()
                if valores is None:
                    continue
                
                probabilidade = fazer_previsao(modelo, valores)
                if probabilidade is not None:
                    exibir_resultado(valores, probabilidade)
            
            elif opcao == "2":
            
                nome_arquivo = input("\nDigite o nome do arquivo CSV: ").strip()
                if nome_arquivo and os.path.exists(nome_arquivo):
                    previsao_lote_csv(modelo, nome_arquivo)
                else:
                    print("❌ Arquivo não encontrado!")
            
            elif opcao == "3":
                print("\n👋 Obrigado por usar o sistema! Até logo!")
                break
            
            else:
                print("❌ Opção inválida! Escolha 1, 2 ou 3.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Programa encerrado pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
