import tensorflow as tf
from tensorflow.keras.optimizers import Adam, RMSprop
import numpy as np
import random
from collections import deque
from parameters import params
from models import Net
from utils import LinearAnneal


class DQN(params):
    def __init__(self, env):
        self.env = env
        self.n_action = len(self.env.action_space)
        self.observation = self.env.state_size
        
        # initialize model
        self._model_init()
        
        # initialize memory
        self.replay_memory = deque(maxlen=self.MEMORY_SIZE)
        self.step = 0
        
        # greedy policy
        self.epsilon = LinearAnneal(self.EPSILON, self.MIN_EPSILON, self.EPISODES)
    
    def _model_init(self):
        self.policy_model = Net(self.env)
        self.target_model = Net(self.env)
        self.policy_model.compile(loss='huber_loss', optimizer=Adam(learning_rate=self.LR))
        self.target_model.compile(loss='huber_loss', optimizer=Adam(learning_rate=self.LR))
        self._update_model()
        
    def _update_model(self):
        self.target_model.set_weights(self.target_model.get_weights())
    
    def _update_memory(self, transitions):
        self.replay_memory.append(transitions)
    
    def _choose_action(self, state):
        
        if random.random() < self.epsilon.anneal():
            return np.argmax(self.policy_model.predict(state)[0])
        return random.randint(0, 2)
    
    def _optimize(self):
        if len(self.replay_memory) < self.BATCH_SIZE:
            return
        
        # pick sample batch from replay memory
        batch = random.sample(self.replay_memory, self.BATCH_SIZE)
        states = np.array([transition[0] for transition in batch])
        next_states = np.array([transition[2] for transition in batch])
        
        q = self.policy_model.predict(states)
        next_q = self.target_model.predict(next_states)
        
        for index, (state, action, next_state, reward) in enumerate(batch):
            q[index][action] = (1 - self.GAMMA) * q[index][action] + self.GAMMA * (reward + np.amax(next_q[index])*self.DISCOUNT)
        
        self.policy_model.fit(states, q, verbose=0)
        
    def train(self):
        for episode in range(1, self.EPISODES+1):
            self.env.reset()
            state = self.env.reset()
            done = False
            total_reward = 0
            while not done:
                action = self._choose_action(state)
                next_state, reward, done = self.env.step(action)
                self._update_memory((state, action, next_state, reward))
                self._optimize()
                total_reward += reward
                state = next_state
            
            if episode % self.MODEL_UPDATE == 0:
                self._update_model()
            
            print(f'episode: {episode} | reward {total_reward}')