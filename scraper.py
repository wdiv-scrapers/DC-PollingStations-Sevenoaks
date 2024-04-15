from dc_base_scrapers.geojson_scraper import GeoJsonScraper

stations_url = "https://utility.arcgis.com/usrsvcs/servers/9c64a911bfee4ed9acd032f03dcc8f06/rest/services/OpenData/OD_PollingStations/FeatureServer/0/query?outFields=*&where=1%3D1&f=json"
districts_url = "https://utility.arcgis.com/usrsvcs/servers/ecffd85eb016496a92a0091064a77762/rest/services/OpenData/OD_PollingDistricts/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
council_id = 'SEV'

stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
