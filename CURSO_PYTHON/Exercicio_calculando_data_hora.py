# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, date
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000
data = datetime.strptime('20/12/2020',  '%d/%m/%Y')
qtd_anos = 5  #5 anos, cada ano tem 12 meses
valor_parcela = valor_emprestimo / (qtd_anos * 12)

data_final = data

for meses in range(qtd_anos * 12):
    
    meses_restantes = (qtd_anos * 12) - meses

    print( )
    print(f"Mês: {data.strftime('%m/%Y')}")
    print(f"Parcelamentos restantes: {meses_restantes}")
    print(f'Valor da parcela: R$ {valor_parcela:.2f} ')
    data_final += relativedelta(month=+1)




    










    

    




    
