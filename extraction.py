
def get_github_trending():
    url = "https://github.com/trending"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Erro ao acessar a página:", response.status_code)
        return

    soup = BeautifulSoup(response.text, "html.parser")
    repos = soup.find_all("article", class_="Box-row")

    # Abrindo arquivo CSV
    with open("trending.csv", "w", encoding="utf-8") as f:
        f.write("ranking;project;language;stars;stars_todays;forks\n")

        for i, repo in enumerate(repos, start=1):

            # Nome do projeto (owner/repo)
            project = (
                repo.h2.a.get_text(strip=True)
                .replace("\n", "")
                .replace(" ", "")
            )

            # Linguagem (pode não existir)
            lang_tag = repo.find("span", itemprop="programmingLanguage")
            language = lang_tag.get_text(strip=True) if lang_tag else "N/A"

            # Stars e Forks
            links = repo.find_all("a", class_="Link--muted")

            stars = (
                links[0].get_text(strip=True).replace(",", "")
                if len(links) > 0
                else "0"
            )

            forks = (
                links[1].get_text(strip=True).replace(",", "")
                if len(links) > 1
                else "0"
            )

            # Stars hoje
            stars_today_tag = repo.find(
                "span", class_="d-inline-block float-sm-right"
            )

            stars_today = (
                stars_today_tag.get_text(strip=True).split(" ")[0]
                if stars_today_tag
                else "0"
            )

            linha = f"{i};{project};{language};{stars};{stars_today};{forks}\n"

            print(linha.strip())
            f.write(linha)

    print("\nArquivo 'trending.csv' criado com sucesso.")


if __name__ == "__main__":
    get_github_trending()
