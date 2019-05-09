from os import listdir
from os.path import isfile, join
import csv


def main(dir_path):
    nse_files = [join(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f)) and f[-7:] != '_F1.txt']
    for nse_file  in nse_files:
        with open(nse_file, 'r') as nse_file_h:
            highs = []
            for row in csv.reader(nse_file_h):
                (symbol, _, _, _, _, high_price, _, total_traded_quantity, _) = row
                highs.append(float(high_price))
            for high in highs:
                highers = [h for h in highs if ((h - high)/high) > 0.05]
                if len(highers) > 0:
                    print(symbol)
                    # highest_high = max(highers)
                    # print(high)
                    # print(highest_high)
                    # print("*" * 50)
                    break


if __name__ == '__main__':
    main(r'oneminutedata\2019\02MAY')
