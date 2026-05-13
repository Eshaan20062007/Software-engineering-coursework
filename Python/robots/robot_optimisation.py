# robot_optimisation.py
"""
Optimised pizza delivery simulation.
Implements charging optimisation, nearest-pizza allocation, and KPI comparison.
"""

import sys
import os

# This makes sure Python can find the robots folder when we run this file
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from robots.ecosystem.factory import ecofactory

from robots.ecosystem.ecosystem import distance

# Turn on interactive mode so the arena updates live on screen
plt.ion()

DURATION = "1 week" # how long the simulation will run for

SHOW = 0 # whether to show the arena on screen (0 = no, 1 = yes)

PAUSE = 10 # how long to pause for after each update (in milliseconds)

# How many of each bot type to create
N_ROBOTS = 3
N_DROIDS = 3
N_DRONES = 3

HOME = [40, 20, 0] # where bots go to drop off pizzas and charge

BASELINE_CHARGER = [40, 20] # one charger in the middle of the area

BASELINE_THRESHOLD = 0.20 # bots will charge when their battery is below 20%

# Pizzas weigh between 10 and 20 kg in the baseline
BASELINE_MAX_WEIGHT = 20

OPT_CHARGERS = ([20, 10], [60, 10], [20, 30], [60, 30]) # 4 chargers spread out across the area

OPT_MAX_WEIGHT = 35 # pizzas can weigh up to 35 kg in the optimised version

# Each bot type gets its own charge threshold
# Because chargers are spread out, bots can wait longer before charging
OPT_THRESHOLDS = {
    'Robot': 0.15,  # robots are slow so charge a little earlier
    'Droid': 0.12,
    'Drone': 0.10,  # drones are fast so can wait the longest
}

OPPORT_SOC = 0.60 # If a bot's battery is below 60% and there's a charger nearby, it will hopefully go to a charger

OPPORT_DIST = 8.0 # If a bot is within 8 units of a charger, it will charge their battery hopefully

def nearest_charger(bot, chargers):
    closest_charger = None
    closest_distance = float('inf')  # start with infinity so any real distance will be smaller
    
    # Loop through every charger and keep track of whichever one is closest
    for charger in chargers:
        d = distance(bot.coordinates, charger.coordinates)
        if d < closest_distance:
            closest_distance = d
            closest_charger = charger
    
    return closest_charger

def nearest_pizza(bot, pizzas):
    closest_pizza = None
    closest_distance = float('inf')  # start with infinity so any real distance will be smaller
    
    # Loop through every pizza and keep track of whichever one is closest
    for pizza in pizzas:
        d = distance(bot.coordinates, pizza.coordinates)
        if d < closest_distance:
            closest_distance = d
            closest_pizza = pizza
    
    return closest_pizza

# This function implements the opportunistic charging behaviour for bots
def opportunistic_charger(bot, chargers):
    # Do not interrupt a bot that is already heading to a station
    if bot.station is not None:
        return None
    
    # Only charge opportunistically if the battery is below the threshold
    if bot.soc / bot.max_soc >= OPPORT_SOC:
        return None
    
    # Check each charger to see if any are close enough to divert to
    for charger in chargers:
        if distance(bot.coordinates, charger.coordinates) <= OPPORT_DIST:
            return charger
    
    # No charger was close enough so carry on as normal
    return None

def collect_kpis(es):
    # Collect the performance data of every bot in the ecosystem and return as a dictionary

    total_units = 0
    total_weight = 0
    total_energy = 0
    total_distance = 0

    for bot in es.bots:
        total_units += bot.units_delivered
        total_weight += bot.weight_delivered
        total_energy += bot.energy
        total_distance += bot.distance
    
    fleet = {
        'units':     total_units,
        'weight_kg': total_weight,
        'distance':  round(total_distance, 1),
        'energy':    round(total_energy,   1),
    }

    return fleet
