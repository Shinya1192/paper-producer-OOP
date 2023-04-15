import arxiv
import openai
import random

# OpenAI's API key
openai.api_key = 'openAIキーを入力してください。'


def get_summary(result):
    try:
        system = """与えられた論文の要点を3点のみでまとめ、以下のフォーマットで日本語で出力してください。```
        タイトルの日本語訳
        ・要点1
        ・要点2
        ・要点3
        ```"""

        text = f"title: {result.title}\nbody: {result.summary}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': 'system', 'content': system},
                {'role': 'user', 'content': text}
            ],
            temperature=0.25,
        )
        summary = response['choices'][0]['message']['content']
        title_en = result.title
        title, *body = summary.split('\n')
        body = '\n'.join(body)
        date_str = result.published.strftime("%Y-%m-%d %H:%M:%S")
        message = f"発行日: {date_str}\n{result.entry_id}\n{title_en}\n{title}\n{body}\n"

        return message
    except Exception as e:
        print(f"Error in generating summary: {e}")
        return None


def get_papers():
    # Prepare the query
    query = 'ti:%22 Deep Learning %22'

    # Fetch the latest paper information using the arxiv API
    search = arxiv.Search(
        query=query,
        max_results=100,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    # Store the search results in a list
    result_list = []
    for result in search.results():
        result_list.append(result)

    # Randomly select num_papers
    num_papers = 3
    results = random.sample(result_list, k=num_papers)

    # Store the assembled messages in a list
    messages = []
    for i, result in enumerate(results):
        message = get_summary(result)
        if message:
            message = "今日の論文です！ " + str(i + 1) + "本目\n" + message
            messages.append(message)
        else:
            print("Failed to generate summary for a paper.")
    return messages
