import json
import os
from openai import OpenAI
from app.helper.ImageConverter import encode_image
import re


def getOpenAIClient():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def detectImage(product):
    client = getOpenAIClient()
    if client is not None:
        try:
            image = encode_image(product.image)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": (
                            "What product or brand do you recognize in this image?.Give me the detail name with its model also."
                            "Use this JSON format in text: {\"name\":\"\",\"category\":\"\"}"
                        )
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image
                                }
                            }
                        ]
                    }
                ]
            )
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            print(e)
            raise Exception("Failed to analyze the image.Please try again later")
    return None


def analyze(product):
    client = getOpenAIClient()
    if client is not None:
        try:
            response = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {
                        "role": "user",
                        "content": (
                                "Please generate a comprehensive business intelligence report for" + str(product.name) +
                                ".First, create a market analysis timeline from previous 5 years to upcoming 5 years. For each year, include the following fields: year, units_sold, average_rate, sales, growth_rate, market_trend (use 'growth', 'plateau', or 'decline'), market_position, market_drivers, market_challenges, and remarks. All values should be formatted as strings. Provide realistic historical data from past 5 years and sensible projections for upcoming 5 years. Each year’s market_drivers and market_challenges should be written in paragraph form, clearly describing the forces influencing performance, such as pricing, consumer behavior, competition, or technology."
                                "Second, create atleast 5  competitor analysis section in the same JSON format. Each competitor entry should include: brand, model, average_price, target_audience, key_features, strengths, weaknesses, market_share_estimate, and positioning. The positioning field should compare the competitor’s positioning relative to the product."
                                "All the numeric values in 2 digit decimal format like '13.0 billion converted to a number is:13000000000' and ensure the tone, metrics, and content feel authentic and tailored to the product’s market.Combine all the json file with key for first as product_analysis and for second as competitor_analysis. Generate in json format."
                                "Use this JSON format in text: {\"product_analysis\":[{\"year\":\"\",\"units_sold\":\"\",\"average_rate\":\"\",\"sales\":\"\",\"growth_rate\":\"\",\"market_trend\":\"\",\"market_position\":\"\",\"market_drivers\":\"\",\"market_challenges\":\"\",\"remarks\":\"\"}],\"competitor_analysis\":[{\"brand\":\"\",\"model\":\"\",\"average_price\":\"\",\"target_audience\":\"\",\"key_features\":\"\",\"strengths\":\"\",\"weaknesses\":\"\",\"market_share_estimate\":\"\",\"positioning\":\"\"}]}"
                        )
                    },
                ]
            )
            content = response.choices[0].message.content
            print(content)
            formatted = re.sub(r"```json|```", "", content).strip()
            print(formatted)
            try:
                return json.loads(formatted)
            except json.JSONDecodeError:
                return formatted
        except Exception as e:
            print(e)
            raise Exception("Failed to analyze the image.Please try again later")
    return None
