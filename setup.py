from setuptools import find_packages,setup

setup(
    name="mcqgen",
    version="0.0.1",
    author="Debasis P",
    author_email="pdebasis2013@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","pandas","AzureOpenAI"],
    packages=find_packages()
)
