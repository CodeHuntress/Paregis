# Pareģis
Lapa, kas piedāvā Tev uzzināt dažādas lietas aizraujošos veidos. Šajā lapā būs iespējams uzzināt savu veiksmi, veikt testus, kuros atbildot uz dažādiem jautājumiem uzzināsiet ko jaunu par sevi.
## Saturs:
1.Pareģa sadaļas
2.Instalēšana 
3.Lietošana 
 
Pareģa sadaļas
#### 1 lapa - titullapa
Atverot lapu tiek piedāvāts sākt šo testu/spēli "Pareģis", tomēr jau pašā sākumā ar humoru tiek sākta spēle. Trīs reizes spiežot pogu "Sākam!" parāda paziņojumu, ka ir nepieciešams inputs no klaviatūras, lai tiktu pie nākamajiem uzdevumiem.

#### 2-4 lapa - veiksme
Pieci jautājumi ar 3 atbilžu variantiem, atbildot uz jautājumiem tiek savākts noteikts punktu skaits. 

#### 5-7 lapa - atbildes
No savāktā punktu skaita tiek notiekts, cik liela 'veiksme' ir gaidāma šodien. 

#### 8 lapa - horoskops
Atzīmējot savu horoskopu tiek piedāvāts dienas horoskops un iedegas viena no 12 diodēm stendā.

#### 9 lapa - laika prognoze
Tiek dotas 3 pogas un nospiežot tās tiek, piemēram, ieslēgtas diodes vai ventilātors, lai attēlotu laikapstākļus un prognozētu/pareģotu gaidāmos vai esošos laikapstākļus. 

## Instalēšana
Pareģim nav nepieciešamas daudz, dažādas detaļas. Tā veidošanai tika izmantots Raspberry Pi3 un Flask.
Tā instalēšanas norādes var atrast šeit: https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/2
Nepieciešamas ir arī visas mūsu izveidotās mājas lapas ar to kodiem kuras atradīsiet failā pogs.zip šīs lapas sākumā.

## Lietošana
Vispirms ir jāieslēdz Rspberry Pi un jāpieslēdzas kādai no programmām uz kurām rediģēt un rakstīt Raspberry PI skriptu(Putty https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html, Mobaxterm https://mobaxterm.mobatek.net/). No "Pareģis" GitHub lapas vajag lejuplādēt failu "pogs" un iekopēt to jūsu izvēlētajā programmā.
Lai palaistu lapu, terminālajā logā jāieraksta šāda fuunkcija:
#### sudo python pogs.py

Interneta serverī jāieraksta Raspberry PI IP adrese un ports uz kura darbojas lapa9(Katram ietotājam atšķirsies).
#### Piemēram: 196.184.43.269:80
Tālāk tikai nepieciešams atbildēt uz lapās prasīto un ar prieku izmantot Pareģi!

Vairāk info: http://flask.pocoo.org/
