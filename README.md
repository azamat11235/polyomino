# Задача замощения прямоугольного стола заданным множеством полиомино

## Описание алгоритма
Задача решается методом бэктрекинга (поиск с возвратом). Количество возможных состояний каждого полимино ограничено. На каждом шаге для очередного полимино ищется место на столе. Если место найдено, то осуществляется переход к следующему полимино, если нет -- происходит возврат к предыдущему полимино, которое переходит в своё следующее состояние (вращением и/или сдвигом).

Также задачу можно было решить и с использованием `SAT` солверов.

## Сложность
Полимино хранятся поклеточно, поэтому сложность по памяти `O(mn + k)`, где `m` и `n` размеры стола, а `k` - сумма единичных клеток всех полимино.

Задача является `NP`-полной. Сложность по времени в худшем случае составляет `O(mn)^k`.


## Запуск программы
1. Установка необходимых библиотек
```shell
pip install -r requirements.lock.txt
```
2. Запуск
```shell
python example.py
```
