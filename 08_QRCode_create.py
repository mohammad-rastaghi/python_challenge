import qrcode

data = 'I believe that we can reach to the edge of ML technologies and apply them into our businese with hardworking and patient'

image = qrcode.make(data)

image.save('newFactory1.png')
