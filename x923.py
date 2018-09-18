from math import ceil

from pypadding.base import BaseEncoder


class Encoder(BaseEncoder):    
    def encode(self, src: bytes) -> bytes:
        src_len = len(src)
        block_number = ceil((src_len+1)/self.block_size)
        pad_size = block_number * self.block_size - src_len
        return src + bytes([0] * (pad_size-1)) + bytes([pad_size])

    def decode(self, encoded_bytes):
        pad_size = encoded_bytes[-1]
        return encoded_bytes[:-pad_size]
