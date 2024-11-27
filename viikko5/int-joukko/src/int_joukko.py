KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:

    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kapasiteetin pitää olla positiivinen kokonaisluku")

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kasvatuskoon pitää olla positiivinen kokonaisluku")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):

        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm >= len(self.ljono):
                self.kasvata_listaa()

            return True

        return False

    def kasvata_listaa(self):
        uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista


    def poista(self, n):

        if n not in self.ljono[:self.alkioiden_lkm]:
            return False

        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == n:
                for j in range(i, self.alkioiden_lkm - 1):
                    self.ljono[j] = self.ljono[j + 1]
                self.ljono[self.alkioiden_lkm - 1] = 0
                self.alkioiden_lkm -= 1
                return True
        return False

    def kopioi_lista(self, lahde, kohde):
        for i in range(0, len(lahde)):
            kohde[i] = lahde[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()

        for alkio in a.to_int_list() + b.to_int_list():
            tulos.lisaa(alkio)

        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for alkio in a.to_int_list():
            if b.kuuluu(alkio):
                tulos.lisaa(alkio)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for alkio in a.to_int_list():
            if not b.kuuluu(alkio):
                tulos.lisaa(alkio)

        return tulos

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
