from zlib import compress
import sys

img = open('busy-digital-nomad-female-452768.jpg', 'rb').read()
compressed_img = compress(img, level=1)
print('Raw size:', sys.getsizeof(img))
print('Compressed size:', sys.getsizeof(compressed_img))


save_compressed = open('digital.png', 'ab')
save_compressed.write(compressed_img)
save_compressed.close()
