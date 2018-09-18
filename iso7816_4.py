from math import ceil

from pypadding.base import BaseEncoder


class Encoder(BaseEncoder):
    def encode(self, src: bytes) -> bytes:
        src_len = len(src)
        block_number = ceil((src_len+1)/self.block_size)
        pad_size = block_number * self.block_size - src_len
        return src + b'\x80' + bytes([0] * (pad_size-1))

    def decode(self, encoded_bytes):
        for idx, byte in enumerate(reversed(encoded_bytes)):
            pad_size = 0
            if bytes([byte]) == b'\x80':
                pad_size = idx+1
                break
        return encoded_bytes[:-pad_size]


if __name__ == '__main__':
    encoder = Encoder()

    test_samples = ['hello', 'computer', 'blackjack', 'crystallization', 'hydroelectricity']
    encoded_samples = []

    for sample in test_samples:
        test_bytes = sample.encode()
        print('src:', test_bytes, 'len:', len(test_bytes))
        encoded_bytes = encoder.encode(test_bytes)
        print('encoded:', encoded_bytes, 'len:', len(encoded_bytes))
        encoded_samples.append(encoded_bytes)
        print('##########')

    print('/////////////////////////////////////////')

    for sample in encoded_samples:
        print('encoded:', sample, 'len:', len(sample))
        src_bytes = encoder.decode(sample)
        print('src:', src_bytes, 'len:', len(src_bytes))
        print('##########')