## HSL-matkakorttien hallinta

```mermaid
sequenceDiagram
  participant Main
  participant laitehallinto
  participant rautatietori
  participant ratikka6
  participant bussi244
  participant lippu_luukku
  participant kallen_kortti
  Main->>laitehallinto: HKLLaitehallinto()
  Main->>rautatietori: Lataajalaite()
  Main->>ratikka6: Lukijalaite()
  Main->>bussi244: Lukijalaite()
  Main->>laitehallinto: lisaa_lataaja(rautatietori)
  Main->>laitehallinto: lisaa_lukija(ratikka6)
  Main->>laitehallinto: lisaa_lukija(bussi244)
  Main->>lippu_luukku: Kioski()
  Main->>lippu_luukku: osta_matkakortti("Kalle")
  lippu_luukku->>kallen_kortti: Matkakortti("Kalle")
  kallen_kortti->>rautatietori: lataa_arvoa(3)
  rautatietori-->>kallen_kortti: kasvata_arvoa(3)
  kallen_kortti->>ratikka6: osta_lippu(0)
  ratikka6-->>kallen_kortti: True, vahenna_arvoa(1.5)
  kallen_kortti->>bussi244: osta_lippu(2)
  bussi244-->>kallen_kortti: False
```
