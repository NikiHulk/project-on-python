import subprocess

def generate_docs():
    try:
        result = subprocess.run(
            ['pydoctor', '--make-html', '--output-dir=docs', '--project-name="Voice Assistant"', 'src'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(result.stdout.decode())
        print("Документация успешно сгенерирована!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при генерации документации: {e.stderr.decode()}")

if __name__ == "__main__":
    generate_docs()
