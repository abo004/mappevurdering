

def alkohol_volum(total_volum, alkohol_prosent):
    # Man kan skrive alkoholprosenten baade som broek eller prosent
    if alkohol_prosent > 1:
        alkohol_prosent = alkohol_prosent / 100
    volum = total_volum * alkohol_prosent
    return volum


def total_volum(alkohol_volum, alkohol_prosent):
    volum = alkohol_volum / alkohol_prosent
    return volum


def alkohol_per_krone(alkohol_volum, pris):
    alkperkr = float(alkohol_volum) / float(pris) * 1000
    return alkperkr