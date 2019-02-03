#!/usr/bin/env python3

import os
import sys
import argparse
import configparser

import petridish.sites

def path(x, parser):
    if os.path.exists(x):
        return x
    else:
        parser.error('File does not exist: {}'.format(x))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', metavar='NUM', dest='n', type=int, default=10,
                        help='Number of samples to download from each site')
    parser.add_argument('--cfg', metavar='CFG', dest='cfg', default='petri.cfg',
                        type=lambda x: path(x, parser),
                        help='Configuration file to use')

    args = parser.parse_args()

    cfg = configparser.ConfigParser()
    cfg.read(args.cfg)

    sites = [
             #petridish.sites.VXVault(),
             petridish.sites.Malshare(apikey=cfg['MALSHARE']['apikey']),
            ]
    for site in sites:
        site.crawl(args.n)
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
