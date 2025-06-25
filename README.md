# Pixtrace

Project to process the image and generate the business analytics of the product.

1. Analyze the past market history of the product.
2. Predict the future market history of the product.
3. Competitor Analysis of the product.
4. List of product distributors.
5. Youtube review of the products

This project is based of Open AI api to process and analyze the product.
Where as youtube API to get the generic review of the product.

# System Requirement

- Python 3.13.5
- Django 5.2.3
- Mysql 9.2.0

# Installation

1. Create a Database.
2. Set the evironment variables
    - PIXTRACE_DATABASE_NAME [ DB Name ]
    - PIXTRACE_DATABASE_USERNAME [ DB Username ]
    - PIXTRACE_DATABASE_PASSWORD [ DB Password ]
    - OPENAI_API_KEY [ ChatGPT API key ]
    - YOUTUBE_API_KEY [ Google API Key for Youtube]
3. Run <i>Python manage.py migrate</i>
4. Run <i>Python manage.py createsuperuser</i>

# Preview

![Alt text](static/images/preview1.png)

![Alt text](static/images/preview2.png)