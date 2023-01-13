idade_em_dias = int(input())

idade_y = int(idade_em_dias/365)
print(f'{idade_y} ano(s)')
idade_em_dias_restante = idade_em_dias % 365

idade_m = int(idade_em_dias_restante/30)
print(f'{idade_m} mes(es)')
idade_em_dias_restante = idade_em_dias_restante % 30

print(f'{idade_em_dias_restante} dia(s)')
