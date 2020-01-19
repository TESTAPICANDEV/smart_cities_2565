import csv

import matplotlib.pyplot as plt

import wolframalpha
client = wolframalpha.Client("RHQQL4-YWUJQ5Q7WR")

detect = False

import json

not_done = ['Beaconsfield (group)', 'Blandford-Blenheim/Oxford County (group)', 'Brossard (group)', 'Cape Breton Regional Municipality (group)', 'Castlegar (group)', 'Châteauguay\xa0(group)', 'City of Morden (group)', 'City of Mount Pearl', 'City of Niagara Falls / Niagara Region (group)', 'City of Port Colborne / Niagara Region (group)', 'City of St. Catharines / Niagara Region (group)', 'City of Thorold / Niagara Region (group)', 'City of Welland / Niagara Region (group)', 'City of Windsor (group)', 'City of Winkler (group)', 'County of Grande Prairie No. 1', 'Cree Nation of Chisasibi', 'Delaware Nation at Moraviantown (group)', 'Delson (group)', 'District of Barriere', 'District of Tofino', 'East Zorra-Tavistock/Oxford County (group)', 'Gaskiers - Point la Haye (group)', 'Huron-Wendat Nation (group)', 'Ingersoll/Oxford County (group)', 'Kainai - Blood Tribe First Nation', 'Kwantlen First Nation (group)', 'La Broquerie (group)', 'La Prairie (group)', 'Lévis', 'Local Government District of Pinawa', 'Lower Nicola Indian Band', 'Magog (group)', 'Mashteuiatsh', 'Membertou (group)', 'Mississaugas of the New Credit First Nation', 'Municipality of Bayham', 'Municipality of Chatham-Kent (group)', 'Municipality of the County of Annapolis (group)', 'Municipality of the County of Antigonish (group)', 'Municipality of the District of Digby (group)', 'Norwich/Oxford County (group)', "Paqtnkek Mi'kmaw Nation (group)", 'Plessisville (group)', 'Riverhead (group)', 'Rossland (group)', 'Rural Municipality of Stanley (group)', 'Saint-Basile-le-Grand (group)', 'Saint-Constant (group)', 'Sainte-Catherine (group)', 'Saint-Lambert (group)', 'Saint-Pierre-Jolys (group)', 'Saint-Quentin (group)', 'South-West Oxford/Oxford County (group)', "St. Vincent's - St. Stephen's - Peter's River (group)", 'Tillsonburg/Oxford County (group)', 'Town of Amherstburg/County of Essex (group)', 'Town of Annapolis Royal (group)', 'Town of Digby (group)', 'Town of Fort Erie / Niagara Region (group)', 'Town of Grimsby / Niagara Region (group)', 'Town of Kingsville/County of Essex (group)', 'Town of Lakeshore/County of Essex (group)', 'Town of LaSalle/County of Essex (group)', 'Town of Leamington/County of Essex (group)', 'Town of Lincoln / Niagara Region (group)', 'Town of Niagara-on-the-Lake / Niagara Region (group)', 'Town of Pelham / Niagara Region (group)', 'Town of Tecumseh/County of Essex (group)', 'Township of Langley (group)', 'Township of Wainfleet / Niagara Region (group)', 'Township of West Lincoln / Niagara Region (group)', 'Trail (group)', 'Walpole Island First Nation (group)', 'Woodstock/Oxford County (group)', 'Zorra/Oxford County (group)', 'Biigtigong Nishnaabeg (Pic River First Nation)', 'Brazeau County (group)', 'City of Airdrie & Area', 'City of Cambridge/Waterloo Region (group)', 'City of Côte Saint-Luc', 'City of Guelph (group)', 'City of Kitchener/Waterloo Region (group)', 'City of Surrey (group)', 'City of Vancouver (group)', 'City of Waterloo/Waterloo Region (group)', 'Cree Nation of Eastmain', 'Fredericton (group)', 'Greater Victoria (group)', 'Mohawk Council of Akwesasne', 'Opaskwayak Cree Nation (group)', 'Parkland County (group)', 'Rural Municipality of Kelsey (group)', "Saint Mary's First Nation (group)", 'Township of North Dumfries/Waterloo Region (group)', 'Township of Wellesley/Waterloo Region (group)', 'Township of Wilmot/Waterloo Region (group)', 'Township of Woolwich/Waterloo Region (group)', 'Wellington County (group)', 'Yellowhead County (group)']

X = []
Y = []
counter = 99
first = True

not_detected = []
detected = []

with open('mapdata-1.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		if first:
			first = False
		# elif not detect:
		# 	if "Town of Leamington/County of Essex (group)" in row[0]:
		# 		detect = True
		else:
			print("{} : {} : {}".format(row[0], row[1], row[3]))
			if row[0] in not_done and "(group)" in row[0]:
				name = row[0][:-8]
				# Y.append(int(row[3]))
				res = client.query(name)
				with open("{}.json".format(counter), "w+") as file:
					try:
						json.dump(res, file, indent=4)
						with open("detected.txt", "a") as detected_file:
							detected_file.write("{}; {}\n".format(counter, row[0]))
							counter += 1

					except:
						print("could not {}".format(row[0]))
						not_detected.append(row[0])
						print(not_detected)



	        # if row[1]=="Yes":
	        # 	X.append(1)
	        # else:
	        # 	X.append(0)

# print(X)
# print(Y)

# plt.plot(X, Y, "ro")
# plt.ylabel('Population')
# plt.show()