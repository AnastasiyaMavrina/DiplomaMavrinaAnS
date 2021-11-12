
str0="Иерархические алгоритмы кластерного анализа."

str01= "Суть иерархической кластеризации состоит в последовательном объединении меньших кластеров в большие или разделении больших кластеров на меньшие. \
\nВ данном приложении используется алгоритм восходящей группы иерархической кластеризации. \
Эта группа алгоритмов характеризуется последовательным\nобъединением исходных элементов и соответствующим уменьшением числа кластеров. \
В начале работы алгоритма все объекты являются отдельными\nкластерами. На первом шаге наиболее похожие объекты объединяются в кластер. \
На последующих шагах объединение продолжается до тех пор, пока все\nобъекты не будут составлять один кластер."

str03="В качестве метода объединения используется метод Уорда. \
Согласно данному методу, в качестве расстояния между кластерами берется прирост\nсуммы квадратов расстояний объектов до центров кластеров, получаемый в результате их объединения. \
Идея метода состоит в том, чтобы проводить\nобъединение, дающее минимальное приращение внутригрупповой суммы квадратов отклонений, \
то есть оптимизировать минимальную дисперсию внутри\nкластеров. \
Замечено, что метод Уорда приводит к образованию кластеров примерно равных размеров. \
"
str04="В данном приложении результатом иерархического кластерного анализа явлется построение дендрограммы и получение таблиц кластеров на основе\nпостроенной дендрограммы. \
 Иерархический  кластерный анализ предназначен для выявления относительно однородных групп наблюдений по заданным\nхарактеристикам. \
В случае, если пользователь не имеет представления о конечном количестве кластеров или хочет получить\nполную картину последовательных объединений нескольких кластеров в одиин - \
в качестве алгоритма кластерного анализа ему следует выбрать именно\nиерархический алгоритм."

str05="Алгоритм к-средних++."

str06="В отличие от иерархических алгоритмов, которые не требуют предварительных предположений \
относительно числа кластеров, для возможности\nиспользования этого алгоритма необходимо иметь гипотезу \
о наиболее вероятном количестве кластеров."

str07="Алгоритм к-средних строит m кластеров, расположенных как можно дальше друг от друга.\
\nВыбор числа m может базироваться на результатах предшествующих исследований, теоретических соображениях \
или интуиции."

str08="В общем алгоритм к-средних представляет из себя набор следующих действий:\n-выбирается число m объектов множества, и на первом шаге эти объекты считаются «центрами масс» кластеров; одному кластеру соответствует один \nцентр; \
\n-каждый из объектов исследуемого множества относят к кластеру, центр масс которого ближе всего располагается к этому объекту;\
\n-вычисляются центры масс полученных кластеров, которыми затем и далее считаются покоординатные средние кластеров; объекты опять \nперераспределяются. \
\nПроцесс вычисления центров масс и перераспределения объектов продолжается до тех пор, пока \
кластерные центры не стабилизируются, т.е. все\nнаблюдения будут принадлежать кластеру, которому принадлежали до текущей итерации. \
Результат анализа алгоритмом к-средних во многом зависит от\nвыбора исходных центров масс кластеров и, поэтому, является нестабильным. \
Во избежание получения «плохого»  результата в данном приложении\nиспользуется улучшенная версия алгоритма к-средних алгоритм к-средних++. \
Суть улучшения заключается в нахождении более «хороших» начальных\nзначений центров масс кластеров."

str09="В данном приложении результатом работы алгоритма к-средних++ является получение пользователем заданного им количества таблиц кластеров.\
 В случае,\nесли пользователь имеет представления о конечном количестве кластеров, например, хочет разбить объекты на группы по одному конкретному признаку,\
\nв качестве алгоритма кластерного анализа ему следует выбрать алгоритм к-средних++."