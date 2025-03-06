# back_to_1999 - Writeup

Knopfdruck kann man auf der Webseite einen POST-Request abschicken. Wenn man das macht kommt als Teil der Antwort der eigene Useragent.
Das sollte schon eine starker Hinweis darauf sein, wie die Challenge zu lösen ist: Der Useragent vom Browser muss auf etwas anderes gesetzt werden.
Die Seite selbst gibt hier einige Indizien:
1. Die Challenge selbst enthält das Jahr 1999 im Namen
2. Die Seite bezieht sich auf Windows 95. Das Betriebsystem ist also schon bekannt.
3. Nun bleibt noch die Browsersoftware und deren genaue Version offen: Die Ballade auf der Seite gibt hier schon mal die Hinweis, dass es sich vermutlich um entweder Netscape Navigator oder Internet Explorer handlen muss. Zusammen mit 1. kann man ableiten, dass es sich um eine Browser Version muss die im Jahr 1999 noch aktiv sein muss.

Mit etwas durchprobieren der Useragents im eigenen Browser bekommt man irgendwann die Flagge. Wie man das für den eigenen Browser macht, kann man googlen.
