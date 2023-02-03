
import game_constants
import game


if __name__ == '__main__':
    game = game.Game()
    game.presetention()
    game.screen.fill(game_constants.BLACK)
    while game.runing:
        
        if game.playing:
            game.game_loop()
        else:
            game.state_stack.clear()
            game.playing = True
            game.load_states()
        
        
    

