__author__ = 'winterflower'
"""
Slow Poetry Server based on the tutorial by Dave Peticolas (see README for link)
"""

import argparse,os, socket,time

def create_parser():
    usage="""Usage: %prog [options] poetry-file
    This is slow blocking server, which serves Sylvia Plath's poetry \n

    To run this server, open a terminal and execute \n

    python slowpoetryserver.py <poetryfile>

    """
    parser=argparse.ArgumentParser(usage)
    return parser
