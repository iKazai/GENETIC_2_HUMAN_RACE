"""
    This file contains the fitness function
"""
import math
from src.runner import Runner

AIR_RESISTANCE_FACTOR = 0.005 
GRAVITY_FACTOR = 9.81 * 0.02  
POWER_TO_VELOCITY_RATIO = 0.1
THIGH_CONTRIBUTION = 0.7
CALF_CONTRIBUTION = 1 - THIGH_CONTRIBUTION

# IDEAL FACTORS (TODO)
IDEAL_FEMUR_TIBIA_RATIO = None
BASE_EFFICIENCY_SCORE = None

##############################################################
#                                                            #
#                 ---- AUX FUNCTIONS ----                    #
#                                                            #
##############################################################


"""
@resume This function calculates the maximum propulsion capacity of a Runner.
Its raw strength.
@key_genes thighs_size, calf_size, weight, fat_ratio
@returns Relative Power used to calculate the maximum theoric speed
"""
def calculate_power(runner: Runner):
    muscle_weight = runner.get_weight() * (1 - runner.get_fat_ratio())
    muscle_factor = ( runner.get_thighs_size() * THIGH_CONTRIBUTION ) + ( runner.get_calf_size() * CALF_CONTRIBUTION )
    return muscle_weight * muscle_factor


"""
@resume This function calculates the percentage of energy that is converted into forward motion.
@key_genes femur_tibia_ratio, cadence_length_ratio
@returns Biomechanics efficiency factor (0.0 - 1.0)
@notes height is not a key_gene as the biomechanic efficiency is a factor that is calculated 
given the "shape" of a Runner. Therefore, its height must be seen as a scale factor and must not affect the efficiency factor.
@notes the returned value must not be K1 * femur_tibia_ratio + K2 * cadence_length_ratio because this 
would force the GA to converges the two genes to their maximum value with no complex relevance 
"""
def calculate_biomechanics_efficiency(runner):
    efficiency = None
    raise Exception("TODO")
    return max(0.0, min(1.0, efficiency))

"""
@resume This function calculates the energy cost per second run by the Runner at a given speed.
@key_genes weight, height, fasrt_twitch_ratio, biomechanics_efficiency
@returns Energy cost in Joules per second
"""
def calculate_energy_cost(runner: Runner, speed: float):
    raise Exception("TODO")

##############################################################
#                                                            #
#             ---- MAIN FITNESS FUNCTION ----                #   
#                                                            #
##############################################################

"""
@resume This function calculates the fitness of a Runner.
The fitness is based on the minimum time the Runner can achieve given its genes.
@key_genes All genes
@returns Fitness score (the higher the better)
"""
def calculate_fitness(runner: Runner):
    raise Exception("TODO")