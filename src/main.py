import app
import neat
import os
import pickle
import yaml

def population(checkpoint, config, data):
    if(checkpoint):
        return neat.Checkpointer.restore_checkpoint('neat-checkpoint-%i' % data['CheckpointNumber'])   
    else:
        return neat.Population(config)

def run(data):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                "config-FeedForward.txt")

    pop = population(data['LaunchCheckpoint'], config, data)
    
    reporter = neat.Checkpointer(True)
    reporter.generation = True
    reporter.show_species_detail = True
    pop.add_reporter(reporter)
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    application = app.App(data)

    winner = pop.run(application.EvalGenomes)

    print("Best fitness -> {}".format(winner))
    with open("winner.pkl", "wb") as f:
        pickle.dump(winner, f)
        f.close()


if __name__ == "__main__":
    from yaml import load

    with open('config.yml', 'r') as f:
        data = load(f, Loader=yaml.FullLoader)
   
    if(not data['LaunchWinningGenome']):
        run(data)
    else:
        application = app.App(data)
        application.replay_genome()