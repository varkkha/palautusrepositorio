from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print("TOML-tiedoston sisältö:")
        #print(content)

        data = toml.loads(content)
        #print("Derealisoitu data:")
        #print(data)

        name = data.get("tool", {}).get("poetry", {}).get("name", "Unknown Project")
        description = data.get("tool", {}).get("poetry", {}).get("description", "No description available")
        dependencies = list(data.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(data.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys())
        license_type = data.get("tool", {}).get("poetry", {}).get("license", "Unknown License")
        authors = data.get("tool", {}).get("poetry", {}).get("authors", [])

        return Project(name, description, license_type, authors, dependencies, dev_dependencies)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
      #  return Project("Test name", "Test description", [], [])
    
#if __name__ == "__main__":
 #   reader = ProjectReader("https://raw.githubusercontent.com/ohjelmistotuotanto-hy/tehtavat/main/viikko2/test-project/pyproject.toml") 
  #  reader.get_project() 