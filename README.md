BIP5 kellon sää on paska, koska se on Accuweather, eikä ymmärrä paikallisia olosuhteita.

Onneksi siellä on appi nimeltä HTTP, joka osaa tehdä WGET ja näyttää sen tekstin.

Tein tämmösen serverin Termuxiin, joka hakee Supersaa.fi:sta kamaa 20 minsan välein
ja parsii sen yhdeksi tekstiriviksi.
Se myös näyttää vuoronperään joko Forecan tai Ilmailulaitoksen ennusteen.

HTTP-appissa: Title: Sää, Method: GET, URL: http://0.0.0.0:9090, Icon: Sateenvarjo

Lisäksi Exit on Succes: OFF ja Toast on Success: ON

Testaus Linuksissa:  curl 192.168.1.198:9090

Tulos esimerkiksi: F 17:40 23° Etelä 199° 1m/s Selkeää



