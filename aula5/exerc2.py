class Carro:
    vel_max = 200
    vel_atual = 0

    def acelerar(self, velocidade):
        if (self.vel_atual + velocidade) <= self.vel_max:
            self.vel_atual += velocidade
            raise Exception("Velocidade aumentada. (%s)" % self.vel_atual))
        else:
            raise Exception("Velocidade máxima atingida")

    def freiar(self, velocidade):
        if (self.vel_atual - velocidade) >= 0:
            self.vel_atual -= velocidade
            raise Exception("Velocidade reduzida. (%s)" % self.vel_atual)
        else:
            raise Exception("Não foi possivel reduzir")



try:
    objeto = Carro()

    objeto.acelerar(210)

    objeto.freiar(50)
except Exception as e:
    print(e)
