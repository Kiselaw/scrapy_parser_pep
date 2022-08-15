import csv
import datetime as dt
import logging


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
BASE_DIR = 'results/'


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = {
            'Статус': 'Количество',
            'Active/Accepted': 0,
            'Deferred': 0,
            'Final': 0,
            'Provisional': 0,
            'Rejected': 0,
            'Superseded': 0,
            'Withdrawn': 0,
            'Draft': 0,
        }
        self.total = 0

    def process_item(self, item, spider):
        if [item['status']] not in self.results.keys():
            self.results[item['status']] = 0
            logging.info(
                f'Добавлен незапланированный статус: {item["status"]}'
            )
        # Можно было бы сократить, но
        # так Accepted и Active будут отдельно,
        # а мне бы хотелось, чтобы они были совмещены.
        # Но переделаю, если настаиваете :)
        if item['status'] in 'Active/Accepted':
            self.results['Active/Accepted'] += 1
        else:
            self.results[item['status']] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        results = list(self.results.items())
        results.append(('Total', self.total))
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        with open(
            BASE_DIR / 'results' / file_name, 'w', encoding='utf-8'
        ) as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
