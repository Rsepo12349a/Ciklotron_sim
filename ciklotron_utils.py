from constants import g,epsilon
import numpy as np

class loptica:

    def __abs__(self,masa,radijus):
        self.masa = masa
        self.radijus = radijus
        self.kapacitet = np.float32(4 * np.pi * epsilon * self.radijus)
        self.naboj = 0

    def dodaj_naboj(self,U):

        self.naboj = self.kapacitet * U

    def get_naboj(self):
        return self.naboj

    def get_masa(self):
        return self.masa

    def get_radijus(self):
        return self.radijus
