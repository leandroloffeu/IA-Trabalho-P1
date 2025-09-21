
"""
Script de teste para demonstrar o funcionamento do sistema de previsão de admissão.
"""

import numpy as np
from keras.models import load_model
import os

def teste_rapido():
    """
    Teste rápido com valores de exemplo para verificar se o modelo funciona.
    """
    print("🧪 TESTE RÁPIDO DO SISTEMA")
    print("="*40)
    
    
    if not os.path.exists('modelo_treinado.keras'):
        print("❌ Modelo não encontrado!")
        return
    
    try:
        
        print("🔄 Carregando modelo...")
        modelo = load_model('modelo_treinado.keras')
        print("✅ Modelo carregado!")
        
       
        valores_exemplo = [312, 109, 3, 3, 3, 8.69, 0]
        colunas = ["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]
        
        print("\n📋 Valores de teste:")
        for col, val in zip(colunas, valores_exemplo):
            if col == "Research":
                val_display = "Sim" if val == 1 else "Não"
            elif col == "CGPA":
                val_display = f"{val:.2f}"
            else:
                val_display = str(val)
            print(f"   • {col}: {val_display}")
        
     
        print("\n🔄 Fazendo previsão...")
        entrada_array = np.array(valores_exemplo).reshape(1, -1)
        previsao = modelo.predict(entrada_array, verbose=0)
        probabilidade = previsao[0][0]
        
        print(f"\n🎯 Resultado:")
        print(f"   Chance prevista de admissão: {probabilidade:.2%}")
        
  
        if probabilidade >= 0.8:
            status = "🟢 ALTA"
        elif probabilidade >= 0.6:
            status = "🟡 MÉDIA"
        elif probabilidade >= 0.4:
            status = "🟠 BAIXA"
        else:
            status = "🔴 MUITO BAIXA"
        
        print(f"   Status: {status}")
        print("\n✅ Teste concluído com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")

if __name__ == "__main__":
    teste_rapido()

