from scrapy import cmdline

cmdline.execute("scrapy crawl xiaozhu -o respBody -t json".split())