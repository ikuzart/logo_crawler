import argparse
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
from logo_crawler import HTMLPage, SeedFromCsv, CsvWriter, Downloader, LogoFinder
from logo_crawler.settings import MAX_WORKERS, OUTPUT_CSV
from logo_crawler.helpers import get_logger


logger = get_logger()

def parse_args(app_name) -> argparse.Namespace:
    parser = argparse.ArgumentParser(app_name)
    parser.add_argument("seed", help="path to seed csv file")
    return parser.parse_args()


def main():
    args = parse_args(__file__)
    seed = SeedFromCsv(args.seed)
    downloader = Downloader()
    logo_finder = LogoFinder()
    csv_writer = CsvWriter()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for out in as_completed([executor.submit(downloader.download, url) for url in seed.get_next_url()]):
            html_page: HTMLPage = out.result()
            if not html_page.text:
                continue
            html_page.logo_url = logo_finder.search(html_page)
            csv_writer.write_to_output(html_page, OUTPUT_CSV)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.exception(e)
