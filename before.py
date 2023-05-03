import var
import play.playing

def beforeplay():
    var.nome = "Erik"
    var.classeipt = ["Guerreiro", "Mago", "Ladino"]
    var.classe = 0
    play.playing.startGame()

beforeplay()