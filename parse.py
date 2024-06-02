import urllib.request

url = 'https://www876.ff-02.com/token=zxuuivYtnAhiCFJ5_VQ_VA/1679351616/201.240.0.0/22/3/1f/8a3a8f77a2b7944c017efd37070381f3-480p.mp4'
try:
    x = urllib.request.urlopen(url)
    print('La URL es válida')
except urllib.error.URLError:
    print('La URL es inválida o no se puede acceder a ella')
