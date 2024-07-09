def find_district():

  import pandas as pd
  import numpy as np
  import warnings
  warnings.filterwarnings('ignore')

  import os

  file_path= str(input('Please add the file path here: '))
  excel_file= pd.ExcelFile(file_path)
  
  dataframes= {sheet_name: excel_file.parse(sheet_name) for sheet_name in excel_file.sheet_names}
  print(list(dataframes.keys()))
  sheet_path = str(input(f'Please add the sheet path here: '))
  df= dataframes[sheet_path]

  df_temp= df.copy()
  df_temp.columns= df_temp.columns.str.lower()

  correct_columns= []

  for i in range(len(df_temp.columns)):
    correct_columns.append(df_temp.columns[i].strip())

  df_temp.columns= correct_columns
  print([i for i in df_temp.columns])

  column_path= str(input('Please add the column name here: '))
  column_path= column_path.lower()
  print(column_path)

  #df_temp[column_path].fillna('No Address', inplace= True)
  df_temp[column_path]= df_temp[column_path].str.lower()


  anatolia_neighbourhood_pattern= 'yeni sahra|güzeltepe|kavacık|anadolu feneri|yakacıkyeni|burhaniye|sofular|azizmahmuthüdayi|taşdelen|kandilli|polonezköy|erenköy|hürriyet|erenler|gülbahar|gülsuyu|satmazlı|yenidoğan|mehmet akif ersoy|zühtüpaşa|yunusemre|ağaçdere|öğümce|fatihsultanmehmet|uğurmumcu|alemdağ|sahrayıcedit|hacı kasım|orhantepe|küplüce|turgutreis|esenşehir|feyzullah|kordonboyu|veyselkarani|baklacı|gümüşpınar|esenkent|uğur mumcu|yakacıkçarşı|esenler|sapan bağları|evliya çelebi|hilal|muratreis|görele|zeynepkamil|çift mahalle bilgisi|akfırat|i̇çmeler|soğanlık|kızılca|kurna|nizam|altıntepe|mehmetakif|eyüpsultan|şerifali|ulupelit|yeniçamlıca|murat reis|zeynep kamil|merdivenköy|paşabahçe|emirli|namıkkemal|acarlar|fındıklı|kısıklı|eğitim|soğullu|tepeören|mimarsinan|dudullu osb|üvezli|hacıkasım|hacıllı|i̇saköy|anadolu kavağı|cami|sahrayı cedit|ünalan|harmandere|bostancı|girne|ahmediye|yalı|aziz mahmut hüdayi|selamiali|yayla|şeyhli|anadolu|bozhane|huzur|19 mayıs|yakacık yeni|esatpaşa|örnekköy|kuzguncuk|baltalimanı|veysel karani|osmangazi|rasimpaşa|kervansaray|salacak|bıçkıdere|çengeldere|göksu|soğuksu|yukarı|göçe|i̇shaklı|ertuğrul gazi|yavuzselim|barbaros|bozgoca|karabeyli|armağanevler|ortaçeşme|anadolukavağı|petroli̇ş|çavuşoğlu|kurtköy|çamlıbahçe|küçük çamlıca|yeniköy|postane|batı|dudulluosb|cemilmeriç|ahmetyesevi|kirazlıtepe|çelebi|namık kemal|soğukpınar|aydınevler|paşamandıra|mehmetakifersoy|sultantepe|doğancılı|gökmaşlı|doğu|eyüp sultan|kirazlıdere|yunus|caferağa|göztepe|ferhatpaşa|atalar|fevzi çakmak|çamçeşme|i̇stasyon|güllübağlar|suadiye|i̇cadiye|sülüntepe|yalıköy|güzelyalı|fatih|adem yavuz|merkez|alibahadır|tatlısu|acıbadem|şifa|aydıntepe|mahmut şevket paşa|soğanlık yeni|site|sırapınar|hüseyinli|mimar sinan|çengelköy|esenevler|finanskent|koşuyolu|mescit|valide-iatik|cevizli|orhangazi|avcıkoru|i̇stiklal|başıbüyük|küçükçamlıca|sapanbağları|maslak|mustafakemal|ertuğrulgazi|ballıca|kemal türkler|anadoluhisarı|ferah|güllü bağlar|yenimahalle|cemil meriç|dumlupınar|topağacı|feneryolu|kurfallı|aşağıdudullu|esenceli|şuayipli|abdurrahmangazi|kemaltürkler|aşık veysel|oruçoğlu|alacalı|yeşilvadi|hasanpaşa|yeni|çiğdem|orta|ağva|karacaköy|mahmutşevketpaşa|yeni mahalle|saray|mevlana|yenisahra|yakacık çarşı|aşağı dudullu|akçakese|emek|kavakpınar|göllü|sultançiftliği|ramazanoğlu|valide-i atik|yavuztürk|tepeüstü|çiftlik|gümüşsuyu|büyükbakkalköy|fatih sultan mehmet|aşıkveysel|i̇mrenli|çayırbaşı|çubuklu|safa|kozyatağı|akpınar|mustafa kemal|osmanköy|i̇dealtepe|reşadiye|kalem|i̇ncirköy|kabakoz|kazımkarabekir|karlıktepe|bahçelievler|kılıçlı|esenyalı|teke|küçükbakkalköy|sortullu|küçükyalı|çataklı|burgazada|orhanlı|poyrazköy|dudullu|bağlarbaşı|fetih|i̇çerenköy|adil|çavuş|geredeli|çamlık|altunizade|necip fazıl|deriosb|çatalmeşe|osmanağa|necipfazıl|yaka|hekimbaşı|ekşioğlu|atatürk|altayçeşme|belirtilmemiş|velibaba|kumbaba|ahmet yesevi|19mayıs|cumhuriyet|petroliş|i̇nönü|petrol i̇ş|selami ali|fevziçakmak|aydınlı|heybeliada|gülensu|ovacık|i̇nkılap|zümrütevler|battalgazi|sanayi|göçbeyli|çınardere|kadıköy|akbaba|kuleli|selimiye|çengilli|kaynarca|yamanevler|kınalıada|çakmak|rüzgarlıbahçe|turgut reis|yavuz selim|örnek|mehmet akif|altınşehir|meclis|kömürlük|atakent|yunus emre|kayışdağı|madenler|akşemsettin|küçüksu|ihlamurkuyu|beylerbeyi|değirmençayırı|bulgurlu|tokatköy|yenişehir|sahilköy|bucaklı|anadolufeneri|fenerbahçe|hamidiye|deri osb|dereseki|zerzavatçı|aydınlar|maden|ademyavuz|kanlıca|parseller|tantavi|sarıgazi|ahmetli|yazımanayır|nişantepe|anadolu hisarı|i̇mrendere|garipçe|ömerli|paşaköy|elmalı|balibey|mecidiye|kurtdoğmuş|koçullu|caddebostan|riva|karamandere|hasanlı|esentepe|merve|yukarı dudullu|elmalıkent|petrol iş|çiftmahallebilgisi|yeni çamlıca|kazım karabekir|yeşilbağlar|yukarıdudullu|güngören|karakiraz|çınar|meşrutiyet|korucu|soğanlıkyeni|yayalar|darlık|evliyaçelebi|topselvi|fikirtepe'
  anatolia_district_pattern= 'maltepe|pendik|ataşehir|şile|beykoz|sarıyer|tuzla|kartal|i̇stanbul|adalar|sancaktepe|ümraniye|sultanbeyli|üsküdar|kadıköy|şişli|çekmeköy'

  europe_neighbourhood_pattern= 'ovayeni̇ce |şehi̇tler |molla gürani̇|i̇nceği̇z |deni̇zköşkler|osmangazi̇|cevi̇zli̇k |kültür |bi̇nbi̇rdi̇rek |celali̇ye |vatan |güzeltepe|süleymani̇ye|kocataş |ahmedi̇ye |yeşi̇lova |gökevler|atatürk |ati̇kali̇ |uskumruköy |büyükkiliçli|gümüşpala|i̇nci̇rtepe|ali̇beyköy |si̇li̇vri̇kapi|yahya kemal|rumeli̇ hi̇sari |hali̇l rifat paşa|nuri̇paşa |yassiören|celepköy|gençosman|aşik veysel |neci̇p fazil kisakürek |menderes|ormanli|çakil |si̇nanoba|kalenderhane|ömeravni̇|bahçeköyyeni̇|kamer hatun|büyük kiliçli|uğur mumcu |altintepsi̇|muradi̇ye|gülbahar|mevlana |ataköy2-5-6.kisim|gazi̇tepe|paşa|deni̇zköşkler |çakmakli|sümbül efendi̇|rumeli̇ hi̇sari|merkez |basinköy |süleymani̇ye |akşemsetti̇n|menderes |seyrantepe|sakarya |çinar |şehremi̇ni̇ |yunusemre|bebek |gazi̇ |yeni̇gün|şahkulu|yedi̇kule|haciahmet |beşyol|koca mustafapaşa |maden |büyük kiliçli |akincilar|talatpaşa|ki̇reçburnu|mustafa kemal paşa|büyüksi̇nekli̇|ptt evleri̇ |meşruti̇yet |gümüşyaka|yeşi̇lova|baklali|rumeli̇feneri̇|turgutrei̇s|uğurmumcu|ataköy3-4-11.kisim|göztepe |akşemsetti̇n |fati̇h sultan mehmet |çi̇ftehavuzlar|levent|di̇ki̇li̇taş|mavi̇göl|duatepe |beyci̇ler |haseki̇ sultan|göktürk merkez |ali̇paşa|kumburgaz|dervi̇ş ali̇ |yavuzsultanseli̇m|hacimi̇mi̇|rumeli̇ kavaği |esenkent|kati̇pmustafaçelebi̇|19 mayis|akören|bahçeköy kemer|uğur mumcu|bahçeşehi̇r 2. kisim|yarimburgaz|demi̇rtaş|çukur |yeni̇doğan |karamandere |zuhuratbaba |kuruçeşme|kisirkaya|kati̇p mustafa çelebi̇|yahyakemal|si̇lahtarağa |karlibayir |fi̇ruzağa|pi̇ri̇rei̇s|küçük ayasofya|bahçeşehi̇r 1. kisim |muratbey merkez |celali̇ye|hali̇deedi̇padivar|demi̇rci̇ |şehi̇tler|mustafakemalpaşa|çirçir|emni̇yet|i̇sti̇klal|yeni̇|orhan gazi̇|çelti̇k|di̇ki̇li̇taş |kemal paşa|ci̇bali̇|75. yil |akçaburgaz|kati̇pkasim|karadeni̇z |balabanağa|zuhuratbaba|çanta sancaktepe|mehterçeşme |i̇skenderpaşa |15 temmuz|şehi̇tmuhtar|seyyi̇dömer|neci̇p fazil kisakürek|pi̇ri̇ rei̇s|ki̇reçburnu |yeni̇bosna |harbi̇ye |türkali̇|sariyermerkez|duatepe|ni̇şanci|nenehatun |güzelce|dervi̇ş ali̇|pi̇yalepaşa |di̇zdari̇ye |tuna|karagümrük|sakizağaci |ni̇şanci |sultanahmet|kavakli |hocagi̇yasetti̇n|akevler |mehmet aki̇f ersoy|çayirbaşi |halaskargazi̇|pi̇ri̇nççi̇ |nuri̇paşa|yeni̇ |mustafa kemal paşa |akevler|gümüşdere |terazi̇dere|boğazköy i̇sti̇klal|terazi̇dere |esenkent |rami̇yeni̇|yeşi̇lpinar |sakizağaci|ortabayir|hali̇l rifat paşa |ulus|darüşşafaka|kazliçeşme|koza|pi̇ri̇nççi̇|yunus emre |yeni̇kent |mi̇mar hayretti̇n |subaşi|gençosman |durusu|boyalik|karadolap |ayvansaray |başak|mevlanakapi |fevzi̇ çakmak |çobançeşme |yeşi̇lyurt |telsi̇z |zeyrek|tahtakale|yeşi̇ltepe|ergenekon|çi̇li̇ngi̇r|bereketzade|yeşi̇lköy |küçük pi̇yale|yeşi̇lce |ergenekon |üçevler|i̇nci̇rtepe |kisirkaya |50.yil|ataköy 2-5-6. kisim |cebeci̇ |yakuplu |akçaburgaz |gültepe |akşemseddi̇n|sazlibosna |koza |üçevler |yavuz sultan seli̇m|muhsi̇nehatun|harmantepe|yeni̇ mahalle|sayalar|darüşşafaka |muratçeşme|si̇lahtarağa|yayla|yaliköy |tuna |üni̇versi̇te |muratbeymerkez|büyük si̇nekli̇|gökçeali̇ |anadolu|huzur|abbasağa |kavakli i̇sti̇klal|hacimaşli|hürri̇yet|şamlar |levazim |nakkaş |namik kemal |mercan |deli̇kli̇kaya|ali̇ kuşçu|ayvansaray|veli̇efendi̇ |balaban|muratbey merkez|havaalani |yedi̇kule |hallaçli|karaburun |arnavutköymerkez|yavuzseli̇m|baklali |sancaktepe|hali̇de edi̇p adivar|emni̇yettepe|pi̇ri̇ mehmet paşa|bereketzade |tevfi̇kbey|hoca gi̇yasetti̇n|battalgazi̇ |başak |i̇smetpaşa |gürsel |bahçeşehi̇r2.kisim|bülbül |rami̇ cuma |mesi̇hpaşa |haseki̇sultan|hallaçli |kaptanpaşa|muratpaşa|osmangazi̇ |rüstempaşa|küçük si̇nekli̇|kazim karabeki̇r|barbaros|levazim|kalyoncukulluğu|50. yil |eki̇noba|bolluca|sayalar |hi̇cret|mehmetaki̇fersoy|yeşi̇lyurt|yeşi̇lce|harbi̇ye|aydinlar |bahçeli̇evler|murat çeşme|eti̇ler|emni̇yet |ortabayir |ataköy 7-8-9-10. kisim |ardiçli|tarabya |gökalp |tevfi̇k bey|mi̇marhayretti̇n|cerrahpaşa |hadimköy|seli̇mpaşa|bebek|beşyol |soğanli |rüstem paşa|bozkurt|yildiztepe |alemdar|çakil|asmali mesci̇t|yahyakahya|cebeci̇|neci̇pfazilkisakürek|kartaltepe|soğanli|bedretti̇n |bağlarçeşme|şenli̇kköy|defterdar |muratpaşa |gürpinar |feti̇htepe|emi̇rgan|bariş |mi̇mar kemaletti̇n |pi̇ri̇ rei̇s |saridemi̇r |abdurrahman nafi̇z gürman |gazi̇tepe |100.yil|bahçeköykemer|fi̇ruzköy |kavakli|ci̇hangi̇r |fi̇ruzağa |huzur |ci̇hangi̇r|ataköy 3-4-11. kisim |cami̇i̇kebi̇r|deği̇rmenköy i̇smetpaşa|yildirim |kalfa |si̇nanoba |sarigöl |yeşi̇lkent |bostan |mareşalçakmak|boğazköyi̇sti̇klal|yildiztabya|ardiçli |keçeci̇ pi̇ri̇|75. yil|dursunköy|hüseyi̇nağa |kalyoncu kulluğu|bahşayi̇ş|çayirdere|molla gürani̇ |yaylacik |kiliçali̇ paşa|turgut rei̇s |kazimkarabeki̇r|yavuz seli̇m|türkoba |aksaray |işiklar|mi̇mar si̇nan|kati̇p mustafa çelebi̇ |pürtelaş |şemsi̇paşa |çayirdere |seyi̇tni̇zam|demi̇rtaş |altinşehi̇r |seymen|sariyer merkez|şi̇ri̇nevler|pi̇ri̇ paşa|cumhuri̇yet|keçeci̇pi̇ri̇|hi̇sarbeyli̇|defterdar|balmumcu |kocataş|di̇zdari̇ye|kestaneli̇k |çobançeşme|müeyyetzade |yassiören |ormanli |demi̇rkapi|ni̇nehatun|balaban |cevatpaşa|vi̇şnezade|pinartepe |muhsi̇ne hatun|selahaddi̇n eyyubi̇|boğazköy i̇sti̇klal |oklali |kemal paşa |i̇mrahor|bülbül|göztepe|ferhatpaşa|mi̇markemaletti̇n|şahi̇ntepe|sultançi̇ftli̇ği̇|molla hüsrev|5.levent|şehi̇t muhtar|arnavutköy merkez|i̇zzetti̇n|meci̇di̇ye |i̇stasyon|ayazağa |boyalik |mahmut şevket paşa |dereağzi|güneşli̇|yakuplu|arap cami̇|sururi̇|yahya kemal |yeni̇mahalle|güzeltepe |şenli̇kköy |başakşehi̇r|hali̇lrifatpaşa|kadimehmet efendi̇|barbaros hayretti̇n paşa |adnankahveci̇|nakkaş|kabakça|muhsi̇ne hatun |haraççi|türkoba|sultan ahmet|si̇yavuşpaşa |adnan kahveci̇ |danamandira |taşoluk |gülbahar |gayrettepe|hami̇di̇ye|merkez|pinartepe|güzelyurt|mi̇mar si̇nan merkez|talatpaşa |hastane |zi̇yagökalp|ali̇beyköy|türkali̇ |örnek |pi̇ri̇ mehmet paşa |çi̇ftalan |çi̇fte havuzlar|sultanseli̇m|ataköy 2-5-6. kisim|karacaköy |harmantepe |bozkurt |talatpasa |orta |mi̇thatpaşa|mevlanakapi|bağlarbaşi|sahi̇l|osmani̇ye|i̇hsani̇ye|mahmut şevket paşa|orhan gazi̇ |kami̇loba |karlitepe |tomtom|kadiköy |dağyeni̇ce|i̇sti̇nye|kalenderhane |mehterçeşme|bahçeli̇evler |küçük si̇nekli̇ |dursunköy |eti̇ler |mollafenari̇|hami̇di̇ye |adnan kahveci̇|dereağzi |kaptanpaşa |kemankeşkaramustafapaşa|mavi̇göl |yeşi̇lbayir |odayeri̇|celepköy |beyazit|bahçeköy merkez|sanayi̇ |sümbülefendi̇|i̇nönü |maslak|evli̇ya çelebi̇ |barbaroshayretti̇npaşa|topçular|büyük si̇nekli̇ |bağlar|aydinlar|sultan murat|maltepe |yaliköy|çukur|kami̇loba|saadetdere|ki̇razli|kati̇p kasim|bi̇rli̇k |çelti̇k |deği̇rmenköyi̇smetpaşa|kuloğlu |tayakadin|havaalani|bostan|bariş|merkezefendi̇ |nenehatun|akincilar |bahçeşehi̇r 1. kisim|zi̇ya gökalp|hoca paşa |kadimehmetefendi̇|zekeri̇yaköy|turgutözal|gökçeali̇|sultani̇ye |konaklar|sümer |pttevleri̇|büyükçavuşlu|yolçati|cennet|şehremi̇ni̇|i̇hsani̇ye |beyci̇ler|yeşi̇lpinar|şemsi̇paşa|karlitepe|düğmeci̇ler |hürri̇yet |esentepe |hüseyi̇nağa|ali̇ kuşçu |molla hüsrev |çirpici|hastane|fevzi̇ çakmak|aşikveysel|terkos |marmara |kazliçeşme |elbasan |deli̇kli̇kaya |barbaros hayretti̇npaşa|mehmet aki̇f |güverci̇ntepe |büyükdere|balikyolu |abdurrahmannafi̇zgürman|kocasi̇nan |kestaneli̇k|sarigöl|i̇slambey|bahşayi̇ş |göktürkmerkez|emekyemez|balabanağa |halicioğlu|100. yil|şi̇ri̇ntepe|orta|ağaçli|düğmeci̇ler|gümüşsuyu |örenci̇k |karacaköy|bağlarçeşme |sakarya|mahmutşevketpaşa|si̇li̇vri̇kapi |ali̇bey |habi̇bler|seyi̇tni̇zam |kemer|güzelce |mi̇maroba |ömerli̇|basinköy|ati̇kali̇|seyyi̇d ömer|kemalpaşa |fener|saadetdere |mevlana|anadolu |gümüşyaka |mareşal fevzi̇ çakmak|davutpaşa |şehi̇t muhtar |yildiztepe|müeyyetzade|demi̇rkapi |danamandira|ataköy 3-4-11. kisim|mi̇mar hayretti̇n|çi̇fte havuzlar |asmalimesci̇t|fati̇h|turgut özal|emekyemez |habi̇bler |şahkulu |subaşi |haznedar |abdurrahman nafi̇z gürman|topkapi |oruçrei̇s |çeli̇ktepe |yeni̇mahalle |maslak |yildiztabya |bi̇nbi̇rdi̇rek|kanarya|bahçeköymerkez|sümer|yildiz |rami̇cuma|kavakli hürri̇yet|malkoçoğlu |demi̇rci̇|söğütlüçeşme|örcünlü|tarabya|cevi̇zli̇k|telsi̇z|ulus |gümüşsuyu|karadeni̇z|feri̇köy |arnavutköy merkez |çi̇ftli̇kköy|atakent |altinşehi̇r|terkos|oruçrei̇s|ni̇şanca|gültepe|poli̇gon|pinar |kayabaşi|halkali|eski̇şehi̇r|gümüşpinar |mehmetaki̇f|gümüşdere|ömer avni̇|kulaksiz |akpinar |pinar|namik kemal|marmara|sultan seli̇m|kemankeş karamustafa paşa|karayollari|bahçeşehi̇r1.kisim|üni̇versi̇te|çatmamesci̇t|rami̇ yeni̇ |rüstem paşa |pazari̇çi̇|ferahevler|hadimköy |yayla |kulaksiz|karaburun|halkali |hacimi̇mi̇ |kocatepe|seyyi̇d ömer |bi̇rli̇k|alkent |abbasağa|balat|mehmetnesi̇hözmen|fi̇ruzköy|kurfalli|ferahevler |ambarli|güneşli̇ |dağyeni̇ce |teşvi̇ki̇ye |yeşi̇lkent|kocatepe |kuştepe|ambarli |ataköy 1. kisim |ataköy1.kisim|si̇yavuşpaşa|hi̇cret |gürpinar|feti̇htepe |kalei̇çi̇ |kamerhatun|mollagürani̇|çirçir |bağlarbaşi |reşi̇tpaşa|tayakadin |yolçati |altintepsi̇ |kalfa|kuloğlu|osmani̇ye |i̇sti̇klal |i̇slambey |haraççi |karadolap|topçular |hoca gi̇yasetti̇n |mercan|kumköy |veli̇efendi̇|şi̇ri̇nevler |yarimburgaz |konaklar |hobyar |kartaltepe |tomtom |molla fenari̇|kati̇p kasim |semi̇zkumlar|pi̇ri̇mehmetpaşa|meşruti̇yet|50. yil|söğütlü çeşme|saridemi̇r|cennet |selahaddi̇n eyyubi̇ |mi̇maroba|rumeli̇hi̇sari|mi̇marsi̇nanmerkez|adnanmenderes|mahmutbey |işiklar |kuruçeşme |alemdar |yeşi̇lköy|kanarya |kültür|çi̇ftli̇kköy |sultanmurat|haciahmet|5. levent|ortaköy|arnavutköy |deği̇rmenköyfevzi̇paşa|ayazağa|kiliçali̇paşa|akalan |sanayi̇|beştelsi̇z|vi̇şnezade |yavuz sultan seli̇m |karayollari |akalan|atatürk|kocasi̇nan|beştelsi̇z |maltepe|yeni̇şehi̇r |kadiköy|çamlitepe|bahçeşehi̇r 2. kisim |baltali̇mani|ataköy 1. kisim|seli̇mpaşa |büyükşehi̇r|çakmakli |nurtepe|aşik veysel|yeşi̇ltepe |mareşalfevzi̇çakmak|evli̇yaçelebi̇|i̇nönü|meci̇di̇yeköy |şi̇ri̇ntepe |hocapaşa|hirka-i̇ şeri̇f|rumeli̇feneri̇ |aksaray|ahmedi̇ye|kavaklihürri̇yet|elbasan|akören |seymen |barbaros hayretti̇n paşa|mareşal çakmak|güven |ali̇bey|feri̇köy|göktürk merkez|talatpasa|kumköy|koca mustafapaşa|mesi̇hpaşa|yeşi̇lbayir|kurfalli |fulya|yeni̇doğan|oklali|meci̇di̇yeköy|i̇smet paşa|haznedar|bağlar |barbaros |yeni̇köy|sütlüce|cerrahpaşa|evli̇ya çelebi̇|mollahüsrev|muradi̇ye |ni̇şanca |pi̇ri̇paşa|çinar|tozkoparan |hirka-i̇şeri̇f|karlibayir|pazari̇çi̇ |vatan|davutpaşa|selahaddi̇neyyubi̇|çayirbaşi|sultan murat |turgut özal |i̇sti̇nye |gürsel|küçükayasofya|zeyti̇nli̇k|halicioğlu |rumeli̇ kavaği|ali̇paşa |kemalpaşa|fati̇hsultanmehmet|ağaçli |küçükpi̇yale|i̇skenderpaşa|örnek|çanakça |ali̇kuşçu|yeni̇ mahalle |akat|karaağaç |molla fenari̇ |sultançi̇ftli̇ği̇ |gazi̇|ni̇ne hatun|gari̇pçe|yeni̇bosna|ni̇sbeti̇ye |yavuz seli̇m |pi̇yalepaşa|örenci̇k|atakent|15temmuz|si̇nanpaşa|çatma mesci̇t|topkapi|ataköy 7-8-9-10. kisim|çantasancaktepe|balat |yunus emre|yahya kahya |mi̇mar si̇nan |karagümrük |yildirim|kuştepe |büyükşehi̇r |levent |taşoluk|yildiz|hi̇sarbeyli̇ |orhangazi̇|güneştepe|gari̇pçe |cankurtaran|fati̇h |hobyar|malkoçoğlu|bahçeköy yeni̇|gümüşpinar|çağlayan |19mayis|çanakça|zeyrek |örcünlü |zafer|telsi̇zler|mehmet aki̇f|büyük çavuşlu|ci̇hannüma|merkezefendi̇|mi̇mar si̇nan merkez |şamlar|sururi̇ |emni̇yettepe |ci̇bali̇ |uskumruköy|akşemseddi̇n |ptt evleri̇|ki̇razli |tozkoparan|teşvi̇ki̇ye|maden|yeni̇kent|adnan menderes|kabakça |kemer |bahçeköy kemer |meci̇di̇ye|mehmet nesi̇h özmen|örnektepe|balikyolu|sancaktepe |küçüksi̇nekli̇|turgut rei̇s|i̇nceği̇z|sütlüce |karaağaç|güneştepe |hoca paşa|yeni̇şehi̇r|sazlibosna|akpinar|güven|gümüşpala |büyük çavuşlu |cumhuri̇yet |rami̇ cuma|namikkemal|pürtelaş|balmumcu|rami̇ yeni̇|hacimaşli |kavaklii̇sti̇klal|zafer |rumeli̇kavaği|eki̇noba |battalgazi̇|hali̇de edi̇p adivar |poli̇gon |yahya kahya|cevatpaşa |mi̇thatpaşa |75.yil|cami̇i̇kebi̇r |karamandere|seyrantepe |fati̇h sultan mehmet|çi̇ftalan|ovayeni̇ce|mi̇mar kemaletti̇n|büyükdere |esentepe|tahtakale |güverci̇ntepe|ni̇sbeti̇ye|yeni̇gün |i̇smetpaşa|nurtepe |telsi̇zler |çeli̇ktepe|beyazit |dervi̇şali̇|eski̇şehi̇r |mehmet aki̇f ersoy |gökalp|çağlayan|yeni̇köy |ci̇hannüma |si̇nanpaşa |kalei̇çi̇|odayeri̇ |kocamustafapaşa|yaylacik|ataköy7-8-9-10.kisim|paşa |sahi̇l |bedretti̇n|arnavutköy|deği̇rmenköy fevzi̇paşa|zekeri̇yaköy |mi̇marsi̇nan|sultani̇ye|fener |ortaköy |arapcami̇|fevzi̇çakmak|alkent|gayrettepe |mahmutbey|ferhatpaşa '
  
  europe_district_pattern= 'sultangazi|silivri|eyüpsultan|büyükçekmece|beşiktaş|beylikdüzü|bakırköy|şişli|kağıthane|esenyurt|esenler|bayrampaşa|sarıyer|fatih|başakşehi̇r|gaziosmanpaşa|zeytinburnu|avcılar|bağcılar|küçükçekmece|güngören|arnavutköy|çatalca|beyoğlu|bahçelievler'

  def find_district(address, district_list):
    for district in district_list:
        if district in address:
            return district
    return np.nan

  region= str(input('Lütfen temizlemek istediğiniz bölge adını yazınız(ANADOLU - AVRUPA): '))

  if region.upper()== 'ANADOLU':

    district_list= anatolia_neighbourhood_pattern.split('|')
    df_temp[f'{region} Mahalle'] = df_temp[column_path].apply(find_district, district_list=district_list)

    district_list= anatolia_district_pattern.split('|')
    df_temp[f'{region} İlçe']= df_temp[column_path].apply(find_district, district_list=district_list)

  if region.upper() == 'AVRUPA':
    district_list= europe_neighbourhood_pattern.split('|')
    df_temp[f'{region} Mahalle'] = df_temp[column_path].apply(find_district, district_list=district_list)
    district_list= europe_district_pattern.split('|')
    df_temp[f'{region} İlçe']= df_temp[column_path].apply(find_district, district_list=district_list)

  file_name= str(input('Please Select a File Name: '))
  df_temp.to_excel(f'{file_name}.xlsx')

  return df_temp