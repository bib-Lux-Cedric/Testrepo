auto_tankfuellung = 0
auto_kilometerstand = 0
auto_benzinverbrauch = 6.2


def Tanken( menge ):
    global auto_tankfuellung
    auto_tankfuellung = auto_tankfuellung + menge
    print("Tanken:", menge,"Liter")



def Fahren( strecke ):
    global auto_kilometerstand, auto_benzinverbrauch, auto_tankfuellung
    auto_kilometerstand = auto_kilometerstand + strecke
    auto_tankfuellung = auto_tankfuellung - strecke / 100 * auto_benzinverbrauch
    print("Fahren:", strecke,"Kilometer")


def Anzeige():
    global auto_kilometerstand, auto_benzinverbrauch, auto_tankfuellung
    print("-"*30)
    print("Kilometerstand:", auto_kilometerstand)
    print("Tankfüllung:", auto_tankfuellung)
    print("Benzinverbrauch:", auto_benzinverbrauch)
    print("-"*30)

Anzeige()
Tanken(60)
Anzeige()
Fahren(120)
Anzeige()
Fahren(50)
Anzeige()
Fahren(250)
Anzeige()
Tanken(20)
Anzeige()