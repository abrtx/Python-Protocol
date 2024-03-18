from rich import print
from libs.protocols import WebScrap
from libs.modules import ScrapTopUniversity
from libs.models import DataUni
from pyspark.sql import SparkSession
from pyspark import SparkConf


conf = SparkConf().setAppName("MyScraping") \
            .setMaster("local") \
            .set("spark.executor.memory", "2g") \
            .set("spark.executor.cores", "2")

sc = SparkSession.builder.config(conf=conf).getOrCreate()

print(SparkConf().getAll())


class ScrapProcessor:

    def download_json(self, webS: WebScrap):
        return webS.download_json()


def main():

    url = "https://www.topuniversities.com/rankings/endpoint?nid=3846212&page=4&items_per_page=15&tab=&region=&countries=&cities=&search=&star=&sort_by=&order_by=&program_type="

    scrap = ScrapProcessor()
    top = scrap.download_json(ScrapTopUniversity(url))

    item = [DataUni(**t) for t in top]

    # for row in item:
    #     print(row.dict())

    df = sc.createDataFrame(data=item)

    df.show(truncate=False)

    df.createOrReplaceTempView("table")
    sc.sql('select title, rank from table order by rank desc').show(20, False)


if __name__ == "__main__":
    main()
