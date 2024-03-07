import pygame
import game
import neat
import pickle
import time

class App:
    def __init__(self, data):
        self.data = data
        self.generation = -1
        self.generationlp = -1
        self.screen_width = 550 
        self.screen_height = 550
        self.game = game.Game(self.screen_width,self.screen_height)
        self.screen = None
        self.genomes = []
        self.networks = []
        self.tries = 0
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pacman simulation")
        pygame.time.Clock().tick(30)
        self.MaxScore = 0


    def EvalGenomes(self, raw_genomes: list[neat.DefaultGenome], config):
        
        self.tries = 0
        self.networks = []
        self.genomes = []

        for genome_id, g in raw_genomes:
            net = neat.nn.FeedForwardNetwork.create(g, config)
            self.networks.append(net)
            g.fitness = 0
            self.genomes.append(g)

        self.generation+=1

        for i in range(len(self.genomes)):
            #print("Curren genome -> {}".format(genomes[i]))
            self.Run(game_end_callback=lambda: self.RestartGame(i),
                game_update_callback=lambda: self.UpdateEvent(i),
                eat=lambda: self.AddValToFitness(i, 1))


    def Run(self, game_end_callback, game_update_callback, eat):
        self.game.Restart(self.screen_width,self.screen_height)
        self.game.Start(self.screen,game_end_callback, game_update_callback, eat, self.data)


    def RestartGame(self, gen_id):
        self.game.Restart1()
        
        if(self.MaxScore < self.game.map.score):
            self.generationlp = self.generation
            self.MaxScore = self.game.map.score

        #print("MaxScore: "+str( self.MaxScore) +"; ID: "+str(gen_id) + "; fitness: " + str(self.genomes[gen_id].fitness) + "; score: " + str(self.game.map.score) + "; p1: "+str(self.p1) +"; p2: "+ str(self.p2)+"; p3: "+str(self.p3))
        print("ID: "+str(gen_id) + "; fitness: " + str(self.genomes[gen_id].fitness) + "; score: " + str(self.game.map.score) + ";")

        self.tries += 1

    def AddValToFitness(self, gen_id, val):
        self.genomes[gen_id].fitness += val

    def UpdateEvent(self, gen_id):
        self.font = pygame.font.SysFont("Verdana", 15)
        score_text = self.font.render("G:"+str(self.generation), True, (255,255,255))
        self.screen.blit(score_text, (475, 208))

        score_text = self.font.render("M:"+str(self.MaxScore), True, (255,255,255))
        self.screen.blit(score_text, (475, 308))

        score_text = self.font.render("L:"+str(self.generation-self.generationlp), True, (255,255,255))
        self.screen.blit(score_text, (475, 258))
        
        #time.sleep(0.1)
        
        v = []

        p1 = self.game.pacMan.LocalCoordinates(self.game.map)
        g1 = self.game.goustRed.LocalCoordinates(self.game.map)
        g2 = self.game.goustPink.LocalCoordinates(self.game.map)
        g3 = self.game.goustBlue.LocalCoordinates(self.game.map)
        g4 = self.game.goustOrange.LocalCoordinates(self.game.map)

        if(g1[0]>=0):
            g1 = self.game.map.EuclideanDistances(p1[0], p1[1], g1[0], g2[1])
        else:
            g1 = -1
        if(g2[0]>=0):
            g2 = self.game.map.EuclideanDistances(p1[0], p1[1], g2[0], g2[1])
        else:
            g2 = -1
        if(g3[0]>=0):
            g3 = self.game.map.EuclideanDistances(p1[0], p1[1], g3[0], g3[1])
        else:
            g3 = -1
        if(g4[0]>=0):
            g4 = self.game.map.EuclideanDistances(p1[0], p1[1], g4[0], g4[1])
        else:
            g4 = -1
        v += self.game.map.AmountFoodDestination(self.game.pacMan) + [ g1, g2, g3, g4 ]

        print(v)

        outputs = self.networks[gen_id].activate((tuple(v)))
        general_output = 0
    
        maxVal = 0
        for idx, output in enumerate(outputs):
            if output > maxVal:
                maxVal = output
                general_output = idx
        
        #print(general_output)

        if maxVal > 0.8:
            if(general_output==0):
                if(self.game.pacMan.CanPass2("LEFT", self.game.map)):
                    self.game.pacMan.direction = "LEFT"
            elif(general_output==1):
                if(self.game.pacMan.CanPass2("RIGHT", self.game.map) ):
                    self.game.pacMan.direction = "RIGHT"
            elif(general_output==2):
                if(self.game.pacMan.CanPass2("TOP", self.game.map) ):
                    self.game.pacMan.direction = "TOP"
            elif(general_output==3):
                if(self.game.pacMan.CanPass2("BOT", self.game.map) ):
                    self.game.pacMan.direction = "BOT"

    def replay_genome(self, config_path, genome_path="winner.pkl"):
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, "config-FeedForward.txt")
        with open(genome_path, "rb") as f:
            genome = pickle.load(f)
        genomes = [(10, genome)]
        self.EvalGenomes(genomes, config)
