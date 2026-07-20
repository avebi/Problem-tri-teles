import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
import sys

# vyber druhu simulace
konfigurace = input(
    "Vyber konfiguraci:\n"
    "v - vlastni\n"
    "r - nahodne\n"
    "z - Zeme-Slunce-Mesic\n"
    "o - dráha ve tvaru osmičky\n"
    "m - motyl\n"
    "p - planeta obihajici dve hvezdy\n"
    ">>> ").lower()

# seznamy pro všechny tělesa    
m = []
poloha = []
rychlost = []


if konfigurace == "v":
    
    # kolik teles chceme simulovat 2-5
    pocet_teles = int(input("Vyberte kolik těles chete simulovat (2 az 5): "))
    
    if pocet_teles < 2 or pocet_teles > 5:
        print("Vyberte prosím podporovaný počet těles")
        sys.exit()

    # hmotnost kazdeho telesa
    for i in range(pocet_teles):

        vstup_m = input(f"Zadejte hmotnost {i+1}. tělesa nebo napište 'r' pro náhodnou: ").strip()

        if vstup_m.lower() == "r":
            hmotnost = random.uniform(0.5, 2.0)
        else:
            hmotnost = float(vstup_m)

        m.append(hmotnost)

        
    # pocatecni poloha kazdeho telesa
    for i in range(pocet_teles):    
        
        vstup_poloha = input(f"Zadejte souřadnice {i+1}. tělesa (x y z) jednotlive hodnoty oddelujte mezernikem nebo napište 'r' pro náhodnou: ").strip()

        if vstup_poloha.lower() == "r":
            pozice = [random.uniform(-3,3) for _ in range(3)]
        else:
            pozice = list(map(float, vstup_poloha.split()))

        poloha.append(pozice)


    # pocatecni rychlost kazdeho telesa
    for i in range(pocet_teles):

        vstup_rychlost = input(f"Zadejte rychlost {i+1}. tělesa (vx vy vz) jednotlive hodnoty oddelujte mezernikem nebo napište 'r' pro náhodnou: ").strip()

        if vstup_rychlost.lower() == "r":
            v = [random.uniform(-0.5,0.5) for _ in range(3)]
        else:
            v = list(map(float, vstup_rychlost.split()))

        rychlost.append(v)


elif konfigurace == "r":

    pocet_teles = int(input("Vyberte kolik těles chete simulovat (2 az 5): "))

    if pocet_teles < 2 or pocet_teles > 5:
        print("Vyberte prosím počet těles od 2 do 5.")
        sys.exit()

    m = [random.uniform(0.5, 2) for _ in range(pocet_teles)]


    for body in range(pocet_teles):

        while True:

            jedna_poloha = [random.uniform(-7, 7) for _ in range(3)]

            # poloha prvního tělesa se přijme automaticky
            if len(poloha) == 0:
                poloha.append(jedna_poloha)
                break

            # kontrola vzdálenosti od všech již vytvořených těles
            dostatecne_daleko = True

            for jina_poloha in poloha:
                vzdalenost = np.linalg.norm(np.array(jedna_poloha) - np.array(jina_poloha))

                if vzdalenost < 1.5:
                    dostatecne_daleko = False
                    break

            if dostatecne_daleko:
                poloha.append(jedna_poloha)
                break
        

    for body in range(pocet_teles):
        jedna_rychlost = []

        for souradnice in range(3):
            cislo = random.uniform(-0.5, 0.5)
            jedna_rychlost.append(cislo)

        rychlost.append(jedna_rychlost)

    
elif konfigurace == "z":
    pocet_teles = 3
    m = [1.0, 0.000003, 0.000000037]
    poloha = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.00257, 0.0, 0.0]]
    rychlost = [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.034, 0.0]]

elif konfigurace == "o":
    pocet_teles = 3
    m = [1.0, 1.0, 1.0]
    poloha = [
        [-0.97000436, 0.24308753, 0.0],
        [0.97000436, -0.24308753, 0.0],
        [0.0, 0.0, 0.0]
    ]
    rychlost = [
        [0.466203685, 0.43236573, 0.0],
        [0.466203685, 0.43236573, 0.0],
        [-0.93240737, -0.86473146, 0.0]
    ]

elif konfigurace == "m":
    pocet_teles = 3
    m = [1.0, 1.0, 1.0]
    poloha = [[-1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    rychlost = [[0.0, 0.5, 0.0], [0.0, -0.5, 0.0], [0.0, 0.0, 0.0]]

elif konfigurace == "p":
    pocet_teles = 3
    m = [1.0, 1.0, 0.001]
    poloha = [[-0.5, 0.0, 0.0], [0.5, 0.0, 0.0], [0.0, 4.0, 0.0]]
    rychlost = [[0.0, -0.707106, 0.0], [0.0, 0.707106, 0.0], [-0.63, 0.0, 0.0]]
else:
    print("Vyberte prosim platnou moznost")
    sys.exit()
    
    
pridat_druzici = input("Chcete přidat družici (tedy teleso s hmotnosti 0)? (a/n): ").lower()

if pridat_druzici == "a":

    vstup_poloha = input("Zadejte polohu družice (x y z), nebo r pro náhodnou: ")

    if vstup_poloha.lower() == "r":
        poloha_druzice = [random.uniform(-6, 6) for _ in range(3)]
    else:
        poloha_druzice = list(map(float, vstup_poloha.split()))

    vstup_rychlost = input("Zadejte rychlost družice (vx vy vz), nebo r pro náhodnou: ")

    if vstup_rychlost.lower() == "r":
        rychlost_druzice = [random.uniform(-0.5, 0.5) for _ in range(3)]
    else:
        rychlost_druzice = list(map(float, vstup_rychlost.split()))

    m.append(0.0)
    poloha.append(poloha_druzice)
    rychlost.append(rychlost_druzice)

    pocet_teles += 1
    

# celkovy pocatecni stav systemu
S0 = np.array([poloha, rychlost]).ravel()


# system obycejnych diferencialnich rovnic

def ode(t, S, m, pocet_teles):

    # aktuální polohy všech těles
    polohy = S[:3 * pocet_teles].reshape(pocet_teles, 3)

    # aktuální rychlosti všech těles
    rychlosti = S[3 * pocet_teles:].reshape(pocet_teles, 3)
    
    # aktualni zrychleni, vypoctena z Newtnova gravitacniho zakona

    zrychleni = np.zeros((pocet_teles, 3))

    for i in range(pocet_teles):
        
        for j in range(pocet_teles):

            if i != j:

                zrychleni[i] += (m[j] * (polohy[j] - polohy[i]) / np.linalg.norm(polohy[j] - polohy[i])**3)
            
    return np.array([rychlosti, zrychleni]).ravel()

print(S0)
print(ode(0, S0, m, pocet_teles))


# jeden krok metody Runge-Kutta 4. radu
def rk4_krok(f, t, S, h, m, pocet_teles):
    
    k1 = f(t, S, m, pocet_teles)
    k2 = f(t + h/2, S + h*k1/2, m, pocet_teles)
    k3 = f(t + h/2, S + h*k2/2, m, pocet_teles)
    k4 = f(t + h, S + h*k3, m, pocet_teles)

    novy_stav = S + h * (k1 + 2*k2 + 2*k3 + k4) / 6

    return novy_stav

# velikost časového kroku
h = 0.01

# počáteční čas
t = 0

# seznam všech stavů soustavy
stavy = []

# počáteční stav
S = S0
stavy.append(S.copy())

# výpočet dalších stavů
for i in range(5000):

    S = rk4_krok(ode, t, S, h, m, pocet_teles)
    t = t + h

    stavy.append(S.copy())

# převedení seznamu na numpy array
stavy = np.array(stavy)

# polohy všech těles ve všech časových okamžicích
polohy_v_case = stavy[:, :3 * pocet_teles].reshape(len(stavy), pocet_teles, 3)

# vykreslení trajektorií ve 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

for i in range(pocet_teles):

    if m[i] == 0:
        ax.plot(
            polohy_v_case[:, i, 0],
            polohy_v_case[:, i, 1],
            polohy_v_case[:, i, 2],
            linestyle=":",
            color="black",
            label="Družice"
        )

        ax.scatter(
            polohy_v_case[-1, i, 0],
            polohy_v_case[-1, i, 1],
            polohy_v_case[-1, i, 2],
            color="black",
            s=20
        )

    else:
        cara, = ax.plot(
            polohy_v_case[:, i, 0],
            polohy_v_case[:, i, 1],
            polohy_v_case[:, i, 2],
            label=f"Těleso {i + 1}"
        )

        ax.scatter(
            polohy_v_case[-1, i, 0],
            polohy_v_case[-1, i, 1],
            polohy_v_case[-1, i, 2],
            color=cara.get_color()
        )
ax.set_title(f"Problém {pocet_teles} těles - RK4")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.legend()
plt.show()



fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

trajektorie = []
body = []

for i in range(pocet_teles):

    if m[i] == 0:
        traj, = ax.plot([], [], [], linestyle=":", color="black", label="Družice")
        bod, = ax.plot([], [], [], marker="o", color="black", markersize=4)
    else:
        traj, = ax.plot([], [], [], label=f"Těleso {i + 1}")
        bod, = ax.plot([], [], [], marker="o", color=traj.get_color(), markersize=6)

    trajektorie.append(traj)
    body.append(bod)

ax.set_title(f"Problém {pocet_teles} těles - animace RK4")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.legend()

ax.set_xlim(np.min(polohy_v_case[:,:,0]), np.max(polohy_v_case[:,:,0]))
ax.set_ylim(np.min(polohy_v_case[:,:,1]), np.max(polohy_v_case[:,:,1]))
ax.set_zlim(np.min(polohy_v_case[:,:,2]), np.max(polohy_v_case[:,:,2]))


def update(frame):

    for i in range(pocet_teles):

        trajektorie[i].set_data(polohy_v_case[:frame,i,0], polohy_v_case[:frame,i,1])
        trajektorie[i].set_3d_properties(polohy_v_case[:frame,i,2])

        body[i].set_data([polohy_v_case[frame,i,0]], [polohy_v_case[frame,i,1]])
        body[i].set_3d_properties([polohy_v_case[frame,i,2]])

    return trajektorie + body


animace = FuncAnimation(fig, update, frames=range(0, len(stavy), 10), interval=10, blit=False)

plt.show()