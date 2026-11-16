# === DADOS DE ENTRADA (FCTÍCIOS) ===

cliente_nome = "Ayla (Fictício)"
servico = "Massoterapia Relaxante"
valor_sessao = 120.00
quantidade_sessoes = 3
alerta_saude = True # Apenas indica se há pós-operatório/dor aguda(Minimização LGPD)

# === PROCESSAMENTO ===
valor_total = valor_sessao * quantidade_sessoes

# === SAÍDA ===
print("--- RESUMO DO ORÇAMENTO ---")
print(f"Cliente: {cliente_nome}")
print(f"Serviço: {servico}")
print(f"Quantidade: {quantidade_sessoes} sessões")
print(f"Total sem desconto: R$ {valor_total:.2f}")  # :.2f formata com 2 casas decimais
print(f"Requer triagem prévia da profissional? {alerta_saude}")


# === DADOS DE ENTRADA (FCTÍCIOS) ===
nome_cliente = "Benjamin (Fictício)"
tipo_servico = 'SPA de pés'
valor_unitario = 85.50
sessoes_quantidade = 4
desconto_10 = 0.10
status_saude = False

# === PROCESSAMENTO ===
valor_total_servico = valor_unitario * sessoes_quantidade
valor_com_desconto = valor_total_servico - (sessoes_quantidade * desconto_10)
# === SAÍDA ===
print("--- RESUMO DO ORÇAMENTO ---")
print(f"Cliente: {nome_cliente}")
print(f"Serviço: {tipo_servico}")
print(f"Quantidade: {sessoes_quantidade} sessões")
print(f"Total sem desconto: R$ {valor_total_servico:.2f}")  # :.2f formata com 2 casas decimais
print(f"Total com desconto: R$ {valor_desconto_fixo:.2f}")  # :.2f formata com 2 casas decimais
print(f"Requer triagem prévia da profissional? {status_saude}")