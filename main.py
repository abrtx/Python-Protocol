from rich import print
from libs.protocols import WebScrap
from libs.modules import ScrapTopUniversity
from libs.models import DataUni, DataComp
from pyspark.sql import SparkSession
from pyspark import SparkConf


# conf = SparkConf().setAppName("MyScraping") \
#             .setMaster("local") \
#             .set("spark.executor.memory", "2g") \
#             .set("spark.executor.cores", "2")

# sc = SparkSession.builder.config(conf=conf).getOrCreate()

# print(SparkConf().getAll())


class ScrapProcessor:

    def download_json(self, webS: WebScrap):
        return webS.download_json()


def main():

    url = "https://www.topuniversities.com/rankings/endpoint?nid=3846212&page=4&items_per_page=15&tab=&region=&countries=&cities=&search=&star=&sort_by=&order_by=&program_type="

    url1 = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3751069_indicators.txt?sadmbz"

    url3 = "https://www.topuniversities.com/rankings/filter/endpoint?nid=3846272&tab=indicators"

    scrap = ScrapProcessor()
    top = scrap.download_json(ScrapTopUniversity(url3))

    # item = [DataUni(**t) for t in top]

    # for row in item:
    #     print(row.dict())

    # df = sc.createDataFrame(data=item)

    # df.show(truncate=False)

    # df.createOrReplaceTempView("table")
    # sc.sql('select title, rank from table order by rank desc').show(20, False)

    comp = DataComp()

    item = [DataComp(**t) for t in top]

    for row in item:
        print(row.dict())

    comp.test_comp_0()
    # comp.test_comp_1()


if __name__ == "__main__":
    main()
