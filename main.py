from rich import print
from libs.protocols import WebScrap
from libs.modules import ScrapTopUniversity
from libs.models import DataUni


class ScrapProcessor:

    def download_json(self, webS: WebScrap):
        return webS.download_json()


def main():

    url = "https://www.topuniversities.com/rankings/endpoint?nid=3846212&page=4&items_per_page=15&tab=&region=&countries=&cities=&search=&star=&sort_by=&order_by=&program_type="

    scrap = ScrapProcessor()
    top = scrap.download_json(ScrapTopUniversity(url))

    item = [DataUni(**t) for t in top]

    for row in item:
        print(row.dict())


if __name__ == "__main__":
    main()
