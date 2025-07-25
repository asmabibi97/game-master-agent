from agents import functional_tool
import random

@functional_tool
def roll_dice()->str:
    return f"you rolled a {random.randint(1,6)}!"

@functional_tool
def generate_event()->str:
    events =[
        "you encountered a dragon!",
        "you found a tressure chest.",
        "you fell into a trap!",
        "you met a mysterious wizard"
    ]
    return random.choice(events)