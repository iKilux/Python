#! usr/bin/python3
fichier = open('write.txt', 'w')
fichier.write('\nUne premiere chose QUOI')
fichier.close()

fichier = open('write.txt', 'a')
fichier.write('\nJe suis en train d\'ecrire pour écrire en vrai je ne vise rien.\nEt pourtant j\'écris toujours')
fichier.write('\nEt oui je ne m\'arrete toujours pas parce que je ne peux pas le faire')
fichier.write('\nOk c\'est bon maintenant ! ')
fichier.close()


fichier = open('write.txt')
contenuFichier = fichier.read()
fichier.close()
print(contenuFichier)
