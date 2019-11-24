"""
////
This Program is a calculator for European style call and put options
The mathematical formula is the Black and Scholes option model (1973)
///

-----------
Start         23/11/2019 | 22:13:09
Actualisation 24/11/2019 | 00:29:51
Actualisation 24/11/2019 | 16:08:36
Actualisation 24/11/2019 | 22:13:09
End           25/11/2019 | 00:09:49
-----------
"""

import tkinter as tkn
import math as mt
from scipy.stats import norm

def N(x):
    return norm.cdf(x, loc= 0, scale= 1)
def NP(x):
    return (1/(mt.sqrt(2*mt.pi)))*(mt.exp(-mt.pow(x,2)/2))
    

#fonction pour calcul CALL
def pricing():
    #test des variables
    test=[SJACENT.get().replace(",", "",1).replace(".", "",1).isdigit(),
          STRIK.get().replace(",", "",1).replace(".", "",1).isdigit(),
          echeance.get().replace(",", "",1).replace(".", "",1).isdigit(),
          TAUX.get().replace(",", "",1).replace(".", "",1).isdigit(),
          VOLATIVITE.get().replace(",", "",1).replace(".", "",1).isdigit(),
          DIVIDENDE.get().replace(",", "",1).replace(".", "",1).isdigit()]
    if all(test)==True:
        #déclaration des variables
        S=float (SJACENT.get().replace(",", ".",1))
        K=float (STRIK.get().replace(",", ".",1))
        M=float (echeance.get().replace(",", ".",1))
        T=float (M/365)
        I=float (TAUX.get().replace(",", ".",1))/100
        F=float (VOLATIVITE.get().replace(",", ".",1))/100
        Q=float (DIVIDENDE.get().replace(",", ".",1))/100
        #Calcul pour le Call
        d1=(mt.log(S/K)+T*(I-Q+(mt.pow(F,2))/2))/(F*mt.sqrt(T))
        d2=d1-F*mt.sqrt(T)
        Cc=mt.exp(-Q*T)*S*N(d1)-K*(mt.exp(-I*T))*N(d2)
        Dc=mt.exp(-Q*T)*N(d1)
        Gc=(NP(d1)*mt.exp(-Q*T))/(S*F*mt.sqrt(T))
        Tec=(-S*mt.exp(-Q*T)*NP(d1)*F)/(2*mt.sqrt(T))+Q*S*mt.exp(-Q*T)*N(d1)-I*K*N(d2)*mt.exp(-I*T)
        Rc=K*T*mt.exp(-I*T)*N(d2)
        Vc=S*mt.exp(-Q*T)*mt.sqrt(T)*NP(d1)
        #Actualisation des résultats dans la fenetre
        priceC.configure(text = round (Cc,4))
        deltaC.configure(text = round (Dc,4))
        gammaC.configure(text = round (Gc,4))
        thetaC.configure(text = round (Tec,4))
        rhoC.configure(text = round (Rc,4))
        vegaC.configure(text = round (Vc,4))
        #Calcul pour le Put
        Cp=mt.exp(-Q*T)*S*(N(d1)-1)+K*mt.exp(-I*T)*(1-N(d2))
        Dp=mt.exp(-Q*T)*(N(d1)-1)
        Gp=(NP(d1)*mt.exp(-Q*T))/(S*F*mt.sqrt(T))
        Tep=((-S*NP(d1)*F)/(2*mt.sqrt(T)))-Q*S*mt.exp(-Q*T)*N(-d1)+(I*K*mt.exp(-I*T)*N(-d2))
        Rp=-K*T*mt.exp(-I*T)*N(-d2)
        Vp=S*mt.exp(-Q*T)*mt.sqrt(T)*NP(d1)
        #Actualisation des résultats dans la fenetre
        priceP.configure(text = round (Cp,4))
        deltaP.configure(text = round (Dp,4))
        gammaP.configure(text = round (Gp,4))
        thetaP.configure(text = round (Tep,4))
        rhoP.configure(text = round (Rp,4))
        vegaP.configure(text = round (Vp,4))
        erreur_label.configure(text='')
    else:
        erreur_label.configure(text='Sorry, This Entry Is Not Allowed', bd='10', width='20')
        priceP.configure(text = ' !!! ')
        deltaP.configure(text = ' !!! ')
        gammaP.configure(text = ' !!! ')
        thetaP.configure(text = ' !!! ')
        rhoP.configure(text = ' !!! ')
        vegaP.configure(text = ' !!! ')
        priceC.configure(text = ' !!! ')
        deltaC.configure(text = ' !!! ')
        gammaC.configure(text = ' !!! ')
        thetaC.configure(text =' !!! ')
        rhoC.configure(text = ' !!! ')
        vegaC.configure(text = ' !!! ')
#creation de la fenetre    
fenetre = tkn.Tk()
fenetre.title=('')
fenetre.geometry("550x400")

#creation des button
calcul_button=tkn.Button(fenetre, text='Calculer', width='15', font = ("Helvetica", 10), command= pricing)

#creation label principale 
entet_label=tkn.Label(fenetre, text=('Black-Scholes Pricer | European Option'), bd='15', font = ("Helvetica", 15))

#creation label des entrées 
ssjacent_label=tkn.Label(fenetre, text=('Spot Price'), bd='5', width='15')
strik_label=tkn.Label(fenetre, text=('Strike'), bd='10', width='15')
echeance_label=tkn.Label(fenetre, text=('Days until Expiration'), bd='10', width='15')
volativite_label=tkn.Label(fenetre, text=('Volatility % '), bd='10', width='15')
taux_label=tkn.Label(fenetre, text=('Risk-Free Interest %'), bd='10', width='15')
dividende_label=tkn.Label(fenetre, text=('Dividend %'), bd='10', width='15')
erreur_label = tkn.Label(fenetre, text='',width='12')
credit_label=tkn.Label(fenetre, text=('Credit: hichem-L | C7@live.ca'), bd='15', font = ("Helvetica", 8))
#creation des espaces vides pour les 
call_label = tkn.Label(fenetre, text='Call Option',width='12')
put_label = tkn.Label(fenetre, text='Put Option',width='12')
priceC = tkn.Label(fenetre,bd='10')
deltaC = tkn.Label(fenetre,bd='10')
gammaC = tkn.Label(fenetre,bd='10')
thetaC = tkn.Label(fenetre,bd='10')
rhoC   = tkn.Label(fenetre,bd='10')
vegaC  = tkn.Label(fenetre,bd='10')
priceP = tkn.Label(fenetre,bd='10')
deltaP = tkn.Label(fenetre,bd='10')
gammaP = tkn.Label(fenetre,bd='10')
thetaP = tkn.Label(fenetre,bd='10')
rhoP   = tkn.Label(fenetre,bd='10')
vegaP  = tkn.Label(fenetre,bd='10')
#creation des label pour les résultats 
price_label= tkn.Label(fenetre, text=('Price'), bd='10', width='12')
delta_label=tkn.Label(fenetre, text=('DELTA'), bd='10', width='12')
gamma_label=tkn.Label(fenetre, text=('GAMMA'), bd='10', width='12')
theta_label=tkn.Label(fenetre, text=('THETA'), bd='10', width='12')
rho_label=tkn.Label(fenetre, text=('RHO'), bd='10', width='12')
vega_label=tkn.Label(fenetre, text=('VEGA'), bd='10', width='12')

#creation des entrées 
SJACENT=tkn.Entry(fenetre, width='10')
SJACENT.insert(0, '120')
STRIK=tkn.Entry(fenetre, width='10')
STRIK.insert(0, '100')
echeance=tkn.Entry(fenetre, width='10')
echeance.insert(0, '90')
VOLATIVITE=tkn.Entry(fenetre, width='10')
VOLATIVITE.insert(0, '20')
TAUX=tkn.Entry(fenetre, width='10')
TAUX.insert(0, '5')
DIVIDENDE=tkn.Entry(fenetre, width='10')
DIVIDENDE.insert(0, '0')
#Organisation de affichage de resultat

#ligne 1 pour entet
entet_label.grid(row=1, column=1, columnspan='4')

#cote gauche pour les entrées et les label des entrées
ssjacent_label.grid(row=3, column=1)
SJACENT.grid(row=3, column=2, sticky=tkn.W)

strik_label.grid(row=4, column=1,)
STRIK.grid(row=4, column=2, sticky=tkn.W)

echeance_label.grid(row=5, column=1)
echeance.grid(row=5, column=2, sticky=tkn.W)

volativite_label.grid(row=6, column=1)
VOLATIVITE.grid(row=6, column=2, sticky=tkn.W)

taux_label.grid(row=7, column=1)
TAUX.grid(row=7, column=2, sticky=tkn.W)

dividende_label.grid(row=8, column=1)
DIVIDENDE.grid(row=8, column=2, sticky=tkn.W)

#cote droit pour les button de choix
calcul_button.grid(row=9, column=3, columnspan='4', sticky=tkn.W)

#cote droit pour les résultats et les label des résultats
call_label.grid(row=2, column=4)
put_label.grid(row=2, column=5)
price_label.grid(row=3, column=3, sticky=tkn.E)
delta_label.grid(row=4, column=3)
gamma_label.grid(row=5, column=3)
theta_label.grid(row=6, column=3)
rho_label.grid(row=7, column=3)
vega_label.grid(row=8, column=3)

priceC.grid(row=3, column=4, sticky=tkn.E)
deltaC.grid(row=4, column=4, sticky=tkn.E)
gammaC.grid(row=5, column=4, sticky=tkn.E)
thetaC.grid(row=6, column=4, sticky=tkn.E)
rhoC.grid(row=7, column=4, sticky=tkn.E)
vegaC.grid(row=8, column=4, sticky=tkn.E)
priceP.grid(row=3, column=5, sticky=tkn.E)
deltaP.grid(row=4, column=5, sticky=tkn.E)
gammaP.grid(row=5, column=5, sticky=tkn.E)
thetaP.grid(row=6, column=5, sticky=tkn.E)
rhoP.grid(row=7, column=5, sticky=tkn.E)
vegaP.grid(row=8, column=5, sticky=tkn.E)
erreur_label.grid(row=10, column=2, columnspan='4', sticky=tkn.W)
credit_label.grid(row=11, column=1, columnspan='4', sticky=tkn.W)
#affichage de la fenetre
fenetre.mainloop()
