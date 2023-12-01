import app
import neat
import os
import pickle
CHECKPOINT = 1
isCheckpoint = False

def population(checkpoint, config):
    if(checkpoint):
        return neat.Checkpointer.restore_checkpoint('neat-checkpoint-%i' % CHECKPOINT)   
    else:
        return neat.Population(config)

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    pop = population(False, config)
    
    reporter = neat.Checkpointer(True)
    reporter.generation = True
    reporter.show_species_detail = True
    pop.add_reporter(reporter)
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    application = app.App()

    winner = pop.run(application.EvalGenomes)

    print("Best fitness -> {}".format(winner))
    with open("winner.pkl", "wb") as f:
        pickle.dump(winner, f)
        f.close()

def openConfig():
    local_dir = os.path.dirname(__file__)
    return os.path.join(local_dir, "..\\config-FeedForward.txt")

def general():
    run(openConfig())

def replayWinGanome():
    application = app.App()
    application.replay_genome(openConfig())

if __name__ == "__main__":
    if(not isCheckpoint):
        general()
    else:
        replayWinGanome()