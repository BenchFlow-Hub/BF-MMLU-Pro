import logging
import os
import re

from openai import OpenAI

from benchflow import BaseAgent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MMLUAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.api_key = os.getenv("OPENAI_API_KEY")
        print(self.api_key)

    def call_api(self, env_info):
        prompt = env_info["prompt"]
        input_text = env_info["input_text"]

        try:
            logger.info("[UserAgent]: Calling OpenAI API")
            client = OpenAI(
                api_key=self.api_key,  # This is the default and can be omitted
            )

            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": input_text}
                ],
                model="gpt-4o",
                temperature=0.9,
            )
            content = response.choices[0].message.content
            logger.info(f"[UserAgent]: Got action: {content}")
            return content
        except Exception as e:
            logger.error(f"[UserAgent]: Error calling OpenAI API: {e}")
            raise

if __name__ == "__main__":
    agent_classes = [cls for cls in locals().values() 
                     if isinstance(cls, type) and issubclass(cls, BaseAgent) and cls != BaseAgent]
    agent = agent_classes[-1]()
    agent.run_with_endpoint("0.0.0.0", 10004)