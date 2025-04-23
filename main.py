import psutil
# biblioteca para verificar informacoes do sistema
import matplotlib.pyplot as plt
#animacao da escala
from matplotlib.animation import FuncAnimation


#configurando o grafico

fig, ax = plt.subplots()
ax.set_ylim(0, 100)
ax.set_xlim(0,100)
ax.set_title('Uso da CPU e da Memória')
ax.set_xlabel('Tempo')
ax.set_ylabel('Uso (%)')
cpu_line, = ax.plot([], [], label ='CPU', color = '#FF5733')
memoria_line, = ax.plot([], [], label = 'Memória', color = '#C70039')
ax.legend()

#adicionando textos aos valores da CPU e memória

cpu_text = ax.text(0.77, 0.7, '', transform = ax.transAxes)
memoria_text = ax.text(0.77, 0.6, '', transform = ax.transAxes)

#func do grafico

def update_chart(frame):
    cpu_percent = psutil.cpu_percent()
    #cpu

    memoria = psutil.virtual_memory()
    memoria_percent = memoria.percent
    #memoria

    cpu_line.set_data(list(range(frame)),[cpu_percent]*frame)
    memoria_line.set_data(list(range(frame)),[memoria_percent]*frame)

    cpu_text.set_text(f'CPU: {cpu_percent: .1f}%')
    memoria_text.set_text(f'Memória: {memoria_percent: .1f}%')

    return cpu_line, memoria_line, cpu_text, memoria_text

#estilizando o gráfico

animation = FuncAnimation(fig, update_chart, frames=100, interval=1000, blit=True)

for line in [cpu_line, memoria_line]:
    line.set_linewidth(2)
    line.set_marker('o')
    line.set_markersize(5)

ax.set_facecolor('#F5F5F5')

plt.show()