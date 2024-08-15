import requests 

def fetch_papers(query, limit=1):
    query = query.replace(" ", "+")  # Replace spaces with '+' for URL encoding
    offset = 0  
    fields="title,abstract,authors,citationCount,year,venue,tdlr"
    # url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit={limit}&offset={offset}&fields={fields}"
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "offset": offset,
        "fields": fields
    }

    response = requests.get(url, params = params)

    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content.decode('utf-8')}")
    
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Error: Unable to fetch papers (Status Code: {response.status_code})")
        return None
    

