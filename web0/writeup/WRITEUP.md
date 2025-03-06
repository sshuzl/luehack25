# web0 - Writeup

Die gegebene Webseite führt in die Grundlagen der Grundlagen von HTML, CSS und JavaScript ein.
Jedes der drei Gebiete liefert einen Teil der Flagge.

Der erste Teil der Flagge findet sich im Abschnitt zu HTML.
Dort wird erklärt, dass Kommentare zwar im HTML stehen, aber vom Browser ignoriert werden.
Sieht man sich den HTML-Code im Bereich um diese Erklärung herum an, so findet man einen Kommentar mit dem ersten Teil der Flagge.

Der zweite Teil der Flagge wird direkt auf der Webseite angezeigt.
Allerdings sind die Buchstaben vertauscht und teilweise übereinander.
Schaut man sich den CSS-Code an, so sieht man, dass die Buchstabenpositionen von der Breite des Browserfensters abhängen.
Spielt man etwas mit der Breite des Browsers, so findet man genau eine Position, bei der sich keine Buchstaben überlagern oder große Lücken zwischen den Zeichen entstehen.
Der in diesem Fall angezeigte Text (der in Leetspeak auch Sinn ergibt) ist der zweite Teil der Flagge.

Den letzten Teil findet man, wenn man den JavaScript-Code ansieht.
Der Code enthält eine Funktion, der den dritten teil der Flagge vom Server lädt und in die Konsole ausgibt.
Allerdings wird diese Funktion von der Webseite nicht aufgerufen.
Tut man dies selbst, so erhält man den letzten Flaggenteil.
Alternativ kann auch die vom JavaScript aufgerufene URL selbst zugreifen und so die Flagge kompletieren.
