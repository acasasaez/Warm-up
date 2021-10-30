import random
import seaborn as sns
import matplotlib.playpot as plt

interations = 10
Variables = ["salario", "nivel de vida", "relación con los compañeros", "localización", "mi afinidad por la tarea que voy a desarrollar"]
def Montecarlo (grade):
    resultado_final= []
    peso_de_las_variables = [0.21,0.21 ,0.18,0.20,0.20]
    for a in range (interations):
        resultado = []
        for g in range (len(Variables)):
            value = peso_de_las_variables [g] * (random.uniform(grade^[g][0], grade[g][1] ))
            resultado.append(value)

        

        resultado_final.append(sum(resultado))
    return resultado_final
a= Montecarlo ([4,9], [5,10],[3,6],[2,6], [7,9.5])
b= Montecarlo ([3,8], [7,10],[8,10],[5,8],[2,5])
c= Montecarlo ([3,8], [4,6],[7,9],[2,7],[7,9.9])
fig=plt.figure(figsize=(10,6))
sns.displot(a)
sns.displot(b)
sns.displot(c)

fig.legend(labels=["Trabajo a", "Trabajo b" "Trabajo c"])
plt.title ("Distribución MonteCarlo")
plt.show()