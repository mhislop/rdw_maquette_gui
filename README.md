# RDW Maquette GUI

Dit is de repository van de RDW Maquette GUI. In deze repository is de interface te vinden die wordt gebruikt om de stoplichten individueel op afstand te besturen. De micro-sd kaart voor de raspberry pi die meegegeven is tijdens de overdracht is al opgezet en deze kan direct gebruikt worden om de interface te starten. Mocht het zo zijn dat de micro-sd niet te gebruiken is vanwege redenen, dan moet de setup eenmalig opnieuw gedaan worden. Om verbinding te maken met de raspberry pi kan de gevolgd worden. 

## Setup Micro-sd kaart (Eenmalig als SD-kaart geformatteerd is)
Benodigheden:
- Raspberry Pi 4 Model B
- Micro-SD kaart met adapter
- UTP Kabel (aanrader) of telefoon met mobiel network 

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
   8.1 Ga naar Pi menu >> Preferences >> Raspberry Pi Configuration
   8.2 Verander wachtwoord van de pi
   8.3 Verander hostname van de pi
   8.4 Interfaces >> enable VNC, SPI, I2C 

## Verbinden met Raspberry Pi via SSH + VNC server
1. Plaatst de SD-kaart in de Raspberry Pi 
2. Sluit de Raspberry Pi aan.
3. Installeer PuTTY (windows) of open Terminal (Mac) en voer de volgende stap uit.
   - PuTTY: stel in op **ssh** en host **raspberry.local**
   - Terminal: ssh pi@raspberry.local
4. Je ziet de password-prompt van de Raspberry PI. Tik in 
raspberry (default wachtwoord) en je hebt een ssh verbinding gelegd met de Raspberry PI (terminal mode)
5. Download en installeer [VNC server](https://www.realvnc.com/en/connect/download/vnc/)
6. Type in de terminal waar je SSH-verbinding hebt gemaakt: vncserver
7. Noteer laatste regel dat de vorm heeft van raspberrypi:1 (ip-addres:1)
8. Open het programma VNC Viewer en tik in het hostnaam-adres dat je 
genoteerd hebt: raspberrypi.local:1 (let op: woord .local is toegevoegd)
9. Je ziet de Raspberry PI Desktop GUI op jouw laptop. Je kan nu via de grafische GUI werken 
alsof je een monitor en toetsenbord rechtstreeks aan de Raspberry Pi hebt gekoppeld.

