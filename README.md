# Корпус и обработка русского мата с использованием словаря

Репозиторий для тех, кто решает задачу поиска мата в тексте. Пользователь может скрывать мат при помощи всяческих замен символов.

В файле words.txt лежат стандатные нецензурные слова и выражения. Для несложных задач, где мат не совсем скрыт, такой набор уже подойдет.

Для генерации всех возможных вариантов нецензурных фраз вы можете использовать как предложенный файл words.txt, так и ваш. Проверьте лишь, что формат файла
такой же как и данный words.txt.

Для создания файла с возможными фразами, в которых скрыт мат, склонируйте репозиторий и запустите скрипт по типу:
```python
  wg = WordsGenerator()
  words = wg.create_list_of_obscene_words('words.txt')
  wg.create_file_with_obscene_words('my_file_with_all_words.txt',words)
```
При использовании замен в классе WordsGenerator, предложенных в коде класса, и предложенного файла words.txt, выходной файл будет по размеру примерно  1,5Гб. Для уменьшения объема можно уменьшить кол-во замен для каждой из букв, убрать некоторые слова из файла words.txt.

Для проверки слова можно использовать класс ObsceneFilter. 

При создании объекта класса нужно указать путь к файлу формата words.txt. 
```python
  of = ObsceneFilter('my_file_with_all_words.txt')
```
Для проверки, есть ли слово в вашем словаре, достаточно вызвать метод:
```python
  of.search_word_in_collection('слово')
```
Данный метод реализует простой бинарный поиск на наборе слов. Поэтому важно ,при создании файла с неприемлимыми словами, сортировать их. Класс WordsGenerator при создании файла сортирует слова по умолчанию.

Для поиска наиболее похожих матерных слов к предложенному слову можно использовать метод get_closest_with_Levenstein, под капотом лежит алгоритм подсчета расстояния Левенштейна (https://ru.wikipedia.org/wiki/Расстояние_Левенштейна).
```python
  distance, closest_word = of.search_word_in_collection('слово')
```
Реализацая подсчета расстояния Левенштейна взята из https://pypi.org/project/python-Levenshtein/. 

Данный мини-проект я использовал для псевдо-разметки данных для обучения модели машинного обучения по выявлению мата в тексте.
