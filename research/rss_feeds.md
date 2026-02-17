# arXiv Feeds for LLM Agent Security Monitoring

## Category Feeds
- `cs.CR` – <https://export.arxiv.org/rss/cs.CR>
- `cs.AI` – <https://export.arxiv.org/rss/cs.AI>
- `cs.CL` – <https://export.arxiv.org/rss/cs.CL>
- `cs.LG` – <https://export.arxiv.org/rss/cs.LG>
- `stat.ML` – <https://export.arxiv.org/rss/stat.ML>

## Keyword / Topic Feeds
1. **LLM / Foundation Model + Security (broad)**  
   <https://export.arxiv.org/api/query?search_query=%28all%3A%22large%20language%20model%22%20OR%20all%3ALLM%20OR%20all%3A%22foundation%20model%22%29%20AND%20%28all%3Asecurity%20OR%20all%3Asafety%20OR%20all%3Ajailbreak%20OR%20all%3A%22prompt%20injection%22%20OR%20all%3Aprivacy%20OR%20all%3Abackdoor%20OR%20all%3Apoisoning%20OR%20all%3Aexfiltration%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending>
2. **Prompt Injection / Tool Use / Agent Safety**  
   <https://export.arxiv.org/api/query?search_query=%28all%3A%22prompt%20injection%22%20OR%20all%3A%22indirect%20prompt%20injection%22%20OR%20all%3A%22tool%20use%22%20OR%20all%3Aagent%29%20AND%20%28all%3A%22large%20language%20model%22%20OR%20all%3ALLM%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending>
3. **Jailbreak / Adversarial Prompts / Red Teaming**  
   <https://export.arxiv.org/api/query?search_query=%28all%3Ajailbreak%20OR%20all%3A%22prompt%20attack%22%20OR%20all%3A%22adversarial%20prompt%22%20OR%20all%3A%22red%20teaming%22%29%20AND%20%28all%3A%22large%20language%20model%22%20OR%20all%3ALLM%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending>
4. **Training-stage Poisoning / Backdoor**  
   <https://export.arxiv.org/api/query?search_query=%28all%3Apoisoning%20OR%20all%3A%22data%20poisoning%22%20OR%20all%3Abackdoor%20OR%20all%3A%22trojan%22%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending>
5. **Deployment-stage Privacy / Membership Inference / Data Extraction**  
   <https://export.arxiv.org/api/query?search_query=%28all%3A%22membership%20inference%22%20OR%20all%3A%22training%20data%20extraction%22%20OR%20all%3A%22data%20exfiltration%22%20OR%20all%3Aprivacy%29%20AND%20%28all%3A%22large%20language%20model%22%20OR%20all%3ALLM%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending>

_Notes:_
- All feeds sorted by submission date descending.
- `max_results=100` gives a rolling window; adjust if API caps become an issue.
- Feeds can be fetched via `curl`/`web_fetch` and parsed as Atom/RSS.
