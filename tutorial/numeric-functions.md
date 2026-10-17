---
title: "Числові функції"
h1: "Числові та математичні функції SQL Server"
---

Математичні функції та агрегатні функції для чисел.

Колонка «Результат» отримана виконанням прикладу на SQL Server 2022 з демо-базою DemoShop.

<div class="table-scroll"><table>
<tr><th>Функція</th><th>Опис</th><th>Приклад</th><th>Результат</th></tr>
<tr><td><strong>ABS</strong></td><td>Повертає абсолютне значення числа</td><td><code>SELECT ABS(-243.5);</code></td><td>243.5</td></tr>
<tr><td><strong>ACOS</strong></td><td>Повертає арккосинус числа</td><td><code>SELECT ACOS(0.25);</code></td><td>1.318116071652818</td></tr>
<tr><td><strong>ASIN</strong></td><td>Повертає арксинус числа</td><td><code>SELECT ASIN(0.25);</code></td><td>0.25268025514207865</td></tr>
<tr><td><strong>ATAN</strong></td><td>Повертає арктангенс числа</td><td><code>SELECT ATAN(2.5);</code></td><td>1.1902899496825317</td></tr>
<tr><td><strong>ATN2</strong></td><td>Повертає арктангенс двох чисел</td><td><code>SELECT ATN2(0.50, 1);</code></td><td>0.4636476090008061</td></tr>
<tr><td><strong>AVG</strong></td><td>Агрегатна: середнє значення виразу</td><td><code>SELECT (SELECT AVG(Price) FROM Products);</code></td><td>29.513333</td></tr>
<tr><td><strong>CEILING</strong></td><td>Найменше ціле, яке більше або дорівнює числу</td><td><code>SELECT CEILING(25.75);</code></td><td>26</td></tr>
<tr><td><strong>COUNT</strong></td><td>Агрегатна: кількість рядків</td><td><code>SELECT (SELECT COUNT(*) FROM Products);</code></td><td>15</td></tr>
<tr><td><strong>COS</strong></td><td>Повертає косинус числа</td><td><code>SELECT COS(2);</code></td><td>-0.4161468365471424</td></tr>
<tr><td><strong>COT</strong></td><td>Повертає котангенс числа</td><td><code>SELECT COT(6);</code></td><td>-3.436353004180128</td></tr>
<tr><td><strong>DEGREES</strong></td><td>Перетворює радіани на градуси</td><td><code>SELECT DEGREES(PI());</code></td><td>180.0</td></tr>
<tr><td><strong>EXP</strong></td><td>Повертає e в заданому степені</td><td><code>SELECT EXP(1);</code></td><td>2.718281828459045</td></tr>
<tr><td><strong>FLOOR</strong></td><td>Найбільше ціле, яке менше або дорівнює числу</td><td><code>SELECT FLOOR(25.75);</code></td><td>25</td></tr>
<tr><td><strong>LOG</strong></td><td>Натуральний логарифм (або логарифм за заданою основою)</td><td><code>SELECT LOG(8, 2);</code></td><td>3.0</td></tr>
<tr><td><strong>LOG10</strong></td><td>Десятковий логарифм</td><td><code>SELECT LOG10(1000);</code></td><td>3.0</td></tr>
<tr><td><strong>MAX</strong></td><td>Агрегатна: найбільше значення</td><td><code>SELECT (SELECT MAX(Price) FROM Products);</code></td><td>97.00</td></tr>
<tr><td><strong>MIN</strong></td><td>Агрегатна: найменше значення</td><td><code>SELECT (SELECT MIN(Price) FROM Products);</code></td><td>9.00</td></tr>
<tr><td><strong>PI</strong></td><td>Повертає число π</td><td><code>SELECT PI();</code></td><td>3.141592653589793</td></tr>
<tr><td><strong>POWER</strong></td><td>Підносить число до степеня</td><td><code>SELECT POWER(4, 2);</code></td><td>16</td></tr>
<tr><td><strong>RADIANS</strong></td><td>Перетворює градуси на радіани</td><td><code>SELECT RADIANS(180.0);</code></td><td>3.141592653589793116</td></tr>
<tr><td><strong>RAND</strong></td><td>Повертає випадкове число від 0 до 1 (з seed — передбачуване)</td><td><code>SELECT RAND(5);</code></td><td>0.7136665250979564</td></tr>
<tr><td><strong>ROUND</strong></td><td>Округлює число до заданої кількості знаків</td><td><code>SELECT ROUND(235.415, 2);</code></td><td>235.420</td></tr>
<tr><td><strong>SIGN</strong></td><td>Повертає знак числа: -1, 0 або 1</td><td><code>SELECT SIGN(-255.5);</code></td><td>-1.0</td></tr>
<tr><td><strong>SIN</strong></td><td>Повертає синус числа</td><td><code>SELECT SIN(2);</code></td><td>0.9092974268256817</td></tr>
<tr><td><strong>SQRT</strong></td><td>Повертає квадратний корінь</td><td><code>SELECT SQRT(64);</code></td><td>8.0</td></tr>
<tr><td><strong>SQUARE</strong></td><td>Повертає квадрат числа</td><td><code>SELECT SQUARE(64);</code></td><td>4096.0</td></tr>
<tr><td><strong>SUM</strong></td><td>Агрегатна: сума значень</td><td><code>SELECT (SELECT SUM(Quantity) FROM OrderDetails);</code></td><td>502</td></tr>
<tr><td><strong>TAN</strong></td><td>Повертає тангенс числа</td><td><code>SELECT TAN(1.75);</code></td><td>-5.52037992250933</td></tr>
</table></div>
