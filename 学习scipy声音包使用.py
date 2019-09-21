##
from scipy.io import wavfile
like = wavfile.read('./output.wav')


'''
返回的第一个数值,表示1s 内有多少个数,
第二个是numpy数组,表示所有的音

'''





##
print(like[1])

print(like[1].shape)
#这个项目里面用的是1s 2万的采样.



