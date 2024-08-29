# from fetch_papers import fetch_papers
from models.summarize import get_text, summarize_text


if __name__ == "__main__":

    papers = summarize_text()
    # print(f"Text: {papers}")

    # query = "Intermittent Fasting"
    # papers = fetch_papers(query)
    # for idx, paper in enumerate(papers):
    #     print(f"Paper {idx}: {paper['title']}")
    #     print(f"Authors: {', '.join([author['name'] for author in paper['authors']])}")
    #     print(f"Abstract: {paper.get('abstract', 'No abstract available')}")
    #     print(f"Citations: {paper['citationCount']}")
    #     print(f"Published in: {paper['venue']} ({paper['year']})")
    #     print(f"TLDR: {paper.get('tldr', 'No TLDR available')}")
    #     print("-" * 40)