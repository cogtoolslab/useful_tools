import prolific_generate_bonusses

# db = 'curiophysion'
db = 'sketch_program_synthesis_human'

# collection = 'dominoes'
collection = 'discriminative'

# iteration = 'full_1'
iteration = 'pilaot2'

prolific_generate_bonusses.get_bonusses_from_mongo(db, collection, iteration, prolific_generate_bonusses.comprehension_bonus_function
)