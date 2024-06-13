import numpy as np
import random

# Q-table oluşturma
Q = np.zeros((9, 4))  # 9 durum (3x3 matris için), 4 aksiyon

# Hedef matris
goal = 8

# Hareketler (0: Yukarı, 1: Aşağı, 2: Sol, 3: Sağ)
actions = [0, 1, 2, 3]

# Ödül matrisi
R = np.array([
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],  # 0
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],  # 1
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],  # 2
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],  # 3
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],  # 4
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],  # 5
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],  # 6
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],  # 7
    [-1, -1, -1, -1, -1, -1, -1, -1, 100]  # 8 (hedef)
])

# Q-learning parametreleri
gamma = 0.8
alpha = 0.1
epsilon = 0.1
epochs = 1000

# Q-learning algoritması
for _ in range(epochs):
    # Rastgele bir başlangıç durumu seç
    state = random.randint(0, 8)
    
    # Hedefe ulaşana kadar
    while state != goal:
        # Epsilon-greedy yöntem ile hareket seçimi
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            action = np.argmax(Q[state])
        
        # Yeni durum ve ödül hesaplama
        next_state = action
        reward = R[state, action]
        
        # Q değerini güncelleme
        Q[state, action] = (1 - alpha) * Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state]))
        
        # Yeni durumu güncelleme
        state = next_state

# Eğitim sonrası Q-table'ı yazdırma
print("Q-table:")
print(Q)

# Eğitim sonrası ajanın performansını test etme
state = 0  # Başlangıç durumu
steps = [state]

while state != goal:
    action = np.argmax(Q[state])
    state = action
    steps.append(state)

print("Optimal yol:")
print(steps)
