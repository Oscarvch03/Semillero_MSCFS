# CLASES Y FUNCIONES ###########################################################
################################################################################

class Agent:

    def __init__(self, estrategia, score, politica, vecinos):
        # (estrategia inicial, puntaje inicial, politica inicial, lista de vecinos)
        # self.estrategias = [estrategia]
        # if(score != None):
        #     self.score = [score]
        # else:
        #     self.scores = []
        # self.politicas = [politica]
        self.vecinos = vecinos
        self.actual_pol = politica
        self.new_pol = politica
        self.actual_scr = score
        self.actual_est = estrategia



    def __str__(self):
        msg = "Agent With: \n"
        msg += "E: {0} \n".format(self.actual_est)
        msg += "S: {0} \n".format(self.actual_scr)
        msg += "P: {0} \n".format(self.actual_pol)
        msg += "V: {0}".format(self.vecinos)
        return msg

################################################################################

class Politica:

    def __init__(self, num_politica): # num_politica = 0, 1, 2, ..., 7
        self.num_politica = num_politica
        self.politica = None

        pol = {}
        if(num_politica == 0):
            pol = {(0, 0): 0, (1, 1): 0, (1, -1): 0}
        elif(num_politica == 1):
            pol = {(0, 0): 0, (1, 1): 0, (1, -1): 1}
        elif(num_politica == 2):
            pol = {(0, 0): 0, (1, 1): 1, (1, -1): 0}
        elif(num_politica == 3):
            pol = {(0, 0): 0, (1, 1): 1, (1, -1): 1}
        elif(num_politica == 4):
            pol = {(0, 0): 1, (1, 1): 0, (1, -1): 0}
        elif(num_politica == 5):
            pol = {(0, 0): 1, (1, 1): 0, (1, -1): 1}
        elif(num_politica == 6):
            pol = {(0, 0): 1, (1, 1): 1, (1, -1): 0}
        elif(num_politica == 7):
            pol = {(0, 0): 1, (1, 1): 1, (1, -1): 1}
        else:
            print("The policy is a number in [0, 7]. ")

        self.politica = pol


    def __str__(self):
        msg = "Policy {0} \n".format(self.num_politica)
        msg += "(0, 0): {0} \n".format(self.politica[(0, 0)])
        msg += "(1, 1): {0} \n".format(self.politica[(1, 1)])
        msg += "(1, -1): {0}".format(self.politica[(1, -1)])
        return msg

################################################################################
