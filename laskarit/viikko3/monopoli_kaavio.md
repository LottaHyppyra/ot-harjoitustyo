```mermaid
 classDiagram
      Pelilauta "1" --> "*" Pelaaja
      Pelilauta "1" --> "*" Ruutu
      Ruutu "1" --> "*" Pelinappula
      Pelinappula "1" --> "1" Pelaaja
      class Pelilauta{
      }
      class Pelaaja{
      }
      class Ruutu{
      }
      class Pelinappula{
      }
```
