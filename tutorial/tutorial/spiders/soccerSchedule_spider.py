import scrapy
import json
from scrapy.exporters import JsonItemExporter

class RowObj:
    def __init__(self):
        self.hour = ''
        self.sport = ''
        self.description = ''
        self.channels = ''

class ScheduleSpider(scrapy.Spider):
    name = "schedule"

    def start_requests(self):
        urls = [
            'http://dixibit.com/arenavision/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        i = 0
        tables = response.css('table')
        rowData = RowObj()
        tableData = []
        schedulesData = []
        rowDataX = []
        for table in tables:
            tableData = []
            print table    

            n=0
            for row in table.css('tr'):            
                cellData = row.css('td::text')   
                rowDataX = []                 
                
                try:

                    hour = cellData[0].extract()
                    rowDataX.append(hour)
                    rowDataX.append(cellData[1].extract())
                    rowDataX.append(cellData[2].extract())
                    rowDataX.append(cellData[3].extract())

                    print 'funciona hsdp'
                    n += 1
                    tableData.append(rowDataX)
                except Exception as e:
                    print '-------------------'
                    print '-------------------'
                    print e
                    print '-------------------'
                    print '-------------------'

                    print 'Fuk this shit fuck this shit!!!'
                    pass                                
            i += 1
            schedulesData.append(tableData)
        theFile = open('tablesInJSON.json', 'wb')
        print tableData
        theFile.write(json.dumps(schedulesData, ensure_ascii=False))
        theFile.close

        print 'DONE'
                   

        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)




        print 'Ya no quiero trabajar'

