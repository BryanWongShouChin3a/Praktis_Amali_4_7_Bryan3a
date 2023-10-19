#Ini merupakan satu program ringkas untuk mendapatkan isipadu kuboid
pi=3.142
def kira_kuboid(tinggi, panjang, lebar):
    isipadu_kuboid=tinggi*panjang*lebar
    return isipadu_kuboid

def kuboid(): #Isipadu kuboid
    tinggi=float(input("Masukkan tinggi kuboid:"))
    panjang=float(input("Masukkan panjang kuboid:"))
    lebar=float(input("Masukkan lebar kuboid:"))
    print("Isi padu kuboid=", kira_kuboid(tinggi, panjang, lebar))

def kira_silinder(pi, jejari, tinggi):
    Isipadu_silinder=pi*(jejari**2)*tinggi
    return Isipadu_silinder

def silinder(): #Isipadu silinder
    jejari=int(input("Masukkan jejari silinder:"))
    tinggi=int(input("Masukkan tinggi silinder:"))
    print("Isipadu silinder=", kira_silinder(pi, jejari, tinggi))

def kira_kon(pi, jejari, tinggi):
          Isipadu_kon=(1/3)*pi*(jejari**2)*tinggi
          return Isipadu_kon

def kon(): #Isipadu kon
    jejari=int(input("Masukkan jejari kon:"))
    tinggi=int(input("Masukkan tinggi kon:"))
    print("Isipadu kon=", kira_silinder(pi, jejari, tinggi))

def kira_sfera(pi, jejari):
    Isipadu_sfera=(4/3)*pi*(jejari**3)
    return Isipadu_sfera
    
def sfera():
    jejari=int(input("Masukkan jejari sfera:"))
    print("Isipadu sfera=", kira_sfera(pi, jejari))

################
# Subatur cara utama
################

ulang=True

while(ulang):
    print("""


************************
Menu mengira isi padu
************************
1. Kuboid
2. Silinder
3. Kon
4. Sfera
5. Keluar dari program

""")
    print("")

    pilih=int(input("Sila masukkan pilihan anda:"))

    if(pilih==1):
        kuboid()    #memanggil fungsi kuboid
    elif(pilih==2):
        silinder()   #memanggil fungsi silinder
    elif(pilih==3):
        kon()       #memanggil fungsi kon
    elif(pilih==4):
        sfera()      #memanggil fungsi sfera
    elif(pilih==5):
        ulang=False
        print("Bye Bye")
        exit

    else:
        print("Pilihan tiada dalam senarai.")
    


    

