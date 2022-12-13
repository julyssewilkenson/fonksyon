import random
import string
###3

alfabet="abcdefghijklmnopqrstuvwxyz"
def jenere_kod(kantite_karakte_mo_a):
    alf = alfabet
    kod=""
    for i in range(kantite_karakte_mo_a):
        let = random.choice(alf)
        kod += let
        alf = alf[0:alf.index(let)] + alf[alf.index(let) + 1:len(alf)]

    return kod
print(jenere_kod(5))


###4
alfabet_nimerik="abcdefghijklmnopqrstuvwxyz0123456789"

def jenere_kod(kantite_karakte_mo_a):
    alf = alfabet_nimerik
    kod=""
    for i in range(kantite_karakte_mo_a):
        let = random.choice(alf)
        kod += let
        alf = alf[0:alf.index(let)] + alf[alf.index(let) + 1:len(alf)]

    return kod

print(jenere_kod(10))



###5
def slug(mo):
    rezilta=""
    for karakte in mo:
        if karakte.lower() in alfabet or karakte == "-":
            rezilta +=karakte
    return rezilta

print(slug("julysse#$@--Jules"))

###6

def separe(chenn):
    return ",".join(list(chenn.strip()))   ###join nan fizyone chenn mwen an pandan l ap separe yo pa vigil
 
print(separe("julysse"))


###7

def kripte(mo):
    pozisyon = []
    for kar in mo:
        pozisyon.append(str(alfabet.index(kar)))
    return "-".join(pozisyon)
    
print(kripte("alo"))


###8
def dekripte(mo):
    korespondan = []
    for pozisyon in mo.split("-"):
        korespondan.append(alfabet[int(pozisyon)])
    return "".join(korespondan)
print(dekripte("0-11-14"))



###9
kontene1 = 30
kontene2 = 35
def pemitasyon(kontene1, kontene2):
    kontene_tanpore = kontene1
    kontene1 = kontene2
    kontene2 = kontene_tanpore
    return(kontene1, kontene2)
print(pemitasyon(kontene1, kontene2)) 




###10
nom="Julysse Wilkenson"
def  fonksyon_nom(nom):
    separe_nom = nom.split(" ")
    separe_nom_san_espas=[]
    inisyal_nom=""
    for nom in separe_nom:
        separe_nom_san_espas += nom.split("-")
    for nom in separe_nom_san_espas:
        inisyal_nom += nom[0]
    print(inisyal_nom)
fonksyon_nom(nom)