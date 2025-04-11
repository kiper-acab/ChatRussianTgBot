import json
import bs4
import requests
from tqdm import tqdm

ROOT_URL = "https://3.shkolkovo.online"
APP_NAME = "practice"

EXAMS = {
    "Русский язык": {"id": 2, "slug": "russian"},
}

task_progress = tqdm(total=9313, desc="Tasks", position=1)
task_answer_list = []

def clean_html(html_content):
    soup = bs4.BeautifulSoup(html_content, "lxml")
    text = soup.get_text(separator="\n", strip=True)
    text = "\n\n".join([line.strip() for line in text.splitlines() if line.strip()])

    return text


for exam_name, exam_item in EXAMS.items():
    tqdm.write(f"Processing exam: {exam_name}")

    response = requests.get(f"{ROOT_URL}/catalog?SubjectId={exam_item['id']}").text
    soup = bs4.BeautifulSoup(response, "lxml")
    themes_divs = soup.find_all("div", class_="jsx-1658459108 accordion__item")

    for theme_div in themes_divs:
        subtopics_a = theme_div.find_all("a", class_="jsx-549154022")
        for subtopic_a in subtopics_a[:-1]:
            subtopic_url = ROOT_URL + subtopic_a.get("href")

            response = requests.get(subtopic_url).text
            tasks_soup = bs4.BeautifulSoup(response, "lxml")
            tasks_divs = tasks_soup.find_all("div", class_="exercise")
            
            number = tasks_soup.find("div", class_="content-with-aside__subtitle").text.split()[1][1:-1]

            for task_div in tasks_divs:
                try:
                    task_html = task_div.find("div", class_="exercise__text").decode_contents()
                    task_cleaned = clean_html(task_html)

                    answers = task_div.find_all(["span", "li"], class_="answer")
                    clean_answers = [answer.text.strip() for answer in answers]

                    explanation_div = task_div.find("div", class_="exercise__solution-text")
                    explanation_html = explanation_div.find("div", class_="tex-render").decode_contents() if explanation_div else ""
                    explanation_cleaned = clean_html(explanation_html)

                    if clean_answers:
                        task_answer_list.append({
                            "number": number,
                            "task": task_cleaned,
                            "asnwer": clean_answers[0],
                            "explanation": explanation_cleaned,
                        })

                    task_progress.update(1)

                except AttributeError:
                    pass


with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(task_answer_list, f, ensure_ascii=False, indent=4)

tqdm.write("Completed 🌟!")
