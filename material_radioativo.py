massa = float(input("Digite a massa inicial: "))
tempo = 0  
while massa > 0.5 or massa == 0.5:
    massa = massa / 2
    tempo = tempo + 50
massa_final = massa
h = tempo // 3600
m = (tempo % 3600) // 60
s = tempo % 60
print(f"Massa final: {massa_final:.2f} g")
print(f"{int(h)}h {int(m)}m {int(s)}s")