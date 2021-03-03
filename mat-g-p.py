from PIL import Image
import numpy
import random

inputSnimky = ['images/BS1/bs0.png' , 'images/BS1/bs1.png' , 'images/BS1/bs2.png' , 'images/BS1/bs3.png' , 'images/BS1/bs4.png' , 'images/BS1/bs5.png' ,
                'images/BS1/bs6.png' , 'images/BS1/bs7.png' , 'images/BS1/bs8.png' , 'images/BS1/bs9.png' , 'images/BS1/bs10.png' , 'images/BS1/bs11.png' ,]


for numOfScan in range(12):

    image = Image.open(inputSnimky[numOfScan])

    imArr = numpy.asarray(image)

    numOfBlackAve = 0
    numOfBrainAve = 0
    otherAve = 0
    numOfTumorAve = 0

    for k in range(1000):
        
        numOfBlack = 0
        numOfBrain = 0
        numOfTumor = 0
        other = 0

        for i in range(10000):
            colorCode = imArr[random.randint(0, 784)][random.randint(0, 784)]
            if colorCode == 0:
                numOfBlack += 1
            elif colorCode >= 24 and colorCode <= 120:
                numOfBrain += 1
            elif colorCode == 22:
                numOfTumor += 1
            else:
                other += 1

        numOfBlackAve += numOfBlack
        numOfBrainAve += numOfBrain
        numOfTumorAve += numOfTumor
        otherAve += other

    print('-------------------------------------------------')
    print('SCAN: ', numOfScan)
    print('    pocet mimo priemerne: ', numOfBlackAve / 1000)
    print('    pocet na mozgu priemerne: ', numOfBrainAve / 1000)
    print('    pocet na tumore priemerne: ', numOfTumorAve / 1000)
    print('    pocet inych priemerne: ', otherAve / 1000)

