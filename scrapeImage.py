from icrawler.builtin import GoogleImageCrawler

google_Crawler = GoogleImageCrawler(storage = {'root_dir': 'imagess'})
google_Crawler.crawl(keyword = 'nuclear aftermath', max_num = 5)