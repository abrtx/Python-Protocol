from rich import print
from libs.protocols import WebScrap
from libs.modules import ScrapTopUniversity
from libs.models import DataComp


class ScrapProcessor:

    def download_json(self, webS: WebScrap):
        return webS.download_json()


def main():

    url1 = "https://www.topuniversities.com/rankings/endpoint?nid=3846272&page=0&items_per_page=2&tab="

    url2 = "https://www.topuniversities.com/ranking_table_ctas"

    url3 = "https://www.topuniversities.com/rankings/filter/endpoint?nid=3846272&tab=indicators"
    url4 = "https://date.nager.at/api/v3/LongWeekend/2024/CL"

    scrap = ScrapProcessor()
    top = scrap.download_json(
        ScrapTopUniversity(
            # url3, ['subjects', 'Broad subject area']))  # 0
            url1, ['score_nodes']))  # 3
            # url2, ['data']))  # 4
            # url4, []))  # 2

    comp2 = DataComp().test_comp_3()

    item2 = [comp2(**t) for t in top]

    for row in item2:
        print(row.dict(exclude_none=True))


if __name__ == "__main__":
    main()
