from pickle import FALSE
import wifi_qrcode_generator as qr

qrCode = qr.wifi_qrcode('Shila_UZAK',False,'WPA','UP94FRyEYX')
qrCode.show()

qrCode.save('qrcode.png')