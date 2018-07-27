import argparse
import random
import math
import sys

INPUT_UNIT_NO = 2
HIDDEN_UNIT_NO = 2
OUTPUT_UNIT_NO = 1

ETA = 0.1
PATTERN_NO = 4

TRAINING_NO = 20000
ERROR_MAX = 0.001

e = math.e


def gen_random():
    return random.randint(0, 1)


def sigmoid_func(net):
    return 1 / (1 + e ** -net)


def read_data(pattern_in, pattern_out):
    pass


def init_w(v, w):


def forward_propagation(p, v, w, pattern_in, h_out, o_out):



def back_propagation(p, v, w, h_out, o_out, pattern_in, pattern_out):
    pass


def get_args():
    # 準備
    parser = argparse.ArgumentParser()

    # 標準入力以外の場合
    if sys.stdin.isatty():
        parser.add_argument('output_file', help='please set ./a.out', type=str)
        parser.add_argument('input_file', help='please set xor.dat', type=str)

    # 結果を受ける
    args = parser.parse_args()

    return (args)


def main():



if __name__ == '__main__':
    main()
