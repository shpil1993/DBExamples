---
title: "BACKUP DATABASE"
h1: "BACKUP DATABASE та RESTORE"
---

Інструкція `BACKUP DATABASE` створює **резервну копію** бази даних SQL Server.

## Синтаксис

```sql
BACKUP DATABASE databasename
TO DISK = 'filepath';
```

## Повна резервна копія

<div class="example" markdown="1">

Створити повну копію бази `DemoShop` на диск `D:`:

```sql
BACKUP DATABASE DemoShop
TO DISK = 'D:\backups\DemoShop.bak';
```

</div>

<div class="note" markdown="1">
**Порада.** Зберігайте резервні копії на іншому фізичному диску (або в іншому місці), ніж саму базу. Якщо диск з базою вийде з ладу, копія залишиться неушкодженою.
</div>

## Диференційна резервна копія

Диференційна копія містить лише ті частини бази, що **змінилися з моменту останньої повної** копії.

```sql
BACKUP DATABASE databasename
TO DISK = 'filepath'
WITH DIFFERENTIAL;
```

<div class="example" markdown="1">

```sql
BACKUP DATABASE DemoShop
TO DISK = 'D:\backups\DemoShop_diff.bak'
WITH DIFFERENTIAL;
```

</div>

Диференційна копія створюється швидше й займає менше місця, ніж повна.

## Резервна копія журналу транзакцій

Якщо база працює в моделі відновлення `FULL`, можна робити копії журналу транзакцій. Це дає змогу відновити базу на конкретний момент часу.

```sql
BACKUP LOG DemoShop
TO DISK = 'D:\backups\DemoShop_log.trn';
```

## Корисні параметри WITH

```sql
BACKUP DATABASE DemoShop
TO DISK = 'D:\backups\DemoShop.bak'
WITH
    INIT,          -- перезаписати файл, а не дописувати
    COMPRESSION,   -- стиснути копію
    CHECKSUM,      -- перевірити контрольні суми сторінок
    STATS = 10;    -- показувати прогрес кожні 10%
```

## Відновлення: RESTORE DATABASE

Відновити базу з резервної копії:

```sql
RESTORE DATABASE DemoShop
FROM DISK = 'D:\backups\DemoShop.bak'
WITH REPLACE;
```

Відновлення повної та диференційної копії:

```sql
RESTORE DATABASE DemoShop
FROM DISK = 'D:\backups\DemoShop.bak'
WITH NORECOVERY, REPLACE;

RESTORE DATABASE DemoShop
FROM DISK = 'D:\backups\DemoShop_diff.bak'
WITH RECOVERY;
```

`NORECOVERY` означає «чекати на наступні копії», а `RECOVERY` — завершити відновлення і відкрити базу для роботи.

## Перевірка резервної копії

```sql
RESTORE VERIFYONLY
FROM DISK = 'D:\backups\DemoShop.bak';
```

У SSMS резервні копії можна робити й через графічний інтерфейс: правою кнопкою на базі → **Tasks → Back Up...**
