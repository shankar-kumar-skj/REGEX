


from tavily import TavilyClient
tavily_client = TavilyClient(api_key="travily api key")
response = tavily_client.search("Who is Leo Messi?")
# print(response)
for result in response['results']:
    print(result['title'])
    print(result['url'])
    print(result['content'])
    print("---")




