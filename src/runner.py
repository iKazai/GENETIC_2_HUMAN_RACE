import random

class Runner:
    """
    Represents an individual (a runner) in the genetic algorithm.
    Its attributes are the genes that determine its performance.
    """

    # Constants that define the realistic value ranges of the genes
    GENE_RANGES = {
        # Muscles (power factors)
        'calf_size': (0.1, 1.0),       # Use/Size of calves
        'thighs_size': (0.2, 1.0),     # Use/Size of thighs
        
        # Skeleton/Structure (Biomechanic factors)
        'height': (1.60, 2.00),        # Height in meters (AJOUTÉ)
        'weight': (50.0, 95.0),        # Total weight in kg (AJOUTÉ)
        'femur_tibia_ratio': (0.8, 1.2), # Ratio between the femur and the tibia
        
        # Body and muscle composition
        'fast_twitch_ratio': (0.1, 0.9), # Ratio of fast-twitch fibers
        'fat_ratio': (0.05, 0.25),       # Percentage of body fat

        # Techniques/Strategy
        'cadence_length_ratio': (0.1, 0.9),  # 0.1: High cadence (small steps) / 0.9: Long strides (low cadence)
    }
    
    # Liste de tous les gènes pour une initialisation compacte
    GENE_ATTRIBUTES = list(GENE_RANGES.keys())

    def __init__(self, **kwargs):
        """
        Initializes a runner. Attributes can be passed as keyword arguments (kwargs)
        for crossover, or generated randomly if not provided (initial population).
        """
        
        # Initialisation de tous les gènes en utilisant une boucle compacte
        for gene_name in self.GENE_ATTRIBUTES:
            # Get the kwargs value or generate a random realistic value
            gene_value = kwargs.get(gene_name, self._get_random_gene(gene_name))
            setattr(self, gene_name, gene_value)

        # Non-genetic variable used for the genetic algorithm
        self.fitness = 0.0 # Stores the performance score (speed)

    def _get_random_gene(self, gene_name):
        """ Generates a random value within the defined range for a gene. """
        min_val, max_val = self.GENE_RANGES[gene_name]
        return random.uniform(min_val, max_val)

    def get_genes_as_dict(self):
        """ Returns all genes in a dictionary for easy manipulation (crossover, mutation). """
        # Utilise la liste des attributs pour s'assurer que seuls les gènes sont retournés
        return {name: getattr(self, name) for name in self.GENE_ATTRIBUTES}

    def get_weight(self):
        return self.weight
    
    def get_fat_ratio(self):
        return self.fat_ratio
    
    def get_thighs_size(self):
        return self.thighs_size
    
    def get_calf_size(self):
        return self.calf_size

    def __repr__(self):
        """ Representation for readable output. """
        return (f"Runner(Fitness: {self.fitness:.2f} | "
                f"Taille: {self.height:.2f}m | Poids: {self.weight:.1f}kg")


# Example
if __name__ == '__main__':
    # 1. Create a random runner (initial population)
    random_runner = Runner()
    print("Random runner:")
    print(random_runner.get_genes_as_dict())
    print(random_runner)
    
    # 2. Create a specific runner after mutation
    specific_runner = Runner(
        thighs_size=0.9,
        height=1.75,
        fast_twitch_ratio=0.85,
        cadence_length_ratio=0.75
    )
    print("\nSpecific runner (Newborn) :")
    print(specific_runner.get_genes_as_dict())