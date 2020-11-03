import matplotlib.pyplot as plt


eixo_X =[1872,1890,1900,1920,1940,1950,1960,1970,1980,1991,2000,2010]
eixo_Y =[9.9,14.3,17.4,30.6,41.1,51.9,70,93.1,119,146.8,169.8,190.75]


plt.plot(eixo_X,eixo_Y)
plt.ylabel('Milhoes')
plt.xlabel('Ano')

plt.title('Populacao brasileira em milhoes/ano')
plt.show()
