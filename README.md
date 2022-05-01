# Devman_API
***

# Project description
    Check weather in locations. 
    Locations configurate in list "LOCATIONS" from file "weater.py".

## Environmental requirements
You will need to use Python ver not lower than 3

## Installing
* Open bash console
* Choose installation directory
* Copy application from repo 
"git clone https://github.com/VetalR/Devman_API.git"

## How to use
* Activate your virtual environment
* Run script to install the required packages "pip3 install -r {path/}requirements.txt"
* Run script "python {path/}weather.py"

## Simple Example
python lessons/weather.py 
London

         \   /     Солнечно
          .-.      12..14 °C      
       ― (   ) ―   ↙ 13 km/h      
          `-’      10 km          
         /   \     0.0 mm         
                            ┌─────────────┐                        
    ┌───────────────────────┤ Вс. 24 апр. ├───────────────────────┐
    │             День      └──────┬──────┘       Ночь            │
    ├──────────────────────────────┼──────────────────────────────┤
    │               Пасмурно       │     \   /     Ясно           │
    │      .--.     17 °C          │      .-.      7..9 °C        │
    │   .-(    ).   ↙ 20-23 km/h   │   ― (   ) ―   ↙ 15-21 km/h   │
    │  (___.__)__)  10 km          │      `-’      10 km          │
    │               0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┘
                            ┌─────────────┐                        
    ┌───────────────────────┤ Пн. 25 апр. ├───────────────────────┐
    │             День      └──────┬──────┘       Ночь            │
    ├──────────────────────────────┼──────────────────────────────┤
    │  _`/"".-.     Местами дождь  │     \   /     Ясно           │
    │   ,\_(   ).   13..14 °C      │      .-.      8..9 °C        │
    │    /(___(__)  ↙ 13-15 km/h   │   ― (   ) ―   ↙ 11-16 km/h   │
    │      ‘ ‘ ‘ ‘  10 km          │      `-’      10 km          │
    │     ‘ ‘ ‘ ‘   0.1 mm | 88%   │     /   \     0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┘
                            ┌─────────────┐                        
    ┌───────────────────────┤ Вт. 26 апр. ├───────────────────────┐
    │             День      └──────┬──────┘       Ночь            │
    ├──────────────────────────────┼──────────────────────────────┤
    │    \  /       Переменная обл…│               Облачно        │
    │  _ /"".-.     13..14 °C      │      .--.     8..10 °C       │
    │    \_(   ).   ↓ 12-14 km/h   │   .-(    ).   ↙ 12-17 km/h   │
    │    /(___(__)  10 km          │  (___.__)__)  10 km          │
    │               0.0 mm | 0%    │               0.0 mm | 0%    │
    └──────────────────────────────┴──────────────────────────────┘
    
    Все новые фичи публикуются здесь: @igor_chubin
