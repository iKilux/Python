def commaCode(nameList):
    name=''
    for i in range(len(nameList)):
        if i==0:
            name+=nameList[i]
        elif i< len(nameList)-1:
            name+=', '+nameList[i]
        else:
            name+=' and '+nameList[i]
    print(name)
spam=['apples', 'bananas', 'tofu', 'cats']
K=['Mahamadou Kaba','Mame Diarra','Yacine Blodin Youm','Ndeye Khady Diouf','Marietou Hadj','Awa Diouf','Samia Waby']
commaCode(K)
#commaCode(spam)
