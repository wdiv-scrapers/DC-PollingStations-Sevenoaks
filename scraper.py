from dc_base_scrapers.geojson_scraper import GeoJsonScraper

stations_url = "https://opendata.arcgis.com/datasets/5adf5af49995429b9527ef64d94c7be6_0.geojson"
districts_url = "https://opendata.arcgis.com/datasets/105585d2718f480d9703973d134aaa40_0.geojson"
council_id = 'E07000111'

stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
