# Erlina Rohmawati	    175150201111045
# Tania Malik Iryana	175150201111053
# Alvina Eka Damayanti	175150201111056
# Jeowandha Ria Wiyani	175150207111029

import re, time
import matplotlib.pyplot as plt

awal = time.time()  
################proses cleaning dan tokenization (nomor 2)###############################
def cleaningTag(readCorpus) :
    #membersihkan tag
    regex = r"(<\w{5}>|</\w{5}>)|(<(/?)\w+>)(.?)+"
    corpusTanpaTag = re.sub(regex,"",readCorpus)
    return corpusTanpaTag

def cleaningPunc(corpusTanpaTag) :
    #membersihkan tanda baca
    corpusBersih = re.sub(r"[^a-zA-Z]", " ", corpusTanpaTag)
    return corpusBersih

def tokenisasi(corpus): #melakukan tokenisasi
    corpusToken = re.split(r"[\s]+", corpus)
    corpusToken.remove("")
    corpusToken.remove("")
    return corpusToken

#############menghitung banyaknya dokumen dalam korpus (nomor 3.a)####################
def hitungDokumen(readCorpus) :
    #3a
    dokumen = re.findall(r'<DOC>',readCorpus)
    return dokumen


#########################menghitung kata yang frekuensinya tinggi, 20 kata yg muncul di semua dokumen, dan 10 kata yang muncul di 50 dokumen (nomor 3.b, c, d)##################################
def kemunculanKata(corpusToken, dokumen) :
    #3b
    print("-----20 kata yang frekuensinya tertinggi-----")
    frekuensi = frekuensiKata(corpusToken)
    i=0
    for word, frekuensiTertinggi in sorted(frekuensi.items(),key=lambda item:item[1], reverse=True):
        i+=1
        if (i<=20):
            print(word, frekuensiTertinggi)
        else:
            break
    
    kemunculanKata = {}
    #3c
    print("-----20 kata muncul di seluruh dokumen-----")
    reTeksDok = re.sub(r"(<\w{5}>|<\w{5}>)|(<(\/?)([^DOC])\w+>)(.?)+","",readCorpus)
    TeksDok = re.split(r"<DOC>", reTeksDok)
    kataUnik = list(frekuensi.keys())
    countSemua = 0
    for i in range(len(kataUnik)):
        jumlahDok =0
        for j in range(len(TeksDok)):
            cariKata = re.findall(kataUnik[i],TeksDok[j])
            if (len(cariKata) != 0) :
                jumlahDok +=1
                continue
            else :
                break
        if(jumlahDok==len(dokumen)):
            countSemua += 1
            if(countSemua<=20):
                print(kataUnik[i] + ": "+str(jumlahDok))
        if(countSemua==20):
            break
    
    #3d
    print("-----10 kata muncul di 50 dokumen-----")
    count50 = 0
    for i in range(len(kataUnik)):
        jumlahDok =0
        for j in range(len(TeksDok)):
            cariKata = re.search(kataUnik[i],TeksDok[j])
            if (cariKata != None) :
                jumlahDok +=1
                continue
            if(jumlahDok > 50):
                break
        if(jumlahDok==50):
            count50 += 1
            if(count50<=10):
                print(kataUnik[i] + ": "+str(jumlahDok))
        if(count50==10):
            break

def frekuensiKata(corpusToken) :
    frekuensi = {}

    for word in corpusToken:
        count = frekuensi.get(word,0)
        frekuensi[word] = count+1

    return frekuensi

##############menghitung banyaknya seluruh kata (nomor 3.g)#############################
def hitungKata(corpusToken):
    banyaknyaTerm = len(corpusToken)
    print("Banyaknya kata dalam korpus : " + str(banyaknyaTerm) + " kata")

##############menghitung banyaknya seluruh kalimat (nomor 3.k)###########################
def hitungKalimat(corpusCleaning) :
    regex =  r"['\"]?[A-Za-z0-9][^.?!]+$|['\"]?[A-Za-z0-9][^.?!]+"
    kalimat = re.findall(regex, corpusCleaning)
    
    print("Banyaknya kalimat dalam korpus : " + str(len(kalimat)) + " kalimat")

###################menghitung banyaknya kata unik (nomor 3.h)############################
def banyakKataUnikKataSedikit(corpusToken) :
    frekuensi = frekuensiKata(corpusToken)

    kataUnik = 0
    kataSedikit = 0
    for word in frekuensi.keys():
        kataUnik += 1
        if(frekuensi[word]<10) :
            kataSedikit += 1
    return kataUnik,kataSedikit
    

#######banyak kata unik dengan imbuhan ber- dan akhiran -kan (nomor 3.i dan 3.j)#########
def kataUnikBerimbuhan(readKamus, corpusToken) :
    kamusToken = re.split(r"[\s]+", readKamus)

    regexBerr = r"\bber\w+"
    regexKan = r"\w+kan\b"
    kataBer = []

    frekuensi={}

    for word in corpusToken:
        count = frekuensi.get(word,0)
        frekuensi[word] = count+1

    kataUnik = " ".join(frekuensi.keys())

    # kataUnik
    kataBer = re.findall(regexBerr,kataUnik)
    kamusBer = re.findall(regexBerr, readKamus)

    kataKan = re.findall(regexKan,kataUnik)
    kamusKan = re.findall(regexKan, readKamus)

    for i in range (len(kataBer)):
        hasilBerKamus = re.search(kataBer[i],readKamus)
        # print("i = " + str(i))
        # print(kataBer[i])
        if (hasilBerKamus != None ):
            # print(hasilBerKamus.group())
            kataBer.remove(hasilBerKamus.group())
        if(i == (len(kataBer)-1)) :
            break
 
    for i in range (len(kataKan)):
        hasilKanKamus = re.search(kataKan[i],readKamus)
        # print("i = " + str(i))
        # print(kataKan[i])
        if (hasilKanKamus != None ):
            # print(hasilKanKamus.group())
            kataKan.remove(hasilKanKamus.group())
        if(i == (len(kataKan)-1)) :
            break

    print("Banyaknya kata dengan imbuhan Ber- : " + str(len(kataBer)))
    print("Banyaknya kata dengan imbuhan -kan : " + str(len(kataKan)))
    
################menghitung bigram dan trigram (nomor 3.l)###############################
def bigramTrigram(corpusCleaning) :
    text_list = corpusCleaning.split()

    #BIGRAM
    print("-----20 Frase Bigram-----")
    dictBigram = {}
    for i in range(len(text_list)-1):
        text = text_list[i]+" "+text_list[i+1]
        if text not in dictBigram.keys():
            dictBigram.update({text:1})       
        else:
            dictBigram[text] = dictBigram[text]+1
    
    #sorting bigram
    i=0
    for word, sortBigram in sorted(dictBigram.items(),key=lambda item:item[1], reverse=True):
        i+=1
        if (i<=20):
            print(word, sortBigram)
        else:
            break

    #TRIGRAM
    print("-----20 Frase Trigram-----")
    dictTrigram = {}
    for i in range(len(text_list)-2):
        text = text_list[i]+" "+text_list[i+1]+" "+text_list[i+2]
        if text not in dictTrigram.keys():
            dictTrigram.update({text:1})       
        else:
            dictTrigram[text] = dictTrigram[text]+1

    #sorting trigram
    i=0
    for word, sortTrigram in sorted(dictTrigram.items(),key=lambda item:item[1], reverse=True):
        i+=1
        if (i<=20):
            print(word, sortTrigram)
        else:
            break       

# #######################################################################################

#membaca file korpus
corpus = open('D:/Tania/UB/Semester 6/STKI/Tugas/Tugas 3/corpus.txt', 'rt', encoding="ANSI")
readCorpus = corpus.read()
corpus.close()

#Membaca kamus kata
kamusKata = open('D:/Tania/UB/Semester 6/STKI/Tugas/Tugas 3/KamusKataDasar.txt', 'rt',)
readKamus = kamusKata.read()
kamusKata.close()

corpusTanpaTag = cleaningTag(readCorpus)
corpusCleaning = cleaningPunc(corpusTanpaTag)
corpusToken = tokenisasi(corpusCleaning)

countDokumen = len(hitungDokumen(readCorpus))
frequency = frekuensiKata(corpusToken)

kataUnik, kataSedikit = banyakKataUnikKataSedikit(corpusToken)

print("=========================a=============================")
print("Banyaknya dokumen dalam korpus : " + str(countDokumen) + " dokumen")

print("======================b, c & d=========================")
kemunculanKata(corpusToken, dokumen=hitungDokumen(readCorpus))

print("\n======================f & h==========================")
print("Banyaknya kata unik : " + str(kataUnik) + " kata")
print("Banyaknya kata dengan frekuensi kurang dari 10 : " + str(kataSedikit) + " kata")

print("\n========================g============================")
hitungKata(corpusToken)

print("\n======================i & J==========================")
kataUnikBerimbuhan(readKamus, corpusToken)

print("\n========================k============================")
hitungKalimat(corpusTanpaTag)

print("\n========================l============================")
bigramTrigram(corpusCleaning)

print("\n========================e============================")
frekKata = list(frequency.values())
plt.plot(frekKata,linewidth=2, color='r')
plt.ylabel('Frekuensi')
plt.xlabel('Dokumen Ke-')
plt.show()
print(corpusToken)

akhir = time.time()
print ("\nTotal Waktu Proses " + str(akhir-awal) + " Detik." )