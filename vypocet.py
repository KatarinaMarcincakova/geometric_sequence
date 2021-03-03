mozogBody = [2508.875, 1245.785, 1221.217, 2046.472, 2216.765, 2051.15, 1889.278, 2221.477, 2531.659, 3673.808, 2000.41, 4645.577]
tumorBody = [405.093, 233.502, 534.43, 0.208, 0.429, 18.257, 88.459, 50.715, 31.73, 2.479, 3.443, 36.571]

mozog = 0
tumor = 0

for i in range(12):
    pocetM = mozogBody[i]
    pocetT = tumorBody[i]

    plochaM = pocetM / 10000

    plochaT = (plochaM * tumorBody[i]) / (mozogBody[i] + tumorBody[i])

    mozog += plochaM 
    tumor += plochaT 

print('mozog poskodeny na ', (tumor / mozog) * 100, '%')

    
