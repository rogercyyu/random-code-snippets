theBoard = {'A1':1, 'B1':2, 'C1':3, 'D1':4, 'E1':5, 'F1':6, 'G1':7,
          'A2':8, 'B2':9, 'C2':10, 'D2':11, 'E2':12, 'F2':13, 'G2':14,
          'A3':15, 'B3':16, 'C3':17, 'D3':18, 'E3':19, 'F3':20, 'G3':21,
          'A4':22, 'B4':23, 'C4':24, 'D4':25, 'E4':26, 'F4':27, 'G4':28,
          'A5':29, 'B5':30, 'C5':31, 'D5':32, 'E5':33, 'F5':34, 'G5':35,
          'A6':36, 'B6':37, 'C6':38, 'D6':39, 'E6':40, 'F6':41, 'G6':42,
          '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7}

def theBoardinvert(d):
    inv = {}
    for k, v in d.iteritems():
        keys = inv.setdefault(v, [])
        keys.append(k)
    return inv

print(theBoardinvert)