import requests

url_ = [
    "https://arxiv.org/pdf/2506.02153",
    "https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf",
]
for indx, val in enumerate(url_):
    response = requests.get(val)
    response.raise_for_status()
    file_name = "file_pdf" + str(indx + 1) + ".pdf"
    with open(file_name, "wb") as f:
        f.write(response.content)

