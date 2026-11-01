import csv
from pathlib import Path
import matplotlib.pyplot as plt
arquivo = Path(__file__).with_name("dados_maquina.csv")

with open(arquivo, "r", encoding="utf-8") as dados:
    leitor = csv.DictReader(dados)
    registros = list(leitor)

temperaturas = [float(linha["temperatura_c"]) for linha in registros]
vibracoes = [float(linha["vibracao_mm_s"]) for linha in registros]
pressoes = [float(linha["pressao_bar"]) for linha in registros]

temperatura_inicial = temperaturas[0]
temperatura_final = temperaturas[-1]

vibracao_inicial = vibracoes[0]
vibracao_final = vibracoes[-1]

pressao_inicial = pressoes[0]
pressao_final = pressoes[-1]

aumento_temperatura = temperatura_final - temperatura_inicial
aumento_vibracao = vibracao_final - vibracao_inicial
queda_pressao = pressao_inicial - pressao_final

print("=== ANALISE DE MANUTENCAO PREDITIVA ===")
print()

print(f"Temperatura inicial: {temperatura_inicial:.1f} °C")
print(f"Temperatura final: {temperatura_final:.1f} °C")
print(f"Aumento da temperatura: {aumento_temperatura:.1f} °C")

print()

print(f"Vibracao inicial: {vibracao_inicial:.1f} mm/s")
print(f"Vibracao final: {vibracao_final:.1f} mm/s")
print(f"Aumento da vibracao: {aumento_vibracao:.1f} mm/s")

print()

print(f"Pressao inicial: {pressao_inicial:.1f} bar")
print(f"Pressao final: {pressao_final:.1f} bar")
print(f"Queda da pressao: {queda_pressao:.1f} bar")

print()

if temperatura_final >= 85 and vibracao_final >= 6:
    print("DIAGNOSTICO: RISCO ELEVADO DE FALHA")
    print("RECOMENDACAO: Programar inspecao e manutencao.")
else:
    print("DIAGNOSTICO: Operacao dentro dos limites.")
datas = [linha["data"] for linha in registros]

plt.figure(figsize=(10, 5))
plt.plot(datas, temperaturas, marker="o")
plt.axhline(y=85, linestyle="--", label="Limite crítico: 85 °C")
plt.legend()
plt.title("Evolução da Temperatura da Máquina")
plt.xlabel("Data")
plt.ylabel("Temperatura (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_temperatura.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(datas, vibracoes, marker="o")
plt.axhline(y=6, linestyle="--", label="Limite crítico: 6 mm/s")
plt.legend()
plt.title("Evolução da Vibração da Máquina")
plt.xlabel("Data")
plt.ylabel("Vibração (mm/s)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_vibracao.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(datas, pressoes, marker="o")
plt.axhline(y=4, linestyle="--", label="Limite mínimo: 4 bar")
plt.legend()
plt.title("Evolução da Pressão da Máquina")
plt.xlabel("Data")
plt.ylabel("Pressão (bar)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_pressao.png", dpi=300)
plt.show()

fig, axes = plt.subplots(3, 1, figsize=(12, 12))

# Temperatura
axes[0].plot(datas, temperaturas, marker="o")
axes[0].axhline(y=85, linestyle="--", label="Limite crítico: 85 °C")
axes[0].set_title("Temperatura da Máquina")
axes[0].set_ylabel("Temperatura (°C)")
axes[0].legend()
axes[0].grid(True)

# Vibração
axes[1].plot(datas, vibracoes, marker="o")
axes[1].axhline(y=6, linestyle="--", label="Limite crítico: 6 mm/s")
axes[1].set_title("Vibração da Máquina")
axes[1].set_ylabel("Vibração (mm/s)")
axes[1].legend()
axes[1].grid(True)

# Pressão
axes[2].plot(datas, pressoes, marker="o")
axes[2].axhline(y=4, linestyle="--", label="Limite mínimo: 4 bar")
axes[2].set_title("Pressão da Máquina")
axes[2].set_xlabel("Data")
axes[2].set_ylabel("Pressão (bar)")
axes[2].legend()
axes[2].grid(True)

axes[0].tick_params(labelbottom=False)
axes[1].tick_params(labelbottom=False)

plt.xticks(rotation=45)
for i, label in enumerate(axes[2].get_xticklabels()):
    if i % 2 != 0:
        label.set_visible(False)
fig.suptitle(
    "Painel de Monitoramento — Manutenção Preditiva",
    fontsize=16
)
fig.text(
    0.5,
    0.93,
    "STATUS: RISCO ELEVADO DE FALHA  |  Recomendação: Programar inspeção e manutenção",
    ha="center",
    fontsize=10,
    fontweight="bold"
)
plt.tight_layout(rect=[0, 0, 1, 0.89])
plt.savefig("painel_manutencao_preditiva.png", dpi=300)
plt.show()