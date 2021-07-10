# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
import math

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"

        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        #print("successorGameState", successorGameState)
        newPos = successorGameState.getPacmanPosition()
        #print("newPos", newPos)
        newFood = successorGameState.getFood()
        #print("newFood", newFood)
        newGhostStates = successorGameState.getGhostStates()
        #print("newGhostStates", newGhostStates)
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #print("newScaredTimes", newScaredTimes)

        "*** YOUR CODE HERE ***"

        score = successorGameState.getScore()
        newFoodList = newFood.asList()
        #print(score)
        #print(newGhostStates[0].getPosition())

        ghostPos = newGhostStates[0].getPosition()
        ghostDistance = manhattanDistance(newPos, ghostPos)
        if ghostDistance > 0:
            score = score - (0.80 / ghostDistance) #less than reciprocol...more risk
            #print("score [ghost]", score)
        
        foodDistance = []

        for food in newFoodList:
            foodDistance.append(manhattanDistance(newPos, food))

        if len(foodDistance) > 0:
            score = score + (0.20 / min(foodDistance)) #adding...relieving risk
            #print("score [food]", score)

        return score


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # When you reach the desired depth you should stop.
        # The ghost is always the last agent to move, unless gameState.isWin() or gameState.isLose() occurs.

        # Things to add:
        # - more than one ghost (i.e. getNumAgents) must iterate through all ghosts then back to pacman
        # - deal with the base case return value, action can't be None... what should it be?

        def dispatch(state, depth, agent):
            if state.isWin() or state.isLose():
                return self.evaluationFunction(state)
            if agent == 0:
                return pacmanValue(state, depth)
            else:
                return ghostValue(state, depth, agent)

        def pacmanValue(state, depth):
            # The agnet after pacman is always a ghost unless there are no more ghosts
            n = state.getNumAgents()
            next_agent = 1
            if n == 1:
                next_agent == 0
            actions = state.getLegalActions(0)
            best_score = -math.inf
            current_score = best_score
            best_action = 'Stop'
            for current_action in actions:
                # Find successor state of each action
                successorState = state.generateSuccessor(0, current_action)
                # Start on the first ghost move afterwards
                current_score = dispatch(successorState, depth, next_agent)
                # Once we have found the highest score of the current_action, test whether it's a better move
                if best_score < current_score:
                    best_score = current_score
                    best_action = current_action
            # If we have reached the parent node of the tree, return the optimal action
            if depth == 0:
                return best_action
            # If we are still deep in the tree, return scores associated with the best action
            else:
                return best_score

        def ghostValue(state, depth, ghost):
            n = state.getNumAgents()
            next_agent = ghost + 1
            if ghost == n - 1:
                next_agent = 0
            actions = state.getLegalActions(ghost)
            best_score = float("inf")
            current_score = best_score
            for current_action in actions:
                successorState = state.generateSuccessor(ghost, current_action)
                # If we have reached the final ghost, next agent is the pacman (back to the beginning of the line)
                if next_agent == 0:
                    # After the final ghost has gone, we have dived one entire level of depth
                    # If we have reached the final depth level, no need to keep diving, return current_score
                    if depth == self.depth - 1:
                        current_score = self.evaluationFunction(successorState)
                    else:
                    # If we have not reached the final depth, dive another level (i.e. all the agents) with the next starting agent as Pacman
                        current_score = dispatch(successorState, depth + 1, next_agent)
                # Otherwise, go to the next ghost agent
                else:
                    current_score = dispatch(successorState, depth, next_agent)
                # Once we have found the highest score of the current_action, test whether it's a better move
                if best_score > current_score:
                    # Update new best score
                    best_score = current_score
            return best_score

        return pacmanValue(gameState, 0)

        util.raiseNotDefined()


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def dispatch(state, depth, agent, a, b):
            if state.isWin() or state.isLose():
                return self.evaluationFunction(state)
            if agent == 0:
                return pacmanValue(state, depth, a, b)
            else:
                return ghostValue(state, depth, agent, a, b)

        def pacmanValue(state, depth, a, b):
            # The agnet after pacman is always a ghost unless there are no more ghosts
            n = state.getNumAgents()
            next_agent = 1
            if n == 1:
                next_agent == 0
            actions = state.getLegalActions(0)
            best_score = -math.inf
            current_score = best_score
            best_action = 'Stop'
            for current_action in actions:
                # Find successor state of each action
                successorState = state.generateSuccessor(0, current_action)
                # Start on the first ghost move afterwards
                current_score = dispatch(successorState, depth, next_agent, a, b)
                # Once we have found the highest score of the current_action, test whether it's a better move
                if best_score < current_score:
                    best_score = current_score
                    best_action = current_action
                if best_score > b:
                    return best_score
                # Update our alpha value for Pacman's best option on path to root
                a = max(best_score, a)
            # If we have reached the parent node of the tree, return the optimal action
            if depth == 0:
                return best_action
            # If we are still deep in the tree, return scores associated with the best action
            else:
                return best_score

        def ghostValue(state, depth, ghost, a, b):
            n = state.getNumAgents()
            next_agent = ghost + 1
            if ghost == n - 1:
                next_agent = 0
            actions = state.getLegalActions(ghost)
            best_score = float("inf")
            current_score = best_score
            for current_action in actions:
                successorState = state.generateSuccessor(ghost, current_action)
                # If we have reached the final ghost, next agent is the pacman (back to the beginning of the line)
                if next_agent == 0:
                    # After the final ghost has gone, we have dived one entire level of depth
                    # If we have reached the final depth level, no need to keep diving, return current_score
                    if depth == self.depth - 1:
                        current_score = self.evaluationFunction(successorState)
                    else:
                    # If we have not reached the final depth, dive another level (i.e. all the agents) with the next starting agent as Pacman
                        current_score = dispatch(successorState, depth + 1, next_agent, a, b)
                # Otherwise, go to the next ghost agent
                else:
                    current_score = dispatch(successorState, depth, next_agent, a, b)
                # Once we have found the highest score of the current_action, test whether it's a better move
                if best_score > current_score:
                    # Update new best score
                    best_score = current_score
                if best_score < a:
                    return best_score
                # Update our beta value for Ghost's best option on path to root
                b = min(best_score, b)
            return best_score

        return pacmanValue(gameState, 0, -math.inf, math.inf)

        util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        def value(state, depth, agent):
            if state.isWin() or state.isLose():
                return self.evaluationFunction(state)
            if agent == 0:
                return pacmanValue(state, depth)
            else:
                return ghostValue(state, depth, agent)

        def pacmanValue(state, depth):
            # The agnet after pacman is always a ghost unless there are no more ghosts
            n = state.getNumAgents()
            next_agent = 1
            if n == 1:
                next_agent == 0
            actions = state.getLegalActions(0)
            best_score = -math.inf
            current_score = best_score
            best_action = 'Stop'
            for current_action in actions:
                # Find successor state of each action
                successorState = state.generateSuccessor(0, current_action)
                # Start on the first ghost move afterwards
                current_score = value(successorState, depth, next_agent)
                # Once we have found the highest score of the current_action, test whether it's a better move
                if best_score < current_score:
                    best_score = current_score
                    best_action = current_action
            # If we have reached the parent node of the tree, return the optimal action
            if depth == 0:
                return best_action
            # If we are still deep in the tree, return scores associated with the best action
            else:
                return best_score

        def ghostValue(state, depth, ghost):
            n = state.getNumAgents()
            next_agent = ghost + 1
            if ghost == n - 1:
                next_agent = 0
            actions = state.getLegalActions(ghost)
            p = 1 / len(actions)
            current_score = 0
            exp_score = 0
            for current_action in actions:
                successorState = state.generateSuccessor(ghost, current_action)
                # If we have reached the final ghost, next agent is the pacman (back to the beginning of the line)
                if next_agent == 0:
                    # After the final ghost has gone, we have dived one entire level of depth
                    # If we have reached the final depth level, no need to keep diving, return current_score
                    if depth == self.depth - 1:
                        current_score = self.evaluationFunction(successorState)
                        exp_score += p * current_score
                    else:
                    # If we have not reached the final depth, dive another level (i.e. all the agents) with the next starting agent as Pacman
                        current_score = value(successorState, depth + 1, next_agent)
                        # Update the probability of the score
                        exp_score += p * current_score
                # Otherwise, go to the next ghost agent
                else:
                    current_score = value(successorState, depth, next_agent)
                    exp_score += p * current_score

            return exp_score


        return pacmanValue(gameState, 0)


        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    if currentGameState.isWin():
        return math.inf
    if currentGameState.isLose():
        return -math.inf

    score = scoreEvaluationFunction(currentGameState)
    foodStates = currentGameState.getFood()
    foodStatesList = foodStates.asList()
    currentPosition = currentGameState.getPacmanPosition()
    ghostDistances = []
    foodDistances = []

    for state in range(1, currentGameState.getNumAgents()):
        currentGhostDistance = manhattanDistance(currentGameState.getGhostPosition(state), currentPosition)
        ghostDistances.append(currentGhostDistance)
    
    if min(ghostDistances) < 2:
        return math.inf

    for food in foodStatesList:
        currentFoodDistance = manhattanDistance(food, currentPosition)
        foodDistances.append(currentFoodDistance)

    # kinda random
    return 1.5*min(ghostDistances) + max(ghostDistances) + score - 8*currentGameState.getNumFood() - 2*min(foodDistances) - max(foodDistances) 
    
    # util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
