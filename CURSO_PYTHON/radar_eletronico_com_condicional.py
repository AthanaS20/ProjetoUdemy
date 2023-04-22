"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

# Dessa forma o código ficou grande e confuso
if velocidade > RADAR_1:
    print('O Carro passou da velocidade max permitida')
if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
     local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
     print('O Carro foi multado ao passar no radar 1.') 

# Forma correta para limpar o código:
velocidade_carro_passou_no_radar = velocidade > RADAR_1
carro_multado_no_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
     local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade_carro_passou_no_radar # Você deve criar variaveis completas para entender depois

if velocidade_carro_passou_no_radar:
    print('O carro passou da velocidade máx permitida.')
if carro_multado_no_radar_1:
    print('O carro foi multado no radar 1.')

