
import argparse
import falcon
from hparams import hparams, hparams_debug_string
import os
from synthesizer import Synthesizer

from wsgiref import simple_server

parser = argparse.ArgumentParser()
parser.add_argument('--checkpoint', required=False, default='/tmp/tacotron-20180906/model.ckpt')
parser.add_argument('--port', type=int, default=9000)
parser.add_argument('--hparams', default='',
                    help='Hyperparameter overrides as a comma-separated list of name=value pairs')
args = parser.parse_args()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
hparams.parse(args.hparams)
# print(hparams_debug_string())
synthesizer = Synthesizer()

synthesizer.load('/tmp/tacotron-20180906/model.ckpt')
res=synthesizer.synthesize('apple i eat')#所以res是 一堆数字的编码
print(res)
print("结果保存在ouput.wav里面")













