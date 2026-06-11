from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os 

os.environ['LANGSMITH_PROJECT'] = 'Sequencial LLM App'

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenRouter(model = "openai/gpt-4o-mini", temperature = 0.7)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
config = {
    "run_name": "Sequential Chain",
    "tags": ["llm_app", 'summarization', 'report_generation'],
    "metadata": {"model": "gpt-4o-mini", 'model_temp': "0.7", "parser": "stroutputparser"}
}

result = chain.invoke({'topic': 'Unemployment in India'}, config=config)

print(result)
