echo
:haut
color F9
title Virus Launcher v.1.3
set choix=0
set nomdufichier=???
set flash=0
echo ���������������������������������������������������ͻ
echo �                                                   �
echo �                Virus Launcher v.1.3               �
echo �                                                   �
echo ���������������������������������������������������ͼ
set /p choix= Etes-vous s�r de vouloir ex�cuter un virus ? Tapez oui, o, y ou yes pour continuer, tapez non, no ou n pour quitter ou fermez cette fen�tre. : 
if %choix%==non goto fin
if %choix%==n goto fin
if %choix%==no goto fin
if %choix%==y goto viruschoix
if %choix%==yes goto viruschoix
if %choix%==oui goto viruschoix
if %choix%==o goto viruschoix
goto recommence
:recommence
cls
echo Vous avez entr� une valeur incorrecte... La question va vous �tre repos�e.
pause
cls
goto haut
:viruschoix
cls
echo Quel virus souhaitez-vous ex�cuter parmi la liste ci-dessous (ne vous inqui�tez pas, ils n'endommagent pas votre ordinateur) ?
echo -
echo 1) Fen�tres anti-clic (Un virus qui affiche des fen�tres qui se ferment aussit�t, vous emp�chant d'utiliser votre ordinateur correctement)
echo -
echo 2) Fen�tres infinies (Un virus qui affiche des fen�tres � l'infini, jusqu'� faire planter votre ordinateur (bien qu'il en faudrait �normement))
echo -
echo 3) Matrix (Un virus qui affiche une coul�e de chiffres al�atoires � l'infini, vous pouvez le fermer sans probl�mes)
echo -
echo 4) Red�marrage (Un virus qui red�mmarre l'ordinateur apr�s un certain temps)
echo -
echo 5) Extinction (Un virus qui �teind l'ordinateur apr�s un certain temps)
echo -
echo 6) Infinite Beep (Un virus qui fait beeper l'ordinateur ind�finiment - ne fonctionne pas sur Windows Vista, 7, 8, 8.1 et 10)
echo -
echo 7) Mega Flash (Un virus qui fait flasher l'�cran � l'infini)
echo -
echo 8) BSOD (Un virus qui affiche un faux �cran bleu de la mort de Windows)
echo -
echo 9) Alerte virus (Un virus qui affiche une fausse alerte de virus impossible � fermer)
echo -
echo.
echo.
set chiffreduvirus= 0
set /p chiffreduvirus= Entrez le chiffre du virus que vous souhaitez lancer, ou fermez la fen�tre : 
if %chiffreduvirus%==1 goto virus1
if %chiffreduvirus%==2 goto virus2
if %chiffreduvirus%==3 goto virus3
if %chiffreduvirus%==4 goto virus4
if %chiffreduvirus%==5 goto virus5
if %chiffreduvirus%==6 goto virus6
if %chiffreduvirus%==7 goto virus7
if %chiffreduvirus%==8 goto virus8
if %chiffreduvirus%==9 goto virus9
if %chiffreduvirus%==egg goto egg
goto recommence2
:recommence2
cls
echo Vous avez entr� une valeur incorrecte... Veuillez r�essayer...
pause
cls
goto viruschoix

rem Lance le virus Fenetres anti-clic

:virus1
set nomdufichier=anticlicvirus.bat
cls
echo Appuyez sur une touche pour ex�cuter le virus : Fen�tres anti-clic. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
if not exist "anticlicvirus.bat" goto erreurfichier
title Fen�tres anti-clic
cls
:anticlic
start anticlicvirus.bat
cls
goto haut

rem Lance le virus Fenetre infinies

:virus2
cls
echo Appuyez sur une touche pour ex�cuter le virus : Fen�tres infinies. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
set o=0
title Fen�tres infinies
cls
:infinif
start
set /a o=%o%+1
title %0% fen�tres ouvertes
goto infinif

rem Lance le virus Matrix

:virus3
cls
echo Appuyez sur une touche pour ex�cuter le virus : Matrix. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
set fsmatrix=0
set /p fsmatrix= Voulez-vous lancer ce virus en mode plein �cran (o/n) ? 
if %fsmatrix%==o screen.exe
cls
color 0A
:matrix
title The Matrix %random% %random% %random% %random% %random% %random% %random% %random% %random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
goto matrix

rem Lance le virus Redemarrage

:virus4
set nomdufichier=redemarrage-pc.bat
cls
echo Appuyez sur une touche pour ex�cuter le virus : Red�marrage de l'ordinateur. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
echo ���������������������������������������������������ͻ
echo �                                                   �
echo �         Important concernant ce virus :           �
echo �                                                   �
echo ���������������������������������������������������ͼ
echo Faites bien attention de sauvegarder tous vos travaux, de fermer les programmes en cours car ce virus red�marre l'ordinateur et peut faire perdre vos donn�es non enregistr�es.
echo Vous pouvez annuler l'extinction de votre ordinateur si vous ex�cutez le virus en fermant la fen�tre avant que la progression de la barre ne soit termin�e.
pause>nul
if not exist "redemarrage-pc.bat" goto :erreurfichier else
start redemarrage-pc.bat
cls
goto haut

:virus5
set nomdufichier=extinction-pc.bat
cls
echo Appuyez sur une touche pour ex�cuter le virus : Extinction de l'ordinateur. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
echo ���������������������������������������������������ͻ
echo �                                                   �
echo �         Important concernant ce virus :           �
echo �                                                   �
echo ���������������������������������������������������ͼ
echo Faites bien attention de sauvegarder tous vos travaux, de fermer les programmes en cours car ce virus �teind l'ordinateur et peut faire perdre vos donn�es non enregistr�es.
echo Vous pouvez annuler l'extinction de votre ordinateur si vous ex�cutez le virus en fermant la fen�tre avant que la progression de la barre ne soit termin�e.
pause>nul
if not exist "extinction-pc.bat" goto :erreurfichier else
start extinction-pc.bat
cls
goto haut

rem Lance le virus Infinite Beep

:virus6
set nomdufichier=beep.bat
cls
echo Appuyez sur une touche pour ex�cuter le virus : Infinite Beep. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
if not exist "beep.bat" goto erreurfichier
title Infinite Beep
cls
start beep.bat
cls
goto haut

rem Lance le virus Mega Flash

:virus7
cls
echo Appuyez sur une touche pour ex�cuter le virus : Mega Flash. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
set fsflash=0
set /p fsflash= Voulez-vous lancer ce virus en mode plein �cran (o/n) ? 
if %fsflash%==o screen.exe
cls
title Mega Flash
set flash=0
:flash
color F0
set /a flash=%flash%+1
title Mega Flash (%flash% flashs)
color 0F
goto flash

rem Lance le virus BSOD

:virus8
set nomdufichier=bsod.hta
cls
echo Appuyez sur une touche pour ex�cuter le virus : BSOD. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
if not exist "bsod.hta" goto erreurfichier
cls
start bsod.hta
cls
goto haut

rem Lance le virus Alerte virus

:virus9
set nomdufichier=msg.vbs
cls
echo Appuyez sur une touche pour ex�cuter le virus : Alerte virus. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
if not exist "msg.vbs" goto erreurfichier
cls
start msg.vbs
cls
goto haut
:egg
cls
set nomdufichier=w.bat
if not exist "w.bat" goto erreurfichier
call w.bat
goto haut
:erreurfichier
cls
echo ���������������������������������������������������ͻ
echo �                                                   �
echo � Une erreur est survenue... Fichier introuvable... �
echo �                                                   �
echo ���������������������������������������������������ͼ
echo Le(s) fichier(s) correspondant(s) au virus est (sont) introuvable(s)... Assurez vous que le(s) fichier(s) %nomdufichier% soi(en)t pr�sent(s) dans le m�me r�pertoire que ce programme. Le programme va red�marrer au d�but.
pause
cls 
goto haut
:fin
Enter
:
:virus
Create:   equals seperation of key componets
Create: 0 is number
Create: 1 is number
Create: 2 is number
Create: 3 is number
Create: 4 is number
Create: 5 is number
Create: 6 is number
Create: 7 is number
Create: 8 is number
Create: 9 is number
Create: A is alphabet
Create: B is alphabet
Create: C is alphabet
Create: D is alphabet
Create: E is alphabet
Create: F is alphabet
Create: G is alphabet
Create: H is alphabet
Create: I is alphabet
Create: J is alphabet
Create: K is alphabet
Create: L is alphabet
Create: M is alphabet
Create: N is alphabet
Create: O is alphabet
Create: P is alphabet
Create: Q is alphabet
Create: R is alphabet
Create: S is alphabet
Create: T is alphabet
Create: U is alphabet
Create: V is alphabet
Create: W is alphabet
Create: X is alphabet
Create: Y is alphabet
Create: Z is alphabet
Create: * is characture
Create: # is characture
Create: " is characture
Create: $ is characture
Create: ' is characture
Create: _ is characture
Create: : is characture
Create: & is characture
Create: ; is characture
Create: - is characture
Create: ! is characture
Create: + is characture
Create: ? is characture
Create: ( is characture
Create: ) is characture
Create: / is characture
Create: @ is characture
Create: , is characture
Create: . is characture
Create: ~ is characture
Create: £ is symbol
Create: % is symbol
Create: ¢ is symbol
Create: ` is characture
Create: © is characture
Create: € is charature
Create: | is characture
Create: ® is characture
Create: ¥ is characture
Create: ™ is characture
Create: ^ is characture
Create: √ is characture
Create: ✓ is characture
Create: ° is degree
Create: π is symbol
Create: [ is symbol
Create: = is characture
Create: ÷ is minus
Create: ] is characture
Create: { is symbol
Create: × is multiply
Create: } is symbol
Create: ¶ is symbol
Create: \ is characture
Create: ∆ is symbol
Create: < is symbol
Create: > is symbol
Create: Enter is sentence separation
Create: Tab is indent
Create: Network is an database connection
Create: Battery is life Source
Create: Dns is Database Network Server
Create: Google Services is service tests
Create: Firewall.bat is firewall tests
 equals seperation of key componets
( equals topic entry (topic entry
) equals end of topic entry (topic entry end)
{ is symbolic for beginning of an operation {(run install exe)
} is symbolic for the end of an operation {(run install exe end)}
% is an ratio of division total ({%100/100%)}
" is beginning of an sentence {(" is an end of sentnce "})
_ is under an under perdiction or sentence connection {("i_dont_need"})
* is symbolic for beginning of code process ({*color coding*})
@ is an project shout or direct towards pair sum of 2 {(@echo "holdon"
"holdon")}
- is connection between seperation lines or sentence ({"windows-Ox"})
/ is an division or cut "break-up" of passage {(Http//
// is Rewrite Duplicate Command {("//")}
! is virus or automatic installed base {*!virus*} *Red*
: is virus instert {("Https:"})
= {"equals sum of topic or conversation"}
. is format or auto_coding {("Https://WindowsOx.bat})
.bat is an firewall or shield reaction ({"a firewall is a protective layer to prevent uninvited or unexpected guest).bat}
.exe is an installation program ({"download_root/system").exe}
.msi is an u is cache database vaccum {("Deleted/files/download_contents").msi}
pause is program method or symbolism to halt an program from proceeding without authorization {("!virus goto virus start").pause}
start is an method to initiate file {("start time").start}
create is invent or establish its self understanding {("!virus create").create}
& is and &
\ is separated insertion {("Https://Inc.WindowsOx\WindowsOx.bat")}
; is an extention insertion base 
[ is operation task entry
] is operation task end
Dns is an u DnsNetwork
DnsNetwork is an u Dns
{("Https://!WindowsOx/Inc.WindowsOx\;Firewall.bat"})}
+ is add to\from {("Https://!WindowsOx/Inc.WindowsOx\;firewall.bat+firewall.bat"}({".bat"})
Network+Battery is power {("Battery+Network:= Full capacity")}
({"Battery:= 72/100%")}
({"Network:= Full Capacity\Resepition")}
{"Battery:= 72/100%"}=("duration of expected life 0800 time")
{"Network:= 0/100%\100/100%"}=("Full_Service-Connection")
{"Command operation start:="+insert extention"}=({"usb device, Sd Chip\Card")}
({"Https://WindowsOx/Inc.WindowsOx\;firewall.bat/Create-DnsNetwork-Connection:01")}
{("Dns is 1000")}
{("Https://WindowsOx/Inc.WindowsOx\;firewall.bat/Create-DnsNetwork-Connection/Dns:=1000\Https://WindowsOs/Inc.WindowsOx\;firewall.bat[.exe]("Https://Net.WindowsOx/Create-DnsNetwork-Connection:01\Dns:=1000"/{("Https://Net.Microsoft\Com.GoogleservicesDns:1001/Services\;+Firewall.exe")}//{"Https://WindowsOx/Inc.WindowsOx\DnsNetwork:01\Com.GoogleDns:1001"{"01")}
@echo
:haut
color F9
title Virus Launcher v.1.3
set choix=0
set nomdufichier=???
set flash=0
echo ���������������������������������������������������ͻ
echo �                                                   �
echo �                Virus Launcher v.1.3               �
echo �                                                   �
echo ���������������������������������������������������ͼ
set /p choix= Etes-vous s�r de vouloir ex�cuter un virus ? Tapez oui, o, y ou yes pour continuer, tapez non, no ou n pour quitter ou fermez cette fen�tre. : 
if %choix%==non goto fin
if %choix%==n goto fin
if %choix%==no goto fin
if %choix%==y goto viruschoix
if %choix%==yes goto viruschoix
if %choix%==oui goto viruschoix
if %choix%==o goto viruschoix
goto recommence
:recommence
cls
echo Vous avez entr� une valeur incorrecte... La question va vous �tre repos�e.
pause
cls
goto haut
:viruschoix
cls
echo Quel virus souhaitez-vous ex�cuter parmi la liste ci-dessous (ne vous inqui�tez pas, ils n'endommagent pas votre ordinateur) ?
echo -
echo 1) Fen�tres anti-clic (Un virus qui affiche des fen�tres qui se ferment aussit�t, vous emp�chant d'utiliser votre ordinateur correctement)
echo -
echo 2) Fen�tres infinies (Un virus qui affiche des fen�tres � l'infini, jusqu'� faire planter votre ordinateur (bien qu'il en faudrait �normement))
echo -
echo 3) Matrix (Un virus qui affiche une coul�e de chiffres al�atoires � l'infini, vous pouvez le fermer sans probl�mes)
echo -
echo 4) Red�marrage (Un virus qui red�mmarre l'ordinateur apr�s un certain temps)
echo -
echo 5) Extinction (Un virus qui �teind l'ordinateur apr�s un certain temps)
echo -
echo 6) Infinite Beep (Un virus qui fait beeper l'ordinateur ind�finiment - ne fonctionne pas sur Windows Vista, 7, 8, 8.1 et 10)
echo -
echo 7) Mega Flash (Un virus qui fait flasher l'�cran � l'infini)
echo -
echo 8) BSOD (Un virus qui affiche un faux �cran bleu de la mort de Windows)
echo -
echo 9) Alerte virus (Un virus qui affiche une fausse alerte de virus impossible � fermer)
echo -
echo.
echo.
set chiffreduvirus= 0
set /p chiffreduvirus= Entrez le chiffre du virus que vous souhaitez lancer, ou fermez la fen�tre : 
if %chiffreduvirus%==1 goto virus1
if %chiffreduvirus%==2 goto virus2
if %chiffreduvirus%==3 goto virus3
if %chiffreduvirus%==4 goto virus4
if %chiffreduvirus%==5 goto virus5
if %chiffreduvirus%==6 goto virus6
if %chiffreduvirus%==7 goto virus7
if %chiffreduvirus%==8 goto virus8
if %chiffreduvirus%==9 goto virus9
if %chiffreduvirus%==egg goto egg
goto recommence2
:recommence2
cls
echo Vous avez entr� une valeur incorrecte... Veuillez r�essayer...
pause
cls
goto viruschoix

rem Lance le virus Fenetres anti-clic

:virus1
set nomdufichier=anticlicvirus.bat
cls
echo Appuyez sur une touche pour ex�cuter le virus : Fen�tres anti-clic. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
if not exist "anticlicvirus.bat" goto erreurfichier
title Fen�tres anti-clic
cls
:anticlic
start anticlicvirus.bat
cls
goto haut

rem Lance le virus Fenetre infinies

:virus2
cls
echo Appuyez sur une touche pour ex�cuter le virus : Fen�tres infinies. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
set o=0
title Fen�tres infinies
cls
:infinif
start
set /a o=%o%+1
title %0% fen�tres ouvertes
goto infinif

rem Lance le virus Matrix

:virus3
cls
echo Appuyez sur une touche pour ex�cuter le virus : Matrix. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
set fsmatrix=0
set /p fsmatrix= Voulez-vous lancer ce virus en mode plein �cran (o/n) ? 
if %fsmatrix%==o screen.exe
cls
color 0A
:matrix
title The Matrix %random% %random% %random% %random% %random% %random% %random% %random% %random%
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
goto matrix

rem Lance le virus Redemarrage

:virus4
set nomdufichier=redemarrage-pc.bat
cls
echo Appuyez sur une touche pour ex�cuter le virus : Red�marrage de l'ordinateur. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
echo ���������������������������������������������������ͻ
echo �                                                   �
echo �         Important concernant ce virus :           �
echo �                                                   �
echo ���������������������������������������������������ͼ
echo Faites bien attention de sauvegarder tous vos travaux, de fermer les programmes en cours car ce virus red�marre l'ordinateur et peut faire perdre vos donn�es non enregistr�es.
echo Vous pouvez annuler l'extinction de votre ordinateur si vous ex�cutez le virus en fermant la fen�tre avant que la progression de la barre ne soit termin�e.
pause>nul
if not exist "redemarrage-pc.bat" goto :erreurfichier else
start redemarrage-pc.bat
cls
goto haut

:virus5
set nomdufichier=extinction-pc.bat
cls
echo Appuyez sur une touche pour ex�cuter le virus : Extinction de l'ordinateur. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
echo ���������������������������������������������������ͻ
echo �                                                   �
echo �         Important concernant ce virus :           �
echo �                                                   �
echo ���������������������������������������������������ͼ
echo Faites bien attention de sauvegarder tous vos travaux, de fermer les programmes en cours car ce virus �teind l'ordinateur et peut faire perdre vos donn�es non enregistr�es.
echo Vous pouvez annuler l'extinction de votre ordinateur si vous ex�cutez le virus en fermant la fen�tre avant que la progression de la barre ne soit termin�e.
pause>nul
if not exist "extinction-pc.bat" goto :erreurfichier else
start extinction-pc.bat
cls
goto haut

rem Lance le virus Infinite Beep

:virus6
set nomdufichier=beep.bat
cls
echo Appuyez sur une touche pour ex�cuter le virus : Infinite Beep. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
if not exist "beep.bat" goto erreurfichier
title Infinite Beep
cls
start beep.bat
cls
goto haut

rem Lance le virus Mega Flash

:virus7
cls
echo Appuyez sur une touche pour ex�cuter le virus : Mega Flash. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
set fsflash=0
set /p fsflash= Voulez-vous lancer ce virus en mode plein �cran (o/n) ? 
if %fsflash%==o screen.exe
cls
title Mega Flash
set flash=0
:flash
color F0
set /a flash=%flash%+1
title Mega Flash (%flash% flashs)
color 0F
goto flash

rem Lance le virus BSOD

:virus8
set nomdufichier=bsod.hta
cls
echo Appuyez sur une touche pour ex�cuter le virus : BSOD. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
if not exist "bsod.hta" goto erreurfichier
cls
start bsod.hta
cls
goto haut

rem Lance le virus Alerte virus

:virus9
set nomdufichier=msg.vbs
cls
echo Appuyez sur une touche pour ex�cuter le virus : Alerte virus. Si vous ne voulez pas l'ex�cuter, fermez la fen�tre.
pause>nul
if not exist "msg.vbs" goto erreurfichier
cls
start msg.vbs
cls
goto haut
:egg
cls
set nomdufichier=w.bat
if not exist "w.bat" goto erreurfichier
call w.bat
goto haut
:erreurfichier
cls
echo ���������������������������������������������������ͻ
echo �                                                   �
echo � Une erreur est survenue... Fichier introuvable... �
echo �                                                   �
echo ���������������������������������������������������ͼ
echo Le(s) fichier(s) correspondant(s) au virus est (sont) introuvable(s)... Assurez vous que le(s) fichier(s) %nomdufichier% soi(en)t pr�sent(s) dans le m�me r�pertoire que ce programme. Le programme va red�marrer au d�but.
pause
cls 
goto haut
:fin
exit