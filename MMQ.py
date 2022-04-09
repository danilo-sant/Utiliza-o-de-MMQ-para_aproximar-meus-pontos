import matplotlib.pyplot as plt
import numpy as np

def mmqlinear(x,y):
  n=len(x)
  sx=0
  sxq=0
  sy=0
  sxy=0
  for i in range(n):
    sx=sx+x[i]
    sxq=sxq+x[i]**2
    sy=sy+y[i]
    sxy=sxy+x[i]*y[i]
  A=np.array([[n, sx],[sx,sxq]])
  b=np.array([[sy],[sxy]])
  r=np.linalg.inv(A)@b
  return r

#pontos coletados
x=np.array([3, 14, 30, 34, 80, 81, 79, 189, 182] )
y=np.array([65.10, 238.50, 583.20, 789.40, 1835.90, 2179.30, 2275.90, 4879.60, 5154.20])

r=mmqlinear(x,y)
print(r)

xn=range(x[0],x[len(x)-1])
yn=r[0]+r[1]*xn

#plt.imshow(img) #imagem
#pontos coletados
plt.plot(x,y,'ro')

plt.plot(xn,yn,'b')

plt.title("Gráfico Com MMQ")
plt.ylabel('Soma de potência')
plt.xlabel('Nª de parques')

plt.grid(color='k', linestyle='-', linewidth=0.5)  # insere o Grid na tela
plt.show()