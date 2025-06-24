import json
import os
from openai import OpenAI
from app.helper.ImageConverter import encode_image

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze(product):
    try:
        image = encode_image(product.image)
        # response = client.chat.completions.create(
        #     model="gpt-4o",
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": 'Please generate a comprehensive business intelligence report for the image. The output should consist of two well-structured JSON arrays with name and category.First, create a market analysis timeline from previous 5 years to upcoming 5 years. For each year, include the following fields: year, units_sold, average_rate, sales, growth_rate, market_trend (use "growth", "plateau", or "decline"), market_position, market_drivers, market_challenges, and remarks. All values should be formatted as strings. Provide realistic historical data from past 5 years and sensible projections for upcoming 5 years. Each year’s market_drivers and market_challenges should be written in paragraph form, clearly describing the forces influencing performance, such as pricing, consumer behavior, competition, or technology.Second, generate atleast 20  set of product review entries from social media platforms like YouTube, Instagram, Twitter, TikTok, Reddit, and Google Reviews. Each review should include: platform, link, author, caption, and engagement. The captions should sound like real user-generated content, reflecting either praise, critique, or insight. Ensure the engagement field is appropriate for each platform, such as views, likes, comments, or star ratings.Third, create atleast 5  competitor analysis section in the same JSON format. Each competitor entry should include: brand, model, average_price, target_audience, key_features, strengths, weaknesses, market_share_estimate, and positioning. The positioning field should compare the competitor’s positioning relative to the image.Use natural, clean JSON formatting and ensure the tone, metrics, and content feel authentic and tailored to the product’s market.Combine all the json file with key for product_name as name, product_category as category and for first as product_analysis,for second as product_review and for third as competitor_analysis. Generate in json format.'
        #         },
        #         {
        #             "role": "user",
        #             "content": [
        #                 {
        #                     "type": "image_url",
        #                     "image_url": {
        #                         "url": image
        #                     }
        #                 }
        #             ]
        #         }
        #     ])
        response = {
            "name": "Mac Laptop",
            "category": "Electronics",
            "product_analysis": [
                {
                    "year": "2020",
                    "units_sold": "1500000",
                    "average_rate": "$1200",
                    "sales": "$1800000000",
                    "growth_rate": "5.0%",
                    "market_trend": "growth",
                    "market_position": "Market leader in premium segment",
                    "market_drivers": "Consistent demand for high-performance and durable laptops from professionals and students. Strong brand loyalty and ecosystem integration with iPhone, iPad, and Apple Watch enhanced desirability.",
                    "market_challenges": "Increasing competition from Windows-based laptops with similar specs at lower prices. Global supply chain disruptions slightly affecting availability and pricing.",
                    "remarks": "MacBook maintained premium image despite global challenges."
                },
                {
                    "year": "2021",
                    "units_sold": "1600000",
                    "average_rate": "$1220",
                    "sales": "$1952000000",
                    "growth_rate": "5.5%",
                    "market_trend": "plateau",
                    "market_position": "Market leader in premium segment",
                    "market_drivers": "Consistent demand for high-performance and durable laptops from professionals and students. Strong brand loyalty and ecosystem integration with iPhone, iPad, and Apple Watch enhanced desirability.",
                    "market_challenges": "Increasing competition from Windows-based laptops with similar specs at lower prices. Global supply chain disruptions slightly affecting availability and pricing.",
                    "remarks": "MacBook maintained premium image despite global challenges."
                },
                {
                    "year": "2022",
                    "units_sold": "1700000",
                    "average_rate": "$1240",
                    "sales": "$2108000000",
                    "growth_rate": "6.0%",
                    "market_trend": "growth",
                    "market_position": "Market leader in premium segment",
                    "market_drivers": "Consistent demand for high-performance and durable laptops from professionals and students. Strong brand loyalty and ecosystem integration with iPhone, iPad, and Apple Watch enhanced desirability.",
                    "market_challenges": "Increasing competition from Windows-based laptops with similar specs at lower prices. Global supply chain disruptions slightly affecting availability and pricing.",
                    "remarks": "MacBook maintained premium image despite global challenges."
                },
                {
                    "year": "2023",
                    "units_sold": "1800000",
                    "average_rate": "$1260",
                    "sales": "$2268000000",
                    "growth_rate": "6.5%",
                    "market_trend": "plateau",
                    "market_position": "Market leader in premium segment",
                    "market_drivers": "Consistent demand for high-performance and durable laptops from professionals and students. Strong brand loyalty and ecosystem integration with iPhone, iPad, and Apple Watch enhanced desirability.",
                    "market_challenges": "Increasing competition from Windows-based laptops with similar specs at lower prices. Global supply chain disruptions slightly affecting availability and pricing.",
                    "remarks": "MacBook maintained premium image despite global challenges."
                },
                {
                    "year": "2024",
                    "units_sold": "1900000",
                    "average_rate": "$1280",
                    "sales": "$2432000000",
                    "growth_rate": "7.0%",
                    "market_trend": "growth",
                    "market_position": "Market leader in premium segment",
                    "market_drivers": "Consistent demand for high-performance and durable laptops from professionals and students. Strong brand loyalty and ecosystem integration with iPhone, iPad, and Apple Watch enhanced desirability.",
                    "market_challenges": "Increasing competition from Windows-based laptops with similar specs at lower prices. Global supply chain disruptions slightly affecting availability and pricing.",
                    "remarks": "MacBook maintained premium image despite global challenges."
                },
                {
                    "year": "2025",
                    "units_sold": "2000000",
                    "average_rate": "$1350",
                    "sales": "$2700000000",
                    "growth_rate": "4.5%",
                    "market_trend": "growth",
                    "market_position": "Leading the innovation curve with Apple Silicon and AI enhancements",
                    "market_drivers": "Increased adoption due to AI features, macOS enhancements, and sustainability efforts. Student discounts and remote work trends continue to push sales.",
                    "market_challenges": "High price tag remains a barrier for entry-level consumers. Competition from ARM-based Windows devices increasing.",
                    "remarks": "Future-proofing and innovation remain key MacBook strengths."
                },
                {
                    "year": "2026",
                    "units_sold": "2100000",
                    "average_rate": "$1375",
                    "sales": "$2887500000",
                    "growth_rate": "4.9%",
                    "market_trend": "plateau",
                    "market_position": "Leading the innovation curve with Apple Silicon and AI enhancements",
                    "market_drivers": "Increased adoption due to AI features, macOS enhancements, and sustainability efforts. Student discounts and remote work trends continue to push sales.",
                    "market_challenges": "High price tag remains a barrier for entry-level consumers. Competition from ARM-based Windows devices increasing.",
                    "remarks": "Future-proofing and innovation remain key MacBook strengths."
                },
                {
                    "year": "2027",
                    "units_sold": "2200000",
                    "average_rate": "$1400",
                    "sales": "$3080000000",
                    "growth_rate": "5.3%",
                    "market_trend": "growth",
                    "market_position": "Leading the innovation curve with Apple Silicon and AI enhancements",
                    "market_drivers": "Increased adoption due to AI features, macOS enhancements, and sustainability efforts. Student discounts and remote work trends continue to push sales.",
                    "market_challenges": "High price tag remains a barrier for entry-level consumers. Competition from ARM-based Windows devices increasing.",
                    "remarks": "Future-proofing and innovation remain key MacBook strengths."
                },
                {
                    "year": "2028",
                    "units_sold": "2300000",
                    "average_rate": "$1425",
                    "sales": "$3277500000",
                    "growth_rate": "5.7%",
                    "market_trend": "plateau",
                    "market_position": "Leading the innovation curve with Apple Silicon and AI enhancements",
                    "market_drivers": "Increased adoption due to AI features, macOS enhancements, and sustainability efforts. Student discounts and remote work trends continue to push sales.",
                    "market_challenges": "High price tag remains a barrier for entry-level consumers. Competition from ARM-based Windows devices increasing.",
                    "remarks": "Future-proofing and innovation remain key MacBook strengths."
                },
                {
                    "year": "2029",
                    "units_sold": "2400000",
                    "average_rate": "$1450",
                    "sales": "$3480000000",
                    "growth_rate": "6.1%",
                    "market_trend": "growth",
                    "market_position": "Leading the innovation curve with Apple Silicon and AI enhancements",
                    "market_drivers": "Increased adoption due to AI features, macOS enhancements, and sustainability efforts. Student discounts and remote work trends continue to push sales.",
                    "market_challenges": "High price tag remains a barrier for entry-level consumers. Competition from ARM-based Windows devices increasing.",
                    "remarks": "Future-proofing and innovation remain key MacBook strengths."
                },
                {
                    "year": "2030",
                    "units_sold": "2500000",
                    "average_rate": "$1475",
                    "sales": "$3687500000",
                    "growth_rate": "6.5%",
                    "market_trend": "plateau",
                    "market_position": "Leading the innovation curve with Apple Silicon and AI enhancements",
                    "market_drivers": "Increased adoption due to AI features, macOS enhancements, and sustainability efforts. Student discounts and remote work trends continue to push sales.",
                    "market_challenges": "High price tag remains a barrier for entry-level consumers. Competition from ARM-based Windows devices increasing.",
                    "remarks": "Future-proofing and innovation remain key MacBook strengths."
                }
            ],
            "product_review": [
                {
                    "platform": "Instagram",
                    "link": "https://instagram.com/post/1001",
                    "author": "user_1",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #instagramreview",
                    "engagement": "1012 likes"
                },
                {
                    "platform": "Twitter",
                    "link": "https://twitter.com/post/1002",
                    "author": "user_2",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #twitterreview",
                    "engagement": "1024 likes"
                },
                {
                    "platform": "TikTok",
                    "link": "https://tiktok.com/post/1003",
                    "author": "user_3",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #tiktokreview",
                    "engagement": "1036 likes"
                },
                {
                    "platform": "Reddit",
                    "link": "https://reddit.com/post/1004",
                    "author": "user_4",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #redditreview",
                    "engagement": "1048 likes"
                },
                {
                    "platform": "Google Reviews",
                    "link": "https://google reviews.com/post/1005",
                    "author": "user_5",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #google reviewsreview",
                    "engagement": "5.5 stars"
                },
                {
                    "platform": "YouTube",
                    "link": "https://youtube.com/post/1006",
                    "author": "user_6",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #youtubereview",
                    "engagement": "1072 likes"
                },
                {
                    "platform": "Instagram",
                    "link": "https://instagram.com/post/1007",
                    "author": "user_7",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #instagramreview",
                    "engagement": "1084 likes"
                },
                {
                    "platform": "Twitter",
                    "link": "https://twitter.com/post/1008",
                    "author": "user_8",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #twitterreview",
                    "engagement": "1096 likes"
                },
                {
                    "platform": "TikTok",
                    "link": "https://tiktok.com/post/1009",
                    "author": "user_9",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #tiktokreview",
                    "engagement": "1108 likes"
                },
                {
                    "platform": "Reddit",
                    "link": "https://reddit.com/post/1010",
                    "author": "user_10",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #redditreview",
                    "engagement": "1120 likes"
                },
                {
                    "platform": "Google Reviews",
                    "link": "https://google reviews.com/post/1011",
                    "author": "user_11",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #google reviewsreview",
                    "engagement": "5.1 stars"
                },
                {
                    "platform": "YouTube",
                    "link": "https://youtube.com/post/1012",
                    "author": "user_12",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #youtubereview",
                    "engagement": "1144 likes"
                },
                {
                    "platform": "Instagram",
                    "link": "https://instagram.com/post/1013",
                    "author": "user_13",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #instagramreview",
                    "engagement": "1156 likes"
                },
                {
                    "platform": "Twitter",
                    "link": "https://twitter.com/post/1014",
                    "author": "user_14",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #twitterreview",
                    "engagement": "1168 likes"
                },
                {
                    "platform": "TikTok",
                    "link": "https://tiktok.com/post/1015",
                    "author": "user_15",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #tiktokreview",
                    "engagement": "1180 likes"
                },
                {
                    "platform": "Reddit",
                    "link": "https://reddit.com/post/1016",
                    "author": "user_16",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #redditreview",
                    "engagement": "1192 likes"
                },
                {
                    "platform": "Google Reviews",
                    "link": "https://google reviews.com/post/1017",
                    "author": "user_17",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #google reviewsreview",
                    "engagement": "5.7 stars"
                },
                {
                    "platform": "YouTube",
                    "link": "https://youtube.com/post/1018",
                    "author": "user_18",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #youtubereview",
                    "engagement": "1216 likes"
                },
                {
                    "platform": "Instagram",
                    "link": "https://instagram.com/post/1019",
                    "author": "user_19",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #instagramreview",
                    "engagement": "1228 likes"
                },
                {
                    "platform": "Twitter",
                    "link": "https://twitter.com/post/1020",
                    "author": "user_20",
                    "caption": "Absolutely loving my new MacBook! Super fast and the battery life is insane! #twitterreview",
                    "engagement": "1240 likes"
                }
            ],
            "competitor_analysis": [
                {
                    "brand": "Dell",
                    "model": "XPS 13",
                    "average_price": "$999",
                    "target_audience": "Business professionals and students",
                    "key_features": "InfinityEdge display, Intel Evo certification, long battery life",
                    "strengths": "High build quality, sleek design, competitive pricing",
                    "weaknesses": "Thermal issues under load, Windows OS fragmentation",
                    "market_share_estimate": "12%",
                    "positioning": "Competitive alternative with a balance of performance and cost, but lacks ecosystem integration like Mac."
                },
                {
                    "brand": "HP",
                    "model": "Spectre x360",
                    "average_price": "$1099",
                    "target_audience": "Creative professionals and general users",
                    "key_features": "Touchscreen, 2-in-1 design, AMOLED display",
                    "strengths": "Flexible usage, good performance, stylish design",
                    "weaknesses": "Heavier than others, occasional driver issues",
                    "market_share_estimate": "9%",
                    "positioning": "Positioned as a stylish and flexible alternative, appealing to multimedia users more than hardcore professionals."
                },
                {
                    "brand": "Lenovo",
                    "model": "ThinkPad X1 Carbon",
                    "average_price": "$1299",
                    "target_audience": "Enterprise and government professionals",
                    "key_features": "Carbon fiber chassis, robust security features, legendary keyboard",
                    "strengths": "Durability, security, and enterprise support",
                    "weaknesses": "Less appealing to general consumers, conservative design",
                    "market_share_estimate": "8%",
                    "positioning": "Focused on enterprise and business reliability over consumer appeal, unlike Mac which spans both."
                },
                {
                    "brand": "Microsoft",
                    "model": "Surface Laptop 5",
                    "average_price": "$1199",
                    "target_audience": "Students and creative professionals",
                    "key_features": "PixelSense display, touch support, Windows Hello",
                    "strengths": "Tight Windows integration, beautiful screen, lightweight",
                    "weaknesses": "Limited ports, less powerful than Mac at the same price",
                    "market_share_estimate": "6%",
                    "positioning": "Well-positioned for users invested in Microsoft ecosystem, but less capable in hardware innovation."
                },
                {
                    "brand": "Asus",
                    "model": "ZenBook Duo",
                    "average_price": "$1399",
                    "target_audience": "Designers, coders, multitaskers",
                    "key_features": "Dual screens, high refresh rate, modern design",
                    "strengths": "Great for multitasking, futuristic design",
                    "weaknesses": "Battery life, software compatibility",
                    "market_share_estimate": "4%",
                    "positioning": "Innovative design attracts niche users; less mainstream appeal compared to Mac."
                }
            ]
        }
        return response
    except Exception as e:
        print(e)
        raise Exception("Failed to analyze the image.Please try again later")
