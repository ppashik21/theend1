fileData="""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8" />
<title>THE END</title>
</head>
<body>




<table
border="1"
background="images/168.png"
bgcolor="#7FFFD4"
cellpadding="10"
style="width:100%; border-radius:5px;">
<!--Создаём строку таблицы-->
<tr>
<!--Создаём столбец таблицы-->
<th>
<!--Содержание ячейки столбца-->
<h1>THE END</h1>

<!--Закрываем таблицу-->
</th>
</tr>
</table>

<table
border="1"
bgcolor="#e6e6fa"
cellpadding="10"
style="width:100%; border-radius:5px;">
<!--Создаём строку-->
<tr>
<!--Создаём ячейку
Оформление:
rowspan="2" - объединяем две ячейки в одну.
Число объединяемых ячеек по числу ячеек в сайдбаре.
style="width:80%" - основной контент занимает 80% всей площади,
оставшиеся 20% для сайдбара-->
<td
rowspan="2"
style="width:80%">


<p style="text-indent:20px">
time is </p>


<!--Закрываем ячейку-->
</td>


</td>
</tr>
</table>


</td>
</tr>
</table>
</body>
</html>"""


f = open('index.html', 'w')
f.write (fileData)
f.close()

from datetime import datetime
current_time = datetime.now().time()
with open("index.html",'r+') as f:
    # Read the file 
    lines=f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('time is'):
            lines[i] = lines[i].strip() + str(current_time)
    f.seek(0)
    for line in lines:
        f.write(line)
            
