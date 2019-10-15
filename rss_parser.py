import urllib.request, re

urls = ('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109',
        'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=131')

def crawl(url):
    ufile = urllib.request.urlopen(url)
    contents = ufile.read().decode('utf-8')

    locations = re.findall(r'<location wl_ver="3">.+?</location>', contents, re.DOTALL)

    for loc in locations:
        city = re.search(r'<city>(.+)</city>', loc)

        print(city.group(1))

        data = re.findall(r'<data>.+?</data>', loc, re.DOTALL)

        for item in data:
            tmEf = re.search(r'<tmEf>(.+)</tmEf>', item)
            wf = re.search(r'<wf>(.+)</wf>', item)
            tmn = re.search(r'<tmn>(.+)</tmn>', item)
            tmx = re.search(r'<tmx>(.+)</tmx>', item)
            reli = re.search(r'<reliability>(.+)</reliability>', item)

            print('    ', tmEf.group(1), wf.group(1), tmn.group(1), tmx.group(1), reli.group(1))


def main():
    for url in urls:
        crawl(url)

if __name__ == "__main__":
    main()