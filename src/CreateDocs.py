import subprocess
import os

def generate_docs():
    # Укажите путь к вашей папке с кодом
    project_dir = os.path.join(os.getcwd(), "my_project")
    # Путь к папке, куда будет сохраняться документация
    output_dir = os.path.join(os.getcwd(), "docs")

    # Запуск PyDoctor
    subprocess.run(["pydoctor", "--output", output_dir, "--project-name", "MyProject", project_dir])

if __name__ == "__main__":
    generate_docs()
