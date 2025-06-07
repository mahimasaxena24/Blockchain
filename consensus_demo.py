import random

# Mock validators
def create_validators():
    miners = [{'power': random.randint(1, 100)} for _ in range(3)]
    stakers = [{'stake': random.randint(1, 100)} for _ in range(3)]
    voters = [{'votes': random.randint(1, 100)} for _ in range(3)]
    return miners, stakers, voters

def pow_selection(miners):
    selected = max(miners, key=lambda x: x['power'])
    print(f"PoW selected validator with power: {selected['power']}")
    print("Selection Logic: In Proof of Work (PoW), the validator with the highest computational power is selected to mine the next block.")
    return selected

def pos_selection(stakers):
    selected = max(stakers, key=lambda x: x['stake'])
    print(f"PoS selected validator with stake: {selected['stake']}")
    print("Selection Logic: In Proof of Stake (PoS), the validator with the highest stake (investment) is selected to create the next block.")
    return selected

def dpos_selection(voters):
    selected = random.choice(voters)
    print(f"DPoS selected validator with votes: {selected['votes']}")
    print("Selection Logic: In Delegated Proof of Stake (DPoS), a validator is randomly selected based on the votes they received from stakeholders.")
    return selected

# Simulate consensus mechanisms
def simulate_consensus():
    miners, stakers, voters = create_validators()
    
    print("Consensus Mechanism Simulation:")
    pow_selected = pow_selection(miners)
    pos_selected = pos_selection(stakers)
    dpos_selected = dpos_selection(voters)

simulate_consensus()
