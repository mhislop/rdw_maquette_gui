# RDW Maquette GUI

Dit is de repository van de RDW Maquette GUI. In deze repository is de interface te vinden die wordt gebruikt om de stoplichten individueel op afstand te besturen. De Micro-SD kaart voor de raspberry pi die meegegeven is tijdens de overdracht is al opgezet en deze kan direct gebruikt worden om de interface te starten. Mocht het zo zijn dat de Micro-SD niet te gebruiken is vanwege redenen, dan moet de setup van de Raspberry Pi eenmalig opnieuw gedaan worden. Zie onder **Eenmalige setup als SD-kaart geformatteerd is of niet gebruikt kan worden** voor alle stappen die doorlopen moeten worden. Als dit niet het geval is en de SD-kaart kan gewoon gebruikt geworden. Volg dan de stappen onder **Stappen voor starten van interface**

## Stappen voor starten van interface ##
Als eerst moet er verbinding gemaakt worden met de raspberry pi en de laptop. Dit wordt gedaan door middel van SSH + VNC Server. 

### Verbinden met Raspberry Pi via SSH + VNC server ###
1. Plaatst de SD-kaart in de Raspberry Pi 
2. Sluit de Raspberry Pi aan.
3. Gebruik een UTP kabel en verbind deze met de Raspberry Pi en jouw laptop.
4. Installeer PuTTY (windows) of open Terminal (Mac) en voer de volgende stap uit.
   - PuTTY: stel in op *ssh* en host *raspberry.local*
   - Terminal: *ssh pi@raspberry.local*
5. Je ziet de password-prompt van de Raspberry PI. Tik in 
*raspberry* (default wachtwoord) en je hebt een ssh verbinding gelegd met de Raspberry PI in de terminal
5. Download en installeer [VNC server](https://www.realvnc.com/en/connect/download/vnc/)
6. Type in de terminal waar je SSH-verbinding hebt gemaakt: *vncserver*
7. Noteer laatste regel dat de vorm heeft van raspberrypi:1 (ip-addres:1)
8. Open het programma VNC Viewer en tik in het hostnaam-adres dat je 
genoteerd hebt: *raspberrypi.local:1* (let op: woord .local is toegevoegd)
9. Je ziet de Raspberry PI Desktop GUI op jouw laptop. Je kan nu via de grafische GUI werken 
alsof je een monitor en toetsenbord rechtstreeks aan de Raspberry Pi hebt gekoppeld.

## Opstarten interface ##
Nadat er verbinding is gemaakt met de Raspberry Pi. Dan kan de interface gestart worden op de volgende twee manieren:
1. Kant-en-klaar: Klik op de gebouwde applicatie genaamd: rdw_maquette_gui.exe
2. Productie:__ 
2.1 Open de terminal_
2.2 Ga naar de map rdw_maquette_gui_
2.3 Activeer de virtual env door in te typen: source env/bin/activate_
2.4 Voer in de terminal om de applicatie te runnen: python build/boot.py_

## Eenmalige setup als SD-kaart geformatteerd is of niet gebruikt kan worden ##

### Setup Micro-sd kaart (Eenmalig als SD-kaart geformatteerd is)
Benodigheden:
- Raspberry Pi 4 Model B
- Raspberry Pi voeding
- Micro-SD kaart met adapter

Stappen:
1. Mount de Micro-SD m.b.v. de adapter met je laptop
2. Maak met programma **Raspberry PI Imager** een boot SD-card
   - Link: https://www.raspberrypi.org/downloads/
   - Versie: Raspberry PI OS Desktop (32-bit) (recommended)
3. Plaats een lege file op de SD-card met de naam ssh
4. Plaats de template file **wpa_supplicant.conf** die te vinden is in de map **setup** op de SD-card
5. Wijzig in file wpa_supplicant.conf de **SSID** en **PSK** waarden met de gegevens van jouw thuis-Wifi, bewaar de nieuwe gegevens.
6. Eject de SD kaart
7. Om nu verbinding te maken met de raspberry pi, dien je de stappen onder het kopje **Verbinden met Raspberry Pi via SSH + VNC server** te volgen.
8. Nadat je verbinding hebt gemaakt de raspberry pi is het nog belangrijk om de volgende configuraties te doen voor de raspberry pi. Deze hoeven maar eenmalig gedaan te worden:
   - 8.1 Ga naar Pi menu >> Preferences >> Raspberry Pi Configuration
   - 8.2 Verander wachtwoord van de pi
   - 8.3 Verander hostname van de pi
   - 8.4 Interfaces >> enable VNC, SPI, I2C 

## Eenmalige setup repository raspberry pi
Voor het installeren van de benodigde modules wordt er gebruikt gemaakt van een virtual enviroment.
1.  Maak een nieuwe virtuele enviromenent met: *python3 -m venv /path/to/new/virtual/environment*
2.  Clone deze repository in de net aangemaakte folder
3.  Activeer de virtuale enviroment met: *source env/bin/activate*
4.  Download alle benodigde modules met: *python3 -m pip install -r /requirements.txt*

