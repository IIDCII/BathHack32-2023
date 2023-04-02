from icrawler.builtin import GoogleImageCrawler

google_Crawler = GoogleImageCrawler(storage = {'root_dir': 'images'})
google_Crawler.crawl(keyword = 'nuclear aftermath', max_num = 5)