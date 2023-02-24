#A SCRIPT FOR A CAR DEALING COMPANY
print("Welcome to Queen's cars company limited\nWe deal with all kinds of cars\nour cars are \
quality and affordable.")
input("if you would like to make inquires  click enter to move to the next detail")
print("Bellow are some of the cars , you might be interested in ")
print("Toyota\nHyundai\nHonda\nBenz\nCorola\nTesla\nFord\nJeep\nLexus\nJagua\nKia\nMazda\nVolvo\nLand Rover\
\nMercedes Benz\nBuick\nChevrolet\nDodge\nAcura\nAudi\nForsche\nLincoln\nVolkswagen\
\nNissan\nChrysler\nAlfa Romeo\nCadillac\buick")
#print("PLEASE SELECT A CAR TO DISPLAY THE PRICE")

carsprice={
    "Toyota":8878788,
    "Hyundai":37636500,
    "Benz":66567787,
    "Ford":665654600,
    "Corolla":5454688,
    "Tesla":767477477,
    "Jeep":74647647800,
    "Lexus":653753736,
    "Jaguar":6353555,
    "Kia":98989,
    "Mazda":100000,
    "Volvo":3837838,
    "Land Rover":474674647,
    "Mercedes Benz":89273887,
    "Chevrolet":475658,
    "Dodge":353535530,
    "Acura":476767747,
    "Audi":466565757,
    "Porshe":64546876687,
    "Lincoln":3562562526,
    "Volkswagen":66565666,
    "Nissan":53452425652,
    "Chrysler":54254254252,
    "Alfa Romeo":3534354362,
    "Cadilloc":55454252400,
    "Buick":87877878,    
        }
name=input("PLEASE SELECT THE CAR YOU WANT TO DISPLAY THE PRICE")
print("Price of ",name," is", carsprice[name],"Ghc")
    