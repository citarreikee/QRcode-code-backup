import zxing

reader = zxing.BarCodeReader()
im = input("请输入文件名：")
barcode = reader.decode(im)
print(barcode.parsed)