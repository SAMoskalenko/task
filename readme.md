#0 Устанавливаем необходимые программы:
requirements.txt

#1 Создаем БД
В консоли последовательно: 
python manage.py makemigrations
python manage.py migrate

База данных состоит из 6 таблиц:
TimeData - данные о времени точек
ValueData - данные о значениях точек
IntervalData - данные о интервалах между точками
FreeRangeData - данные о свободных интервалах
DotData - данные о точках (ссылается на TimeData, ValueData, IntervalData через сериалайзер добавлена информация о комментариях)
CommentData - данные о комментариях (ссылается на IntervalData, FreeRangeData, DotData)


#2 Программа заполнения кода из двоичного файла
Запускаем файл data.py, который заполняет БД db.sqlite3

#3 Создаем файл json для отображения графика
Запускаем файл get_data.py, который создает файл get_data.json

#4 Отображаем график 
Запускаем index.html