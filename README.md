# <img src="Images/Рисунок1.png" width="30"> PacMan_Neat

PacMan_Neat - это проект, который объединяет классическую аркадную игру Pac-Man с искусственным интеллектом. Пакменом будет управлять не человек, а ИИ, используя алгоритм NEAT (NeuroEvolution of Augmenting Topologies).

# Запуск

1. **Скачайте ZIP** со всеми необходимыми файлами [здесь](https://github.com/GREBIAR-Git/PacMan_Neat/releases/download/1.0Neat/PacManNeat.zip)
2. Настройте **config-FeedForward.txt** под себя [здесь пояснения по полям](https://neat-python.readthedocs.io/en/latest/config_file.html)
3. Настройте **config.yml** под себя:
```yml
   LaunchWinningGenome: True/False # запускает победый геном (если он есть)
   LaunchCheckpoint: True/False # запускает контрольную точку (если она есть)
   CheckpointNumber : 24 # номер контольной точки
   EnableGhost: True/False # включает призраков
```
4. Запустите **main.exe**

# Запуск без ИИ

1. **Скачайте ZIP** со всеми необходимыми файлами [здесь](https://github.com/GREBIAR-Git/PacMan_Neat/releases/download/1.1/PacMan.zip)
2. Запустите **main.exe**

# Интерфейс

Общий вид:

<img width=400 height=400 src="Images/Рисунок11.png">

| Объект        | Внешний вид   |
| ------------- |:-------------:|
| Пакмен        | <img width=20 height=20 src="Images/Рисунок1.png"> |
| Блинки      | <img width=20 height=20 src="Images/Рисунок2.png">     |
| Инки | <img width=20 height=20 src="Images/Рисунок3.png">      |
| Пинки | <img width=20 height=20 src="Images/Рисунок4.png">    |
| Клайд | <img width=20 height=20 src="Images/Рисунок5.png">      |
| Стена | <img width=20 height=20 src="Images/Рисунок6.png">      |
| Еда | <img width=20 height=20 src="Images/Рисунок7.png">      |
| Мега еда | <img width=20 height=20 src="Images/Рисунок8.png">      |
| Собрано еды/Всего еды | <img width=40 height=20 src="Images/Рисунок10.png">      |
| G - Текущее поколение; <br /> L - Поколений без улучшений;  <br /> M - Максимальное количество еды;| <img width=40 height=120 src="Images/Рисунок9.png"> |

# Демонстрация работы программы

<div align=center>
<img width=400 height=400 src="Images/Гифка1.gif">
</div>

