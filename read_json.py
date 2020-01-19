import json
import glob, os

class model:
	def __init__(self):
		self.name = None
		self.population = 0
		self.good = 0
		self.funding = 0
		self.nearby_cities_count = 0
		self.nearby_cities_population = 0
		self.nearby_cities_distance = 0
		self.nearby_features_count = 0
		self.nearby_features_distance = 0
		self.big_compagnies_count = 0
		self.big_compagnies_total_employee = 0
		self.big_compagnies_total_revenu = 0
	def add_feature(self, title, e):
		if title=="Nearby cities":
			i = e["subpod"]["img"]["@alt"]
			table = i.split(" | ")
			b = [] #distance
			c = [] #people
			a = len(table)//2
			for k in table[1::2]:
				# print(k) #add distance in km
				b.append(int(k.split(" ")[0]))
			for k in table[2::2]:
				l = k.split(" people ")[0]
				if "million" in l:
					c.append(float(l.split(" ")[0])*1000000)
				else:
					try:
						c.append(float(l))
					except:
						pass
			self.nearby_cities_count = a
			self.nearby_cities_population = sum(c)
			self.nearby_cities_distance = sum(b)

		elif title=="Nearby features":
			i = e["subpod"]["img"]["@alt"]
			table = i.split(" | ")
			b = [] #distance
			c = [] #people
			a = len(table)//2
			for k in table[2::2]:
				b.append(int(k.split(" ")[0])) #add distance in km
			self.nearby_features_count = a
			self.nearby_features_distance = sum(b)				
			


lines = []

datas = []
idx = 0

# os.chdir("./data/")

dict_numbers = {}

with open("detected.txt", "r") as detected_file:
	content = detected_file.readlines()
	for e in content:
		lne = e.split("; ")
		try:
			dict_numbers[lne[0]] = lne[1][:-1]
		except:
			pass
# print(dict_numbers)

with open("mapdata-1.csv", "r") as mapdata_file:
	content1 = mapdata_file.readlines()
	for file in glob.glob("*.json"):
		print(file)
		with open(file, "r") as json_file:
			data = json.load(json_file)
			try:
				other_name = dict_numbers[file[:-5]]
				# print(other_name)
			except:
				continue
			datas.append(model())
			datas[idx].name = other_name

			for e in content1:
				ea = e.split(",")
				if ea[0] in other_name:
					if ea[1] == "Yes":
						datas[idx].good = 1
					else:
						datas[idx].good = 0
					datas[idx].population = ea[3]
					datas[idx].funding = int(ea[4].split(" ")[1])


			for e in data["pod"]:
				# print(e["@title"])
				title = e["@title"]
				datas[idx].add_feature(title, e)

				# print(datas[idx].nearby_cities_distance)
			idx += 1

with open("result.csv", "w") as csv_result_file:
	for e in datas:
		csv_result_file.write("{}, {}, {}, {}, {}, {}, {}, {}\n".format(e.good, e.population, e.nearby_cities_count, e.nearby_cities_distance, e.nearby_cities_population, e.nearby_features_count, e.nearby_features_distance, e.funding))

				




		# name = data["pod"][0]["subpod"]["plaintext"]
		# # print(name)


		# population = data["pod"][1]["subpod"]["img"]["@alt"]
		# print(population)
