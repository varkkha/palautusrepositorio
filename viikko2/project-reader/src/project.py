class Project:
    def __init__(self, name,  description, license_type, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license_type = license_type
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, items):
        return "\n- ".join(items) if len(items) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license_type}"
            f"\n"
            f"\nAuthors:\n- {self._stringify_list(self.authors)}"
            f"\n"
            f"\nDependencies:\n- {self._stringify_list(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:\n- {self._stringify_list(self.dev_dependencies)}"
        )
