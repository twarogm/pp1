import QuadraticEquation

wsp = QuadraticEquation.czytajWspolczynniki()
d = QuadraticEquation.obliczDelte(wsp)
p = QuadraticEquation.obliczPierwiastki(wsp, d)
QuadraticEquation.wyswietlPierwiastki(wsp, d, p)