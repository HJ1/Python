@echo off
title Grab.bat
:start
cls
echo Made by HJ 13/12/13
echo:
echo Some of the links are outdated and won't load
echo:
echo Options:
echo:
echo บออออออออออออออออออออออออออออออออออออออออออออออออออออออออออบ
echo:บ                     Grab beta v2.0                       บ
echo:บ                                                          บ 
echo บ 1. Code link                                             บ
echo บ 2. Sources                                               บ
echo บ 3. Changelog                                             บ
echo บ 4. About                                                 บ
echo:บ                                                          บ    
echo บ Q. Quit                                                  บ
echo บออออออออออออออออออออออออออออออออออออออออออออออออออออออออออบ
echo:
set /p var=What would you like to open? 

IF '%var%' == '1' GOTO LINK
IF '%var%' == '2' GOTO SOURCES
IF '%var%' == '3' GOTO CHANGELOG
IF '%var%' == '4' GOTO ABOUT

IF '%var%' == 'Q' GOTO QUIT
IF '%var%' == 'q' GOTO QUIT

cls
msg * That selection does not exist please try again!
goto start

:LINK
cls
start http://pastebin.com/6MRwFRAM
goto start

:SOURCES
:start2
cls
echo Cited sources:
echo Look in the "data" folder for all the used resources. 
echo:
echo Special thanks to OpenGameArt and Modarchive for the resources.
echo:
echo บออออออออออออออออออออออออออออออออออออออออออออออออออออออออออบ
echo บ 1. OpenGameArt.org - Free sprites and music              บ
echo บ 2. Modarchive.org - Music and sound effects              บ
echo บ 3. Hand (Cursor/Pointer) sprite                          บ  	   
echo บ 4. Background                                            บ
echo บ 5. Border                                                บ
echo บ 6. Music (boc.it)                                        บ
echo บ 7. Clock                                                 บ
echo บ 8. Go Back                                               บ
echo บออออออออออออออออออออออออออออออออออออออออออออออออออออออออออบ
echo:
set /p var=What would you like to open? 

IF '%var%' == '1' GOTO OPENGAMEARTPAGE
IF '%var%' == '2' GOTO MODARCHIVE
IF '%var%' == '3' GOTO HAND
IF '%var%' == '4' GOTO BG
IF '%var%' == '5' GOTO BORDER
IF '%var%' == '6' GOTO MUSIC
IF '%var%' == '7' GOTO CLOCK
IF '%var%' == '8' GOTO BACK

:OPENGAMEARTPAGE
start http://opengameart.org/
Pause
cls
goto start2

:MODARCHIVE
start http://modarchive.org/
Pause
cls
goto start2

:HAND
start http://opengameart.org/content/pointers-part-5
Pause
cls
goto start2

:BG
start http://opengameart.org/content/large-nature-background
Pause
cls
goto start2

:BORDER
start http://opengameart.org/content/graphite-border
Pause
cls
goto start2

:MUSIC
start http://modarchive.org/module.php?170180
Pause
cls
goto start2

:CLOCK
start http://gmc.yoyogames.com/index.php?showtopic=294490
Pause
cls
goto start2

:CHANGELOG
cls
echo:
echo I will write the changelog when I feel like it. 

pause
goto start

:ABOUT
cls
echo You grab Money huge $$$.
pause
goto start

:BACK
cls
goto start

:QUIT
exit