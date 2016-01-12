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
echo:บ                     Grab beta v2.1                       บ
echo:บ                                                          บ 
echo บ 1. Code links                                            บ
echo บ 2. Sources                                               บ
echo บ 3. Changelog                                             บ
echo บ 4. About                                                 บ
echo:บ                                                          บ    
echo บ Q. Quit                                                  บ
echo บออออออออออออออออออออออออออออออออออออออออออออออออออออออออออบ
echo:
set /p var=What would you like to open? 

IF '%var%' == '1' GOTO LINKS
IF '%var%' == '2' GOTO SOURCES
IF '%var%' == '3' GOTO CHANGELOG
IF '%var%' == '4' GOTO ABOUT

IF '%var%' == 'Q' GOTO QUIT
IF '%var%' == 'q' GOTO QUIT

cls
msg * That selection does not exist please try again!
goto start

:LINKS
:start3
cls
echo:
echo บออออออออออออออออออออออออออออออออออออออออออออออออออออออออออบ
echo:บ                     Versions                      	   บ
echo:บ                                                          บ 
echo บ 1. Code: Grab v2.0                                       บ
echo บ 2. Code: Grab v2.1                                       บ
echo บ 3. Go Back                                               บ
echo:บ                                                          บ    
echo บออออออออออออออออออออออออออออออออออออออออออออออออออออออออออบ
echo:
set /p var=What would you like to open? 

IF '%var%' == '1' GOTO V2.0
IF '%var%' == '2' GOTO V2.1
IF '%var%' == '3' GOTO BACK

:V2.0
start http://pastebin.com/6MRwFRAM
Pause
cls
goto start3

:V2.1
start http://pastebin.com/yxcNMRjK
Pause
cls
goto start3

:BACK
cls
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
echo บ 3. Hand (Cursor/Pointer) sprite (by yd)                  บ  	   
echo บ 4. Background (by Julien)                                บ
echo บ 5. Border (by nicubunu)                                  บ
echo บ 6. Music (boc.it) (by Cardamar / BoC)		           บ
echo บ 7. Music (silver.ogg) - (by dean evans)		   บ
echo บ 8. Bomb sound effects (by dklon)                         บ
echo บ 9. Clock                                                 บ
echo บ 10. Go Back                                              บ
echo บออออออออออออออออออออออออออออออออออออออออออออออออออออออออออบ
echo:
set /p var=What would you like to open? 

IF '%var%' == '1' GOTO OPENGAMEARTPAGE
IF '%var%' == '2' GOTO MODARCHIVE
IF '%var%' == '3' GOTO HAND
IF '%var%' == '4' GOTO BG
IF '%var%' == '5' GOTO BORDER
IF '%var%' == '6' GOTO MUSIC
IF '%var%' == '7' GOTO MUSIC2
IF '%var%' == '8' GOTO BOMB
IF '%var%' == '9' GOTO CLOCK
IF '%var%' == '10' GOTO BACK

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

:MUSIC2
start https://www.youtube.com/watch?v=p8oy1iZsMrM
Pause
cls
goto start2

:BOMB
start http://opengameart.org/content/boom-pack-1
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
echo:
echo Version 2.1 Small update:
echo - New bomb sound effect. There are now 2 x bomb explosions sounds.
echo - Added a new score system, "Score Last Time" which will save your score for 
echo each time you play.
echo - Moved bombs to start spawning from level 2 to level 3.
echo - Updated the levels.
echo:
echo:
echo Version 2.2 Small update:
echo - Fixed a problem with the Bomb class.
echo - Added an explosion effect when you touch bombs.
echo - Added highscore to the game.
echo - a lot of small details and other things edited.
echo:
echo:
pause
goto start

:ABOUT
cls
echo:
echo Game made by HJ. Grab is a score related game where the player's goal is to get the highest points as possible.
echo When you advance through the game it'll get harder and more difficult.
echo:
pause
goto start

:BACK
cls
goto start

:QUIT
exit