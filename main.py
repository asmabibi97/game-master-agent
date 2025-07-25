import os 
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI
from agents.run import RunConfig
from game_tools import get_career_roadmap
from game_tools import generate_event ,roll_dice

load_dotenv()
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model =OpenAIChatCompletionsModel(
    model="gemini-2.0-flash" , openai_client=client)
config= RunConfig(model=model, tracing_disable=True)

narrator_agent=Agent(
    name="NarratorAgent",
    instruction="you narate the adventure.ask the player for choicesw.",
    model=model,
    
)
monster_agent=Agent(
    name="MonsterAgent",
    instruction="you handle monster encounters using roll_dice and generate_event.",
    model=model,
    tools=[roll_dice,generate_event]
)
item_agent=Agent(
    name="ItemAgent",
    instructions="you provide rewards or items to the player.",
    model=model
)
def main():
    print("/nWelcome to fantasy game/n")
    interest=input("do you enter the forest or turn back->")

    result1=Runner.run_sync(narrator_agent, choice,run_config=config)
  print('/nstory:",result1.final_output')

    result2=Runner.run_sync(monster_agent,"start encounter",run_config=config)
    print("/nencounter:",result2.final_output)

    result3=Runner.run_sync(job_agent,field,run_config=config)
    print("/nreward:",result3.final_output)


if __name__=="__main__":
    main()


