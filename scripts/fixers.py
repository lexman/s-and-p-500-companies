# BRK/B or BRK.B => BRK-B (this is what yahoo needs)
def fixsymbol(symbol):
    symbol = symbol.replace('/', '-')
    symbol = symbol.replace('.', '-')
    return symbol

def fixname(name):
    name = name.replace('Amer ', 'American ')
    name = name.replace('Pwr', 'Power')
    name = name.replace(' Grp', ' Group')
    name = name.replace(' Hldgs', ' Holdings')
    name = name.replace(' Hldg', ' Holdings')
    name = name.replace(' Svcs', ' Services')
    name = name.replace(' Svs', ' Services')
    name = name.replace(' Natl', ' National')
    name = name.replace(' Engr', ' Engineering')
    name = name.replace(' Inc', '')
    name = name.replace(' Cos', 'Companies')
    name = name.replace('Intl', 'International')
    name = name.replace("Int'l", 'International')
    name = name.rstrip(',')
    name = name.replace('Air Products & Chem', 'Air Products & Chemicals')
    name = name.replace('AMETEK, Inc', 'AMETEK Inc')
    name = name.replace("Amphenol Corp'A'", 'Amphenol Corp A')
    name = name.replace('PLC', 'Plc')
    name = name.replace('Apartment Investment & Mg', 'Apartment Investment & Mgmt')
    name = name.replace('Autodesk, Inc', 'Autodesk Inc')
    name = name.replace('Automatic Data Proc', 'Automatic Data Processing')
    name = name.replace('Becton, Dickinson', 'Becton Dickinson')
    name = name.replace("'A'", '')
    name = name.replace("'B'", '')
    name = name.replace('Cablevision Sys', 'Cablevision Systems')
    name = name.replace('CBS Corp ', 'CBS Corp')
    name = name.replace("Cognizant Tech Solutions'", 'Cognizant Technology Solutions')
    name = name.replace('Comcast Cl', 'Comcast Corp')
    name = name.replace('duPont(E.I.)deNemours', 'Du Pont (E.I.)')
    name = name.replace('Disney (Walt) Co', 'Walt Disney Co')
    name = name.replace("Discovery Communications'", 'Discovery Communications')
    name = name.replace('Fidelity National Info Services','Fidelity National Information Services')
    name = name.replace('Lincoln National Corp', 'Lincoln National')
    name = name.replace('NIKE,', 'NIKE')
    name = name.replace('United Parcel', 'United Parcel Service')
    name = name.replace('PNC Financial Services Gr', 'PNC Financial Services')
    name = name.replace('Perrigo Co Plc', 'Perrigo')
    name = name.replace('News Corp Cl A', 'News Corporation')
    name = name.replace('Nabors Indus', 'Nabors Industries')
    name = name.replace('Mohawk Indus', 'Mohawk Industries')
    name = name.replace('Lauder (Estee) Co', 'Estee Lauder Co')
    name = name.replace('Hartford Finl Services Gp,Financials', 'Hartford Financial Services')
    name = name.replace('ENSCO Plc Cl', 'ENSCO Plc')
    name = name.replace('Tesoro Corp', 'Tesoro Petroleum Co')
    # unfinished ...
    return name

def correctToBillions(item):
   if item.endswith('M'):
       return float(item[:-1]) / 1000
   elif item.endswith('B'):
       return item[:-1]
   else:
       return item
