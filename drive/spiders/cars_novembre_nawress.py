# -*- coding: utf-8 -*-
import scrapy
import re
import pdb
class CarsSpider(scrapy.Spider):
	name = "drive"
	allowed_domains = ["drive.com.au"]
	start_urls = ['http://www.drive.com.au/listings/buy-used-cars/australia/?makeMulti%5B0%5D=&modelMulti%5B0%5D=&priceMin=&priceMax=&keywords=&advancedSearch=']
	all = set()
	def parse(self, response):
		d = {}

		for item in response.xpath('//div[@class="listing"]'):

			href =  item.css('a::attr(href)').extract_first()
			nom = item.css('h6::text').extract_first()
			photo = item.xpath('.//span[@class="imageCount"]/i[@class="far fa-image"]/following-sibling::text()').extract_first().replace(" ","")
			porteplace = item.xpath(".//div[@class='col-xs-12']/text()").extract()[4]

			porteplace=re.findall("([0-9]+)",  porteplace)
			if porteplace is not None and (len(porteplace)==1):
				porte=porteplace[0].replace(" ","")
				place=""
			elif len(porteplace)>1 :
				porte=porteplace[0].replace(" ","")
				place=porteplace[1].replace(" ","")
			else:
				porte=""
				place=""

			if href is not None:
				#pdb.set_trace()
				link = response.urljoin(href)
				request = scrapy.Request(link, callback=self.parse_link)
				request.meta['d'] = d
				request.meta['photo'] = photo
				request.meta['porte'] = porte
				request.meta['place'] = place
				request.meta['nom'] = nom
				yield request
		next_page = response.xpath('//html/body/div[8]/div/main/div/div[1]/div[5]/a[@rel="next"]//@href').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse   )

	def parse_link(self, response):
		d = response.meta['d']
		photo = response.meta['photo']
		porte = response.meta['porte']
		place = response.meta['place']
		nom = response.meta['nom']
		annonce_link=response.url
		garage_id=response.xpath('//input[@name="tmrDealerID"]/@value').extract_first()
		garage_licence=response.xpath('//div[@class="nameLicence"]/text()').re_first(r'[0-9]+')
		id_client=response.xpath('//input[@name="tmrID"]/@value').extract_first()
		Type=response.xpath('//input[@name="seller_type"]/@value').extract_first()
		marque=response.xpath('//input[@name="Make"]/@value').extract_first()
		modele=response.xpath('//input[@name="Model"]/@value').extract_first()
		annee=response.xpath('//input[@name="year"]/@value').extract_first()
		carrosserie=response.xpath('//input[@name="body_style"]/@value').extract_first()
		km=response.xpath('//input[@name="odometer"]/@value').extract_first()
		couleur=response.xpath('//input[@name="colour"]/@value').extract_first()
		garage_name=""
		contact_prenom=""
		if Type=="dealer":
			garage_name=response.xpath('//input[@name="dealer_name"]/@value').extract_first()
		else:
			if Type=="private":
				contact_prenom=response.xpath('//input[@name="dealer_name"]/@value').extract_first()
		if contact_prenom=="":
			contact_prenom=response.xpath('//input[@name="name"]/@value').extract_first()
		contact_nom=response.xpath('//input[@name="lastName"]/@value').extract_first()
		email=response.xpath('//input[@name="email"]/@value').extract_first()
		cp=response.xpath('//input[@name="postcode"]/@value').extract_first()

		#####################--------------------- LOCATION
		province=response.xpath('//input[@name="region"]/@value').re_first(r'.*\s([A-Z]{2,})')
		if province == '' or (province == None):
			ville = response.xpath('//input[@name="region"]/@value').extract_first()
		else:
			ville = response.xpath('//input[@name="region"]/@value').re_first(r'(.*)\s[A-Z]{2,}')

		if  response.xpath('//input[@name="region"]/@value').extract_first() == None :
			try:
				ville = response.xpath('//div[@class="dpricedetail location-details"]//text()').extract()[0].replace('\n','').replace(' ','')
				if  ville == '' :
					province = None
				else :
					try:
						province = response.xpath('//div[@class="dpricedetail location-details"]//text()').extract()[1].replace('\n','').replace(' ','')
					except:
						province = None
			except:
				province = None
				ville =  None

		#################----------------------
		immat=response.xpath('//input[@name="plate"]/@value').extract_first()
		litre=response.xpath('//input[@name="litres"]/@value').extract_first()
		no_chassis=response.xpath('//input[@name="vin"]/@value').extract_first()
		no_vehicule=response.xpath('//input[@name="listingId"]/@value').extract_first()
		telephone=response.xpath('//input[@name="dealer_phone"]/@value').extract_first()
		if telephone is not None:
			telephone=telephone.replace("(","").replace(")","").replace(" ","").replace("+","")
		else:
			telephone=""
		boite=response.xpath('//input[@name="transmission"]/@value').extract_first()
		cylindre=response.xpath('//dt[@title="Cylinders"]/following-sibling::dd/text()').extract_first()
		carburant = response.xpath('/html/body/div[9]/div/main/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[1]/dl/dd[2]//text()').extract_first()

		nb_vitesse=response.xpath('//dt[@title="Gear Number"]/following-sibling::dd/text()').extract_first()
		puissance=response.xpath('//dt[text()="Performance"]/following-sibling::dd/text()').re_first(r'Power: (.*)')

		type = response.xpath('//span[@class="star"]').extract_first()
		if type:
			if "used" in type:
				vn_ind = 0
			elif "new" in type:
				vn_ind = 1
			else:
				vn_ind = ""
		else:vn_ind = ""

		prix = response.xpath('//div[@class="dpricedetail"]/span[@class="ddriveawayp"]//text()').extract_first().replace('$','').replace('\n','').strip()
		if Type == '':
			Type=response.xpath('//div[@class="sellerType dealer"]/text()').extract_first()
			id_client=response.xpath('//i[@class="far fa-star"]/@rel').extract_first()
			marque=response.xpath('//dt[text()="Make"]/following-sibling::dd/text()').extract_first()
			modele=response.xpath('//dt[text()="Model"]/following-sibling::dd/text()').extract_first()
			annee=response.xpath('//dt[text()="Year"]/following-sibling::dd/text()').extract_first()
			carrosserie=response.xpath('//dt[text()="Body"]/following-sibling::dd/text()').extract_first()
			km=response.xpath('//dt[text()="Odometer"]/following-sibling::dd/text()').extract_first()
			couleur=response.xpath('//dt[text()="Colour"]/following-sibling::dd/text()').extract_first()
			no_chassis=response.xpath('//dt[text()="VIN"]/following-sibling::dd/text()').extract_first()
			boite=response.xpath('//dt[text()="Transmission"]/following-sibling::dd/text()').extract_first()

			province=response.xpath('//div[@class="location"]/text()').re_first(r'.*\s([A-Z]{2,})')
			if province == '':
				department=response.xpath('//div[@class="location"]/text()').extract_first()
			else:
				department=response.xpath('//div[@class="location"]/text()').re_first(r'(.*)\s[A-Z]{2,}')

		if km is not None:
			km=km.replace(',', '.')
			km=km.replace(' kms', '')
		if litre is not None:
			litre=litre.replace(',', '.')
		if prix is not None:
			prix=prix.replace(',', '.')
			prix=prix.replace('$', '')
			prix=prix.replace('*', '')
		d = {'ANNONCE_LINK': annonce_link, 'ANNONCE_DATE':'', 'ID_CLIENT':id_client, 'GARAGE_ID': garage_id, 'TYPE': Type, 'SITE':'drive.com.au', 'MARQUE': marque, 'MODELE': modele, 'ANNEE': annee, 'MOIS':'', 'NOM':nom, 'CARROSSERIE': carrosserie, 'OPTIONS':'', 'CARBURANT':carburant, 'CYLINDRE':cylindre, 'PUISSANCE':puissance, 'PORTE':porte, 'BOITE':boite, 'NB_VITESSE':nb_vitesse, 'PRIX':prix, 'KM':km, 'PLACE':place, 'COULEUR':couleur, 'PHOTO':photo, 'LITRE':litre, 'IMMAT':immat, 'VIN':'', 'VN_IND':vn_ind, 'CONTACT':'', 'CONTACT_PRENOM':contact_prenom, 'CONTACT_NOM':contact_nom, 'GARAGE_NAME':garage_name, 'SIRET':garage_licence, 'ADRESSE':'', 'VILLE':ville, 'CP':cp, 'DEPARTEMENT':'', 'PROVINCE':province, 'COUNTRY':'', 'TELEPHONE':telephone, 'TELEPHONE_2':'', 'TELEPHONE_3':'', 'TELEPHONE_4':'', 'TELEFAX':'', 'EMAIL':email, 'WEBSITE':''}
		if d['ID_CLIENT'] not in self.all:
			yield d
			self.all.add(d['ID_CLIENT'])

