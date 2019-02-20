# -*- coding: utf-8 -*-

# Scrapy settings for drive project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'drive'

SPIDER_MODULES = ['drive.spiders']
NEWSPIDER_MODULE = 'drive.spiders'
FEED_EXPORT_FIELDS = ['ANNONCE_LINK', 'ANNONCE_DATE', 'ID_CLIENT', 'GARAGE_ID', 'TYPE', 'SITE', 'MARQUE', 'MODELE', 'ANNEE', 'MOIS', 'NOM', 'CARROSSERIE', 'OPTIONS', 'CARBURANT', 'CYLINDRE', 'PUISSANCE', 'PORTE', 'BOITE', 'NB_VITESSE', 'PRIX', 'KM', 'PLACE', 'COULEUR', 'PHOTO', 'LITRE', 'IMMAT', 'VIN', 'VN_IND', 'CONTACT','CONTACT_PRENOM', 'CONTACT_NOM', 'GARAGE_NAME', 'SIRET', 'ADRESSE', 'VILLE', 'CP', 'DEPARTEMENT', 'PROVINCE', 'COUNTRY', 'TELEPHONE', 'TELEPHONE_2', 'TELEPHONE_3','TELEPHONE_4', 'TELEFAX', 'EMAIL', 'WEBSITE']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'drive (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'drive.middlewares.DriveSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'drive.middlewares.DriveDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'drive.pipelines.DrivePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPCACHE_IGNORE_MISSING = False


#HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcaches' #'/home/n.jguirim/crawl/cachesWare/drive_caches'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
