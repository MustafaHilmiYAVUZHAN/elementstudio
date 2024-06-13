import numpy as np

# Ortam boyutları
GRID_SIZE = 3
START_STATE = (0, 0)
GOAL_STATE = (2, 2)

# Eylemler (yukarı, aşağı, sol, sağ)
ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']
NUM_ACTIONS = len(ACTIONS)

# Q değerlerinin başlatılması
Q = np.zeros((GRID_SIZE, GRID_SIZE, NUM_ACTIONS))

# Q-learning parametreleri
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
NUM_EPISODES = 1000
MAX_STEPS_PER_EPISODE = 100

# Eğitim döngüsü
for episode in range(NUM_EPISODES):
    state = START_STATE
    for step in range(MAX_STEPS_PER_EPISODE):
        # Eylem seçimi - epsilon-greedy yöntem
        if np.random.rand() < 0.1:
            action = np.random.choice(NUM_ACTIONS)
        else:
            action = np.argmax(Q[state[0], state[1]])

        # Yeni durum ve ödül alınması
        if ACTIONS[action] == 'UP':
            new_state = (max(state[0] - 1, 0), state[1])
        elif ACTIONS[action] == 'DOWN':
            new_state = (min(state[0] + 1, GRID_SIZE - 1), state[1])
        elif ACTIONS[action] == 'LEFT':
            new_state = (state[0], max(state[1] - 1, 0))
        elif ACTIONS[action] == 'RIGHT':
            new_state = (state[0], min(state[1] + 1, GRID_SIZE - 1))
        
        if new_state == GOAL_STATE:
            reward = 1
        else:
            reward = 0
        
        # Q değerlerinin güncellenmesi
        Q[state[0], state[1], action] += LEARNING_RATE * (reward + 
                    DISCOUNT_FACTOR * np.max(Q[new_state[0], new_state[1]]) - Q[state[0], state[1], action])
        
        # Yeni durumu güncelle
        state = new_state
        
        # Hedefe ulaşıldıysa episode'yi sonlandır
        if state == GOAL_STATE:
            break

# Eğitim sonrası agent'in performansını test etme
state = START_STATE
steps = 0
while state != GOAL_STATE and steps < MAX_STEPS_PER_EPISODE:
    action = np.argmax(Q[state[0], state[1]])
    print(f"State: {state}, Action: {ACTIONS[action]}")
    
    if ACTIONS[action] == 'UP':
        state = (max(state[0] - 1, 0), state[1])
    elif ACTIONS[action] == 'DOWN':
        state = (min(state[0] + 1, GRID_SIZE - 1), state[1])
    elif ACTIONS[action] == 'LEFT':
        state = (state[0], max(state[1] - 1, 0))
    elif ACTIONS[action] == 'RIGHT':
        state = (state[0], min(state[1] + 1, GRID_SIZE - 1))
    
    steps += 1
    
if state == GOAL_STATE:
    print("Goal reached!")
else:
    print("Agent couldn't reach the goal.")
