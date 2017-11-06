class Carro:
    vel_max = 200
    vel_atual = 0

    def acelerar(self, velocidade):
        if (self.vel_atual + velocidade) <= self.vel_max:
            self.vel_atual += velocidade
            print("Velocidade aumentada")
    

    Velocidade aumentada. (%s)" % self.vel_atual)
        else:
            print("Velocidade máxima atingida")

    def freiar(self, velocidade):
        if (self.vel_atual - velocidade) >= 0:
            self.vel_atual -= velocidade
            print("Velocidade reduzida. (%s)" % self.vel_atual)
        else:
            print("Não foi possivel reduzir")




objeto = Carro()

objeto.acelerar(210)

objeto.freiar(50)
