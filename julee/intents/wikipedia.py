import wikipedia


def get_wikipedia(command):
    query = command.lower()
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=1)
        result = "According to Wikipedia, " + results
    except wikipedia.exceptions.WikipediaException:
        result = None
    return result
